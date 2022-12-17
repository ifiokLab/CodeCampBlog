
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
#from traitlets import default #import this
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
# Create your models here.

class myuser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40,blank=False)
    last_name = models.CharField(max_length=40,blank=False)
    #profile_image = models.ImageField(upload_to='Files/')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BlogAuthor(models.Model):
    user = models.OneToOneField(myuser, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.user}'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,default='')
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    tags = TaggableManager() 
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/',default = '') 
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(BlogAuthor,on_delete=models.CASCADE,related_name='blog_posts')
    body= RichTextUploadingField() 

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post_Detail',args=[self.id])

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)



class BlogComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = 'comments')
    User = models.ForeignKey(myuser,on_delete=models.CASCADE,default = '')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)#manually deactivate inappropriate post from admin site
    parent = models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.User}'

    @property
    def children(self):
        return BlogComment.objects.filter(parent = self).reverse()
    
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
        

    
