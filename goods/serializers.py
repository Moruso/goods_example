from .models import Goods
from rest_framework import serializers


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}
                        }
