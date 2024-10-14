# Shih-Tzu
영화 추천 및 리뷰 커뮤니티

## 프로젝트 설명
이 프로젝트는 사용자들이 시간에 대한 영화 추천을 받고, 영화에 대한 리뷰를 작성하며 다른 사용자들과 소통할 수 있는 영화 리뷰 커뮤니티 웹 애플리케이션입니다. Django를 백엔드로, Vue.js를 프론트엔드로 사용하여 개발되었습니다. 사용자는 시간과 장소, 누구와 함께하는지에 대한 여러 조건으로 영화를 추천받을 수 있습니다.

## 주요 기능
### 영화 추천 알고리즘
- 코사인 유사도 알고리즘
    ```python
    # final-pjt-back/movies/views.py

    # 코사인 유사도 계산을 위한 함수
    def cos_sim(A, B):
        return dot(A, B)/(norm(A)*norm(B))

    # 줄거리와 상관 없는 단어 빈도수 체크에서 제외
    def preprocess_stopwords(stopwords):
        return [word.strip().lower() for word in stopwords]

    # 객체별 벡터 변환 값들이 저장될 데이터
    data_cache = {
        "df": None,
        "tfidf_matrix": None,
        "cos_sim_matrix": None,
        "indices": None
    }
    
    # 첫 유사도 계산 전 데이터 초기화 및
    # 유사도 계산에 필요한 필드 구성
    def initalize_data_cache():
        global data_cache
        
        # 유사도 계산을 위한 함수가 처음 호출 될 때  전체 영화 목록을 저장
        # 이후 동일한 요청 시 저장된 영화 목록에서 계산
        if data_cache["df"] is None:
            conn = sqlite3.connect('db.sqlite3')
            query = '''
                    SELECT 
                        id,
                        title,
                        overview,
                        poster_path,
                        vote_avg,
                        released_date,
                        backdrop_path
                    FROM 
                        movies_movie
                    '''
            df = pd.read_sql_query(query, conn)
            conn.close()

            stopwords_path = os.path.join(os.path.dirname(__file__), 'stopwords.txt')

            with open(stopwords_path, 'r', encoding='utf-8') as file:
                korean_stopwords = file.read().splitlines()

            korean_stopwords = preprocess_stopwords(korean_stopwords)

            # tf-idf: 중요한 내용을 추출하여 문서의 유사도를 판단
            # 각 단어의 빈도수를 체크하여 행렬로 변경, 벡터화
            tfidf = TfidfVectorizer(stop_words=korean_stopwords)
            # 줄거리를 기준으로 유사도 검사
            tfidf_matrix = tfidf.fit_transform(df['overview'])

            # 벡터의 방향이 비슷할수록, 유사한 영화라고 판단할 수 있음
            cos_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
            indices = pd.Series(df.index, index=df['id']).drop_duplicates()

            data_cache["df"] = df
            data_cache["tfidf_matrix"] = tfidf_matrix
            data_cache["cos_sim_matrix"] = cos_sim_matrix
            data_cache["indices"] = indices
    
    # 유사한 영화 찾기 알고리즘
    def get_recommendations(id, cos_sim=cos_sim):
        initalize_data_cache()

        df = data_cache["df"]
        cos_sim = data_cache["cos_sim_matrix"]
        indices = data_cache["indices"]

        idx = indices[id]

        # 각 영화의 코사인 유사도를 리스트로 저장 및 정렬
        sim_scores = list(enumerate(cos_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:13]

        movies_indices = [i[0] for i in sim_scores]

        recommendations = df[['id', 'title', 'overview', 'poster_path', 'backdrop_path', 'vote_avg', 'released_date']].iloc[movies_indices]

        return recommendations
    
    # 아래 함수가 호출되면, 기준 영화와 유사한 영화를 json으로 반환
    def similar(request, movie_id):
        recommend_movies = get_recommendations(movie_id)
        recommendations_list = recommend_movies.to_dict(orient='records')
        return JsonResponse(recommendations_list, safe=False, json_dumps_params={'ensure_ascii': False})
    ```
  > 각 영화의 줄거리 데이터에서 중요하다고 판단되는 단어들의 빈도수를 행렬화 및 벡터화 하여 각 객체의 코사인 유사도를 검사하는 알고리즘입니다.
- 시간별 추천 [시츄, Shih-Tzu] 알고리즘
    ```python
    # final-pjt-back/movies/views.py

    # 시간별 영화 추천 알고리즘
    def shihtzu(request):
    preferences = request.GET

    # 장소에 따라 현재 상영중인 영화 필터링
    if preferences.get('where') == 'Theater':
        movies = Movie.objects.filter(now_playing=True)
    else:
        movies = Movie.objects.filter(now_playing=False)
    
    # 현재 시간 or 지정된 시간
    if preferences.get('time') == 'now':
        time = datetime.now()
        target_time = int(time.strftime("%H")) + 1
    elif preferences.get('time') == 'left':
        target_time = 13
    else:
        target_time = 21
    
    recommended_genres = []
    
    # 주말 여부에따라 런타임 필터링
    if preferences.get('isWeekend') == 'true':
        movies = movies.filter(runtime__gte=90)
    else:
        movies = movies.filter(runtime__lt=90)

    # 시간에 따라 장르 추천
    if target_time // 6 == 0:
        recommended_genres.extend([27, 28, 9648, 878])
    elif target_time // 6 == 1:
        recommended_genres.extend([99, 18, 36, 10751])
    elif target_time // 6 == 2:
        recommended_genres.extend([35, 16, 12, 14])
    else:
        recommended_genres.extend([53, 80, 18, 10749])

    # 누구와 함께 볼 것인지에 따라 장르 추천
    if preferences.get('withWho') == 'Alone':
        recommended_genres.extend([27, 9648, 878, 99])
    elif preferences.get('withWho') == 'Friend':
        recommended_genres.extend([35, 28, 53, 12])
    elif preferences.get('withWho') == 'Family':
        recommended_genres.extend([18, 10751, 16, 12])
    elif preferences.get('withWho') == 'Couple':
        recommended_genres.extend([10749, 35, 18, 10402])
    else:
        # Kids Family의 경우, 애니메이션, 가족 장르만 필터링
        movies = movies.filter(genres__pk__in=[16, 10751]).distinct().order_by('-popularity')[:50]
        movies = random.sample(list(movies), min(len(movies), 30))
        serializer = MovieListSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    genre_counts = {genre: recommended_genres.count(genre) for genre in set(recommended_genres)}

    # 추천 받은 장르에 따라 영화의 popularity에 가중치 더해주기
    # 한 번 추천 받으면 400, 두 번 받으면 1200
    for movie in movies:
        genre_ids = movie.genres.values_list('pk', flat=True)
        popularity_boost = sum([400 if genre_counts[genre] == 1 else 1200 for genre in genre_ids if genre in genre_counts])
        movie.popularity += popularity_boost

    # 인기도 기준 50개를 잘라서, 랜덤 배치 후 30개 추천
    movies = movies.distinct().order_by('-popularity')[:50]
    movies = random.sample(list(movies), min(len(movies), 30))

    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    ```

  > 각 영화 데이터를 받아올 때, popularity라는 필드가 있는 것을 보고 이 필드를 잘 활용하면 좋을 것 같다 생각해서 알고리즘을 구현해보았습니다.
  >
  > 직접 데이터를 확인해 봤을 때, 대부분의 영화 인기도가 200 ~ 700 정도 사이에 분포하고 있고, 작게는 한 자리수까지, 크게는 2000까지도 있는 것을 보았습니다. 이 정도의 차이를 보이는 지표라면, 이미 높은 인기도를 가진 영화는 대부분의 기준에서 추천 받아 마땅한 영화라고 판단, 대부분의 기준에서 추천 영화에 포함되도록 의도했습니다.
  >
  > 시간 별, 누구와 함께 볼 것인지에 따라 추천해주는 장르는 Chat Gpt의 추천에 주관적인 의견을 포함하여 설정했습니다.
  >
  > 추천을 한 번 받은 장르는 인기도에 가중치를 400, 두 번 중복으로 받게되면 1200을 더하고 인기도를 기준으로 영화를 정렬하여 추천하게 됩니다.
  >
  > 매번 같은 영화가 추천되는 것을 방지하고자, 인기도가 높은 영화 50개를 받아 랜덤으로 배치 후 30개까지 추천하도록 구현되어있습니다.
- ChatGpt API활용 챗봇 구현
    ```python
    def AIRecommend(request):
    preferences = request.GET
    where = preferences.get('where')
    time = preferences.get('time')
    
    if where == 'Theater':
        movies = Movie.objects.filter(now_playing=True)
    else:
        movies = Movie.objects.filter(now_playing=False)

    if time == 'now':
        time = datetime.now().strftime("%H:%M")
    elif time == 'left':
        time = '13:00'
    else:
        time = '21:00'

    withWho = preferences.get('withWho')
    openai.api_key = settings.OPENAI_API_KEY
    messages = [
        {
            "role": "user",
            "content": """
            '다음은 전체 영화 장르 목록입니다:
            {"id": 28, "name": "action"},
            {"id": 12, "name": "adventure"},
            {"id": 16, "name": "animation"},
            {"id": 35, "name": "comedy"},
            {"id": 80, "name": "crime"},
            {"id": 99, "name": "documentary"},
            {"id": 18, "name": "drama"},
            {"id": 10751, "name": "family"},
            {"id": 14, "name": "fantasy"},
            {"id": 36, "name": "history"},
            {"id": 27, "name": "horror"},
            {"id": 10402, "name": "music"},
            {"id": 9648, "name": "mystery"},
            {"id": 10749, "name": "romance"},
            {"id": 878, "name": "SF"},
            {"id": 10770, "name": "TV movie"},
            {"id": 53, "name": "thriller"},
            {"id": 10752, "name": "war"},
            {"id": 37, "name": "western"}            
            다음 상황에 따라 어울리는 영화 장르를 이유와 함께 추천해주세요: [Where, with whom, at what time]
            단, 추천하는 장르의 id를 반드시 문장에 맨 앞에 리스트 형태로 포함시켜주세요
            """
        }
    ]
    situations = [{"role": "user", "content": f'[{where}, {withWho}, {time}]'}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages+situations
    )
    assistant_reply = response['choices'][0]['message']['content']
    genre_ids = re.findall(r'\b\d+\b', assistant_reply)
    genre_ids = [int(id) for id in genre_ids]

    movies = Movie.objects.filter(genres__pk__in=genre_ids).distinct().order_by('-popularity')[:50]
    
    # 영화 리스트에서 랜덤 샘플링
    movies = random.sample(list(movies), min(len(movies), 30))
    
    # 응답 데이터 직렬화
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse({
        'assistant_reply': assistant_reply,
        'movies': serializer.data
    }, safe=False, json_dumps_params={'ensure_ascii': False})
    ```
  > ChatGpt에게 시간, 장소, 누구와 함께 할 것인지에 따라 영화 장르를 추천 받도록 하였습니다. 미리 만들어 둔 프롬포트에 따라 영화 장르의 id를 필수로 추천 받고, 이후 이유까지 함께 답변 받을 수 있습니다.

### 사용자 인증 및 관리
- 회원가입, 로그인, 로그아웃
- 프로필 관리 (프로필 사진 업로드 포함)
- 비밀번호 변경 및 계정 삭제

### 영화 검색 및 정보 제공
- 영화 검색 기능
  - 장르 별 검색
  - 제목에 포함된 문자열 검색
- 영화 상세 정보 제공 (제목, 개봉일, 줄거리 등)

### 리뷰 기능
- 리뷰 작성, 삭제
- 각 사용자의 프로필에서 리뷰 목록 보기

### 팔로우 기능
- 다른 사용자 팔로우 및 언팔로우
  - 랭킹 시스템 적용
- 팔로워 및 팔로잉 목록 보기

### 랭킹 시스템
- 팔로워를 많이 받은 순서대로 3명까지, 좋아요 표시 한 영화 리스트 제공
  
### 근처 영화관 찾기
- 위치 기반 근처 영화관 검색
  
### 기술 스택
- 백엔드: Django, Django REST Framework, Django Allauth, DJ-Rest-Auth
- 프론트엔드: Vue.js
- 데이터베이스: SQLite (로컬 개발용 및 배포용)
- 배포: Render.com

## 프로젝트 설정 및 실행 방법
### 백엔드 (Django)
1. 의존성 설치
    ```bash
    pip install -r requirements.txt
    ```
2. 데이터베이스 마이그레이션
    ```bash
    python manage.py migrate
    ```
3. 영화 데이터 로드
    ```bash
    python manage.py loaddata genres.json movies.json users.json
    ```
4. 개발 서버 실행
    ```bash
    python manage.py runserver
    ```
### 프론트엔드 (Vue.js)
1. 의존성 설치
    ```bash
    npm install
    ```
2. 개발 서버 실행
    ```bash
    npm run dev
    ```
## 환경 변수 설정
.env 파일을 back, front 디렉토리에 각각 생성하고, 다음과 같이 설정합니다:

```env
# back/.env

SECRET_KEY='your_secret_key'
# 로컬
DEBUG=True
# 배포
DEBUG=False
OPENAI_API_KEY='your_openai_api_key'
```
```env
# front/.env

VITE_APP_YOUTUBE_API_KEY='your_youtube_api_key'
VITE_APP_MAP_API_KEY='your_kakao_api_key'
VITE_APP_YOUTUBE_API_URL=https://www.googleapis.com/youtube/v3/search
VITE_APP_AUTH_API_URL=http://localhost:8000/api/
VITE_APP_MOVIE_API_URL=http://127.0.0.1:8000/api/movies/
VITE_APP_COMMNET_API_URL=http://127.0.0.1:8000/api/v1/
```


## 프로젝트 구조
```plaintext
📦final-pjt
 ┣ 📂final-pjt-back
 ┃ ┣ 📂accounts         # 계정
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜signals.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┗ 📜views.py
 ┃ ┣ 📂comments         # 리뷰
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┣ 📂movies           # 영화
 ┃ ┃ ┣ 📂fixtures
 ┃ ┃ ┃ ┣ 📜genres.json
 ┃ ┃ ┃ ┣ 📜movies.json
 ┃ ┃ ┃ ┗ 📜users.json
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜serializer.py
 ┃ ┃ ┣ 📜stopwords.txt  # 코사인 유사도 분석 시 제외할 단어
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┣ 📂Shih_Tzu         # 메인 프로젝트
 ┃ ┃ ┣ 📜settings.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┣ 📜.env
 ┃ ┣ 📜manage.py
 ┃ ┗ 📜requirements.txt
 ┣ 📂final-pjt-front
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┣ 📜AITextModal.vue              # chat gpt 추천 모달
 ┃ ┃ ┃ ┣ 📜BoxOffice.vue                # 박스 오피스
 ┃ ┃ ┃ ┣ 📜MovieModal.vue               # 영화 세부정보 모달
 ┃ ┃ ┃ ┣ 📜RecommendMovie.vue           # 추천 영화
 ┃ ┃ ┃ ┣ 📜RecommendPreview.vue         # 추천받기 전 기준 선택
 ┃ ┃ ┃ ┗ 📜YoutubeTrailerModal.vue      # 유튜브 트레일러 모달
 ┃ ┃ ┣ 📂router
 ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┣ 📂stores
 ┃ ┃ ┃ ┣ 📜auth.js                      # 계정 및 인증 관련 스토어
 ┃ ┃ ┃ ┣ 📜comments.js                  # 리뷰 관련 스토어
 ┃ ┃ ┃ ┗ 📜movie.js                     # 영화 관련 스토어
 ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┣ 📜CinemaView.vue               # 영화관찾기
 ┃ ┃ ┃ ┣ 📜CollectionView.vue           # 좋아요 누른 영화 목록
 ┃ ┃ ┃ ┣ 📜FollowerView.vue             # 팔로워 목록
 ┃ ┃ ┃ ┣ 📜FollowingView.vue            # 팔로잉 목록
 ┃ ┃ ┃ ┣ 📜HomeView.vue                 # 메인 페이지
 ┃ ┃ ┃ ┣ 📜LoginView.vue                # 로그인 페이지
 ┃ ┃ ┃ ┣ 📜ProfileCommentsView.vue      # 프로필 - 리뷰 목록
 ┃ ┃ ┃ ┣ 📜ProfileUpdateView.vue        # 사용자 정보 업데이트
 ┃ ┃ ┃ ┣ 📜ProfileView.vue              # 사용자 프로필
 ┃ ┃ ┃ ┣ 📜RankingView.vue              # 컬렉션 정렬
 ┃ ┃ ┃ ┣ 📜RegisterView.vue             # 회원가입 페이지
 ┃ ┃ ┃ ┣ 📜SearchView.vue               # 영화 검색 페이지
 ┃ ┃ ┃ ┗ 📜ShihTzuView.vue              # 시간 별 추천 페이지
 ┃ ┃ ┣ 📜App.vue
 ┃ ┃ ┗ 📜main.js
 ┃ ┣ 📜.env
 ┃ ┣ 📜index.html
 ┃ ┣ 📜package-lock.json
 ┃ ┣ 📜package.json
 ┃ ┗ 📜vite.config.js
 ┗ 📜README.md
```
## 기여 방법
- 이 저장소를 포크합니다.
- 새로운 브랜치를 생성합니다.
    `git branch feature/your-feature`
- 생성한 브랜치로 전환합니다.
    `git switch feature/your-feature`
- 변경 사항을 커밋합니다.
    `git commit -m 'Add some feature'`
- 브랜치에 푸시합니다.
    `git push origin feature/your-feature`
- 풀 리퀘스트를 생성합니다.

## 문의
프로젝트 관련 문의는 다음 이메일로 연락주시기 바랍니다:

[dakgoo02@naver.com](mailto:dakgoo02@naver.com)

[andyandy0409@naver.com](mailto:andyandy0409@naver.com)


## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 아래를 참조하세요.

MIT License

Copyright (c) [2024] [이유찬, 최지우]