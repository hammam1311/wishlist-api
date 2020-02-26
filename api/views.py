from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,  RetrieveAPIView
from items.models import Item, FavoriteItem
from .serializers import RegisterSerializer ,ItemListSerializer,ItemDetailSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.filters import OrderingFilter,SearchFilter
from .permissions import IsOwner



class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']



class Register(CreateAPIView):
	serializer_class = RegisterSerializer


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
