from rest_framework import viewsets
from .models import Category, Product, Color, Brand, Slider
from .serializers import CategorySerializer, ProductSerializer, ColorSerializer, BrandSerializer, SliderSerializer
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import GoogleTokenSerializer

class GoogleLogin(views.APIView):
    serializer_class = GoogleTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Можете добавить создание токена JWT или чего-то ещё здесь, если требуется
            return Response({'success': 'User authenticated'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer