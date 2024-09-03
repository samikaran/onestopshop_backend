from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('products', views.ProductViewSet)
# router.register('orders', views.OrderViewSet)
router.register('productreview', views.ReviewViewSet)


urlpatterns = [
    # Product Category
    path('categories/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),

    # Order
    path('orders/', views.OrderList.as_view()),
    path('order/<int:pk>', views.OrderDetail.as_view()),
]

urlpatterns += router.urls
