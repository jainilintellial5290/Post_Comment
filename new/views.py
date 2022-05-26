from argparse import ONE_OR_MORE
from os import unlink
from django.shortcuts import render, redirect
from .models import Post, Comment, Like
# Create your views here.

def index(request):
    global get_post
    fetchdata = Post.objects.values("postid","author","title","content","liked","date")
    print(fetchdata, "fetch_dataaaa")
    post_comment = Comment.objects.values("comment","sno","user","post")
    list = []
    get_like = Like.objects.values("value","post")
    for likes in get_like:
        list.append(likes)
    print(list,"get_likkkkkk")                        
    print(get_like, "likesss")
    # print(post_comment, 'hfdhfdhdfh') 
    context = {"fetchdata":fetchdata, "post_comment":post_comment}
    return render(request, "index.html", context)
     
    
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        comment = Comment(comment=comment)
        comment.save()

    return render(request,'comment.html')

def compose(request):
    if request.method == "POST":
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        compose = Post(author=author, title=title, content=content, date=date)
        print(compose,"ssssssssss")
        compose.save()

    return render(request,'compose.html')

def like(request):
    user = request.user  
    if request.method == "POST":
        postid = request.POST.get('postid')
        post_obj = Post.objects.get(postid=postid)

        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)    
            
        like, created = Like.objects.get_or_create(user=user,post_id=postid)
            
        if not created:
            if like.value == 'Like':
                like.value == 'Unlike'
            else:
                like.value = 'Unlike'
        like.save()

    return redirect("/")
