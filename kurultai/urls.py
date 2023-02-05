from django.urls import path
from kurultai import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('createrubrics/', views.createrubrics, name='createrubrics'),
    path('deleterubrics/<int:pk>/', views.deleterubrics, name='deleterubrics'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_list/<int:pk>/', views.post_list, name='post_list'),
    path('updatecomment/<int:pk>/', views.updatecomment, name='updatecomment'),
    path('commentlist/', views.commentlist, name='commentlist'),
    path("password_reset/", views.password_reset_request, name="password_reset")
]

