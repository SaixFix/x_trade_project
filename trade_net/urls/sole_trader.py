from django.urls import path

from trade_net.views.sole_trader import SoleTraderCreateView, SoleTraderListView, SoleTraderRetrieveView

urlpatterns = [
    path('create/', SoleTraderCreateView.as_view(), name='factory_create'),
    path('list/', SoleTraderListView.as_view(), name='factory_list'),
    path('<int:pk>/', SoleTraderRetrieveView.as_view(), name='factory_RUD'),
]