from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from trade_net.models.sole_trader import SoleTrader
from trade_net.serializers.sole_trader import SoleTraderCreateSerializer, SoleTraderListSerializer, \
    SoleTraderUpdateSerializer


class SoleTraderCreateView(CreateAPIView):
    model = SoleTrader
    serializer_class = SoleTraderCreateSerializer
    queryset = SoleTrader.objects.all()
    permission_classes = [IsAuthenticated]


class SoleTraderListView(ListAPIView):
    model = SoleTrader
    serializer_class = SoleTraderListSerializer
    queryset = SoleTrader.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class SoleTraderRetrieveView(RetrieveUpdateDestroyAPIView):
    model = SoleTrader
    serializer_class = SoleTraderUpdateSerializer
    queryset = SoleTrader.objects.all()
    permission_classes = [IsAuthenticated]
