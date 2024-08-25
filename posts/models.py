from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
class Post (models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)  
    banner = models.ImageField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    status = models.IntegerField(choices=STATUS, default=0)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    