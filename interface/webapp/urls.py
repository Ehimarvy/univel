from django.urls import path
from.views import ProductEndPoint,ProductDetailPoint,NewProductEndPoint,SingleProductEndPoint
urlpatterns=[
    path('product',ProductEndPoint.as_view(), name="Product" ),
    path("product/<int:pk>", ProductDetailPoint.as_view(), name="details"),
    path('product-list', NewProductEndPoint.as_view(), name='new-product-list'),
    path('product-list/<int:pk>', SingleProductEndPoint.as_view(),name='single-product'),
]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    