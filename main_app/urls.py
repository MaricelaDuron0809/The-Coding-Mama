from django.urls import path
from . import views

urlpatterns = [

    path('', views.LandingPage.as_view(), name="landing"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('posts/<int:post_pk>/comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name="comment_delete"),
    path('profile/<int:pk>/', views.Profile.as_view(), name="profile"),



 ]