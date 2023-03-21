from django.urls import path
from post.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete
from django.contrib.auth.decorators import login_required
app_name = 'post'

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('Create/', login_required(BlogPostCreate.as_view()), name="create"),
    path('Edit/<str:slug>', BlogPostUpdate.as_view(), name="edit"),
    path('Detail/<str:slug>', BlogPostDetail.as_view(), name="detail"),
    path('Delete/<str:slug>', BlogPostDelete.as_view(), name="delete")
    ]
