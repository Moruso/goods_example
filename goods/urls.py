from django.urls import path, include
from goods import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('goods', views.GoodsViewSet)

urlpatterns = [path('', include(router.urls)) ]
