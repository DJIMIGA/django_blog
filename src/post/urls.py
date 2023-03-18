from django.urls import path
from post.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = 'post'

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('Create/', BlogPostCreate.as_view(), name="create"),
    path('Edit/<int:pk>', BlogPostUpdate.as_view(), name="edit"),
    path('Detail/<int:pk>', BlogPostDetail.as_view(), name="Detail"),
    path('Delete/<int:pk>', BlogPostDelete.as_view(), name="delete")
]
