from django.urls import path
from . import views

urlpatterns = [
    # 팔로우
    path('<int:user_pk>/follow/', views.follow),
    # 다른 유저 정보 가져오기
    path('<int:user_pk>/anotherinfo/', views.anotherinfo),
]