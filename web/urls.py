
from django.urls import path,include
from .views import userlst
urlpatterns = [
    path('',userlst.as_view(),name='index')
]
