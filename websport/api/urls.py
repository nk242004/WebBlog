from django.urls import path

from api.views import *

urlpatterns = [
    path('sportsman/<int:pk>', SportsmanDetail.as_view()),
    path('sportsman/', SportsmanList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
]