from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('details/<int:pk>/', views.details, name="details"),
    path('CreateNewPost/', views.createPost, name="createPost"),
    path('About-Us/', views.About, name="about"),
    path('Contact-Us/', views.Contact, name="contact"),
]