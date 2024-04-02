from rest_framework import serializers,exceptions
from .models import Product


class CommentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50, min_length=3)
    email=serializers.EmailField()
    message=serializers.CharField()

    def validate(self, attrs):
        name=attrs.get('name')
        if name == "John":
            raise exceptions.NotAcceptable(detail="Sorry this name is not allowed")
        
        return attrs
    
    def create(self, validated_data):
        return validated_data
    
    def update(self,instance,validated_data):
        return None
    

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id", "name", "description","category", "supply_price","selling_price", "supply_date", "stock_amt", "thumbnail","brand"]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id", "name", "description","category","selling_price", "stock_amt", "thumbnail","brand"]