from django.contrib import admin
from django.urls import path, include
from social import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('user/<str:username>/', views.user_posts, name='user_posts'),
    path('like/<int:id>/', views.like_post, name='like_post'),
]