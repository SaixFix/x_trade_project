from django.urls import path

from trade_net.views.retail_network import RetailNetworkCreateView, RetailNetworkListView, RetailNetworkRetrieveView

urlpatterns = [
    path('create/', RetailNetworkCreateView.as_view(), name='factory_create'),
    path('list/', RetailNetworkListView.as_view(), name='factory_list'),
    path('<int:pk>/', RetailNetworkRetrieveView.as_view(), name='factory_RUD'),
]