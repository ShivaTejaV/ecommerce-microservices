from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
# from .pagination import SmallPagePagination,MediumPagePagination,LargePagePagination
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    # pagination_class = SmallPagePagination

    def get_queryset(self):
        products = Product.objects.all().select_related('category')
        request = self.request

        name = request.GET.get('name')
        description = request.GET.get('description')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')

        if name:
            products = products.filter(name__icontains=name)
        if description:
            products = products.filter(description__icontains=description)
        if price_min:
            products = products.filter(price__gte=price_min)
        if price_max:
            products = products.filter(price__lte=price_max)

        return products

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

