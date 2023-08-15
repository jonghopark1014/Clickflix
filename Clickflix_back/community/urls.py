from django.urls import path
from . import views

urlpatterns = [
    # Review
    path('review/list/', views.review_list),
    path('review/<int:movie_pk>/create/', views.review_create),
    path('review/<int:review_pk>/', views.review_detail),
    path('review/edit/<int:review_pk>/', views.review_detail_edit),
    path('review/<int:review_pk>/like/', views.review_like),

    # Comment
    path('<int:review_pk>/comment/', views.comment_list), 
    path('review/<int:review_pk>/comment/', views.comment_create),
    path('comment/<int:comment_pk>/edit/', views.comment_edit),
    path('comment/<int:comment_pk>/like/', views.comment_like),

    # famousline
    path('famousline/list/', views.famousline_list),
    path('famousline/<int:famousline_pk>/', views.famousline_info),
    path('famousline/<int:movie_pk>/create/', views.famousline_create),
    path('famousline/<int:famousline_pk>/edit/', views.famousline_edit),

    # Machine
    path('machine/list/', views.machine_comment_list),
    path('machine/<int:movie_pk>/create/', views.machine_comment_create),
    path('machine/<int:machinecomment_pk>/edit/', views.machine_comment_edit),
]
