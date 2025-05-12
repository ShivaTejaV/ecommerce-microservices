from rest_framework import serializers
from .models import Category,Product,ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # show full category details in GET
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=Category.objects.all(),
        write_only=True
    )  # let user provide just category ID in POST/PUT
    # images = ProductImageSerializer(many=True, read_only=True)  # list of product images

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']


