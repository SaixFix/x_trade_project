from rest_framework.generics import CreateAPIView, ListAPIView

from trade_net.models.factory import Factory
from trade_net.serializers.factory import FactoryCreateSerializer, FactoryListSerializer


class FactoryCreateView(CreateAPIView):
    model = Factory
    serializer_class = FactoryCreateSerializer
    queryset = Factory.objects.all()



class FactoryListView(ListAPIView):
    model = Factory
    serializer_class = FactoryListSerializer
    queryset = Factory.objects.all()