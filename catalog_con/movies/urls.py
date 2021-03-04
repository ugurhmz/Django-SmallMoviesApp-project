from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='movies'),
    path('<int:movie_id>', views.movies_detail, name = 'detail'),
    path('search', views.search, name='search'),
]