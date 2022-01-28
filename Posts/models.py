from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.

CATEGORY_CHOICES = (
    ("Lifestyle", "Lifestyle"),
    ("Fashion", "Fashion"),
    ("Technology", "Technology"),
    ("Entertainment", "Entertainment"),
    ("CryptoCurrency", "CryptoCurrency"),
    ("Art", "Art"),
    ("Travel", "Travel"),
    ("Health", "Health"),
    ("Food", "Food"),
    ("Nature", "Nature"),
    ("Gaming", "Gaming"),
)

TAG_CHOICES = (
    ("MainContent", "MainContent"),
    ("SubContent", "SubContent"),
    ("News", "News"),
    ("TopPost", "TopPost"),
    ("Popular", "Popular")
)

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=100, choices = CATEGORY_CHOICES, blank=True)
    image = models.ImageField(upload_to="Article/images")
    description = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=200, choices = TAG_CHOICES, blank=True)

    def __str__(self):
        return self.title

class PostReply(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.firstName

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email