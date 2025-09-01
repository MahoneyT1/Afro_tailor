from django.urls import path, include
from .views import ProductCreateView, ProductListUpdateDeleteView


urlpatterns = [
    path("product/", ProductCreateView.as_view(), name="create-product"),
    path("product/<int:pk>/", ProductListUpdateDeleteView.as_view(), name="product-detail"),
    path("product/<int:pk>/update/", ProductListUpdateDeleteView.as_view(), name="update-product"),
    path("product/<int:pk>/delete/", ProductListUpdateDeleteView.as_view(), name="delete-product"),
    path("product/list/", ProductListUpdateDeleteView.as_view(), name="list-products"),
]