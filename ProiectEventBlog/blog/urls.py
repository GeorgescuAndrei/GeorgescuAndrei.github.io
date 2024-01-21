from django.urls import path
from . import views
from .views import blog_index
urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
     path('', blog_index, name='home'),
]



