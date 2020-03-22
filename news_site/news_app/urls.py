from django.urls import path, include
from .views import news_view, post_detail

urlpatterns = [
    path('', news_view, name='home'),
    path('post/<int:id>', post_detail, name='post_detail'),
]
