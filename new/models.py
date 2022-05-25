from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    liked = models.ManyToManyField(User, default=None, blank=True)
    date = models.DateField(default=now)


    def __str__(self):
        return str(self.author)

    @property
    def num_likes(self):
        return self.liked.all().count()
 
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Comment(models.Model):
    comment=models.TextField()
    sno= models.AutoField(primary_key=True,null=False, default=None)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, default=None)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.post)

        
