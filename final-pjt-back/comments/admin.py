from django.contrib import admin
from .models import Comment, Review
# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)