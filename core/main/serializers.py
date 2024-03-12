from rest_framework import serializers
from .models import Category, Product, Color, Brand, Slider


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name', )

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('name', )

class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)


    class Meta:
        model = Product
        fields = ('id', 'brand', 'productName', 'img', 'img1', 'img2', 'img3', 'price', 'discount', 'colors')

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'products')


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ('image',)