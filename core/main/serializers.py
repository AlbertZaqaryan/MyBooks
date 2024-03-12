from rest_framework import serializers
from .models import Category, Product, Color, Brand, Slider
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp
from allauth.socialaccount.providers.google.provider import GoogleProvider
from requests.exceptions import HTTPError
from django.contrib.auth import get_user_model

User = get_user_model()

class GoogleTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('token')

        try:
            app = SocialApp.objects.get(provider=GoogleProvider.id)
            token = SocialToken(token=token, app=app)
            login = SocialLogin(token=token, user=User())
            login.token = token
            complete_social_login(self.context['request'], login)
        except HTTPError as e:
            raise serializers.ValidationError(str(e))

        if not login.is_existing:
            user = login.user
            user.set_unusable_password()
            user.save()
            login.save(request=self.context['request'])
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Error with Google authentication')

        return super().validate(attrs)


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