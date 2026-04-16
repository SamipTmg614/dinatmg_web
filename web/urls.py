
from django.urls import path
from .views import userlst, blog_list, blog_detail
urlpatterns = [
    path('', userlst.as_view(), name='index'),
    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
]
