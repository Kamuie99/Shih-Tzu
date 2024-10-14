from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_followed(request, username):
    target_user = get_object_or_404(User, username=username)
    is_followed = target_user.followers.filter(id=request.user.id).exists()
    return Response({'is_followed': is_followed})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, username):
    target_user = get_object_or_404(User, username=username)
    req_user = request.user
    if req_user.following.filter(username=username).exists():
        req_user.following.remove(target_user)
        followed = False
    else:
        req_user.following.add(target_user)
        followed = True
    
    return JsonResponse({'followed': followed})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request):
    try:
        user = request.user
        if 'image' in request.FILES:
            image = request.FILES['image']
            
            path = default_storage.save(image.name, ContentFile(image.read()))

            user.profile_image = path
            user.save()
        
        image_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{user.profile_image}")
        return Response({'message': 'User updated successfully', 'path': image_url}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    current_password = request.data.get('current_password')
    new_password1 = request.data.get('new_password1')
    new_password2 = request.data.get('new_password2')

    if not user.check_password(current_password):
        return Response({"detail": "현재 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    if new_password1 != new_password2:
        return Response({"detail": "새 비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password1)
    user.save()
    return Response({"detail": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, username):
    try:
        req_user = request.user
        print(req_user)
        user = get_object_or_404(User, username=username)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
