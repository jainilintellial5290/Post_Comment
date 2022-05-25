from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.

class showPost(admin.ModelAdmin):
    list_display = ['postid','author','title','content','date']
    
admin.site.register(Post,showPost)

class showComment(admin.ModelAdmin):
    list_display = ['sno','post','comment']

admin.site.register(Comment,showComment)

class showLike(admin.ModelAdmin):
    list_display =  ['post','value','user']
    
admin.site.register(Like,showLike)

