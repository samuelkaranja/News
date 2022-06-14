from django.contrib import admin
from . models import Post, Newsletter, Comment, Contact
# Register your models here.

admin.site.register(Post)
admin.site.register(Newsletter)
admin.site.register(Comment)
admin.site.register(Contact)