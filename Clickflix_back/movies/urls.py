from django.urls import path
from . import views

urlpatterns = [
    # recommend
    path('recommend/anonymous/', views.recommend_anonymous), # 메인 추천리스트(비회원)
    path('recommend/<int:user_pk>/', views.recommend_user), # 메인 추천리스트(회원)
    path('recommend/allrandom/', views.all_random), # 올랜덤 선택 한개

    # search movie page(all_list)
    path('listall/', views.movie_list),

    # Detail modal page
    path('<int:movie_pk>/', views.movie_detail),

    # like_movie
    path('<int:movie_pk>/like/', views.like_movie),

    # wish_watch
    path('<int:movie_pk>/wish/', views.add_watchlist),

    # is_watched
    path('<int:movie_pk>/watched/', views.add_watched),

    # add_prefer
    path('<int:movie_pk>/prefer/', views.add_user_prefer),
]
