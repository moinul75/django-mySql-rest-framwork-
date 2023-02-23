from rest_framework import serializers
from .models import Product




#create the serializers class 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        