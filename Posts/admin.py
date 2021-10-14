from django.contrib import admin
from . models import Post, Newsletter, PostReply
# Register your models here.

admin.site.register(Post)
admin.site.register(Newsletter)
admin.site.register(PostReply)