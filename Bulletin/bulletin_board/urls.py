from django.urls import path
from .views import PostList, PostCreate, PostSingle, PostEdit, PostDelete, PostFeedback

urlpatterns = [
    path('', PostList.as_view(), name='main'),
    path('<int:pk>/', PostSingle.as_view(), name='post_single'),
    path('<int:pk>/feedback', PostFeedback.as_view(), name='add_fb'),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    ]
