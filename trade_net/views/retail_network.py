from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from trade_net.models.retail_network import RetailNetwork
from trade_net.serializers.retail_network import RetailNetworkCreateSerializer, RetailNetworkListSerializer, \
    RetailNetworkUpdateSerializer


class RetailNetworkCreateView(CreateAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkCreateSerializer
    queryset = RetailNetwork.objects.all()


class RetailNetworkListView(ListAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkListSerializer
    queryset = RetailNetwork.objects.all()


class RetailNetworkRetrieveView(RetrieveUpdateDestroyAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkUpdateSerializer
    queryset = RetailNetwork.objects.all()
