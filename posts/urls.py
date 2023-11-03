from django.urls import path, include
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', PostListView.as_view(), name='post page'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]

