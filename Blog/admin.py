from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(myuser)
admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
