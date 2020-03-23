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
    path('billing',views.billing,name='billing'),
    path('store_bills/<str:cust_id>',views.store_bills,name='store_bills'),
    path('view_schedule',views.view_schedule, name='view_schedule'),
    path('pending_for_approval',views.pending_for_approval, name='pending_for_approval'),
    path('accept/<int:no>',views.accept, name='accept'),
    path('reject/<int:no>',views.reject, name='reject'),
    path('view_rejected',views.view_rejected, name='view_rejected'),
]