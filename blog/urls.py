from django.urls import path
from .views import BlogView
from .views import BlogCreateView
from .views import BlogDetailView
from .views import BlogUpdateView
from .views import BlogDeleteView

app_name = "blog"

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
]