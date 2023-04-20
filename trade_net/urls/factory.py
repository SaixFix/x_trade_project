from django.urls import path

from trade_net.views.factory import FactoryCreateView, FactoryListView

urlpatterns = [
    path('create/', FactoryCreateView.as_view(), name='factory_create'),
    path('list/', FactoryListView.as_view(), name='factory_list'),
]