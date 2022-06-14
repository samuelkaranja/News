from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
# Create your models here.

CATEGORY_CHOICES = (
    ("Breaking News", "Breaking News"),
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

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.firstname + self.lastname
