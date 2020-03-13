from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('view_prices/',views.view_prices, name='view_prices'),
    path('edit_prices/',views.edit_prices, name='edit_prices'),
    path('delete_cust_type/<int:no>', views.delete, name='delete'),
    path('add_customer/',views.add_customer, name='add_customer'),
    path('view_customers/',views.view_customers, name='view_customers'),
    path('add_advert/',views.add_advert,name='add_advert'),
    path('view_adverts',views.view_adverts,name='view_adverts'),
]