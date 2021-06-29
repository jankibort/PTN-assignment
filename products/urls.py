from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='allProducts'),
    path('new', views.new, name='newProducts')
]