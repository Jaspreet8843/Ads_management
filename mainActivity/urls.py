from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('view_prices/',views.view_prices, name='view_prices'),
    path('edit_prices/',views.edit_prices, name='edit_prices'),
]