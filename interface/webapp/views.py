from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CommentSerializer
from rest_framework.response import Response
from .serializers import ProductCreateSerializer,ProductSerializer
from .models import Product
from rest_framework import status,exceptions,generics,permissions
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    operation_description="Retrieve a list of all users.",
    responses={200: 'Success'},
)
# Create your views here.

# class TestEndPoint(APIView):
#     def get(self,request, *args, **kwargs):
#         return Response({"message": "Yoo!! It's working"},status=200)

#     def post(self,request, *args, **kwargs):
#         incoming_data=request.data
#         comment=CommentSerializer(data=incoming_data)
#         if comment.is_valid(raise_exception=True):
#             comment.save()
#             return Response (data=comment.data, status=200)
#         return Response(comment.errors, status=400)
    
#Generics view classes
class NewProductEndPoint(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductCreateSerializer
    queryset=Product.objects.all()

    def get_queryset(self):
        qs=super().get_queryset()
        value=self.request.query_params.get('brand')
        cat=self.request.query_params.get('category')
        if value is not None or cat is not None:
            qs=qs.filter(Q(brand=value) | Q(category=cat))
        return qs
    
    

class ProductEndPoint(APIView):
    def get(self,request, *args, **kwargs):   #retrieve a record
        all_product=Product.objects.all()
        products=ProductSerializer(all_product, many=True)
        return Response(products.data, status=200)

    def post(self,request,args,*kwargs):     #Adding new record
        incoming_data=request.data
        serializer=ProductCreateSerializer(data=incoming_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()             # This will trigger the update the create method or update method from the default
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SingleProductEndPoint(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ProductCreateSerializer
    query_set=Product.objects.all()
    lookup_field='pk' 

   
    
    
      
class ProductDetailPoint(APIView):
    def get_object(self,pk):
        try:
            product=Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise exceptions.NotFound(detail="Product with this id does not exist")
        return product
    

def get(self, request, *args, **kwargs):
        product=self.get_object(kwargs.get("pk"))
        serializer=ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def put(self,request,*args, **kwargs):
        product=self.get_object(kwargs.get('pk'))
        serializer=ProductCreateSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def delete(self,request,args,*kwargs):
        product=self.get_object(kwargs.get("pk"))
        product.delete()
        return Response({'message':"Product deleted successfully"},status=status.HTTP_204_NO_CONTENT)