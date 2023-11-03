from django.urls import path
from .views import home, HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', PostListView.as_view(), name='home'),
]

