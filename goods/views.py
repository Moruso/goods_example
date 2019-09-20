from rest_framework import viewsets, permissions
from goods import serializers
from goods.models import Goods


class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GoodsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Goods.objects.all()
