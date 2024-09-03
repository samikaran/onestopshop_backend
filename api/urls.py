from django.urls import path
from accounts import views as accounts_views
from ecommerce import views as ecommerce_views
from customer import views as customer_views
from vendor import views as vendor_views

from rest_framework_simplejwt.views import TokenRefreshView

"""
    http post http://127.0.0.1:8000/api/user/token/ username=admin password=admin

    http http://127.0.0.1:8000/api/user/profile/ "Authorization: Bearer your_token_id"

    http http://127.0.0.1:8000/api/user/token/refresh referesh=your_token_id"
"""

urlpatterns = [
    path('', accounts_views.getRoutes),

    # Userauths API Endpoints
    path('user/token/', accounts_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', accounts_views.RegisterView.as_view(),
         name='auth_register'),
    path('user/profile/<user_id>/',
         accounts_views.ProfileView.as_view(), name='user_profile'),
    path('user/test/', accounts_views.testEndPoint, name='auth_register'),
    path('user/password-reset/<email>/',
         accounts_views.PasswordEmailVerify.as_view(), name='password_reset'),
    path('user/password-change/',
         accounts_views.PasswordChangeView.as_view(), name='password_change'),

    # Adoon Endpoint
    #     path('addon/', ecommerce_views.ConfigSettingsDetailView.as_view(), name='addon'),

    # Store API Endpoints
    path('category/', ecommerce_views.CategoryListView.as_view(), name='category'),
    path('products/', ecommerce_views.ProductListView.as_view(), name='products'),
    path('products/<slug:slug>/<int:id>/',
         ecommerce_views.ProductDetailView.as_view(), name='product'),
    #     path('brand/', ecommerce_views.BrandListView.as_view(), name='brand'),
    #     path('featured-products/', ecommerce_views.FeaturedProductListView.as_view(), name='featured-products'),
    path('cart-view/', ecommerce_views.CartApiView.as_view(), name='cart-view'),
    path('cart-list/<str:cart_id>/',
         ecommerce_views.CartListView.as_view(), name='cart-list'),
    path('cart-list/<str:cart_id>/<int:user_id>/',
         ecommerce_views.CartListView.as_view(), name='cart-list-with-user'),
    path('cart-detail/<str:cart_id>/',
         ecommerce_views.CartDetailView.as_view(), name='cart-detail'),
    path('cart-detail/<str:cart_id>/<int:user_id>/',
         ecommerce_views.CartDetailView.as_view(), name='cart-detail'),
    path('cart-delete/<str:cart_id>/<int:item_id>/',
         ecommerce_views.CartItemDeleteView.as_view(), name='cart-delete'),
    path('cart-delete/<str:cart_id>/<int:item_id>/<int:user_id>/',
         ecommerce_views.CartItemDeleteView.as_view(), name='cart-delete'),
    path('create-order/', ecommerce_views.CreateOrderView.as_view(),
         name='create-order'),
    path('checkout/<order_oid>/',
         ecommerce_views.CheckoutView.as_view(), name='checkout'),
    path('coupon/', ecommerce_views.CouponApiView.as_view(), name='coupon'),
    path('create-review/', ecommerce_views.ReviewRatingAPIView.as_view(),
         name='create-review'),
    path('reviews/<product_id>/',
         ecommerce_views.ReviewListView.as_view(), name='create-review'),
    path('search/', ecommerce_views.SearchProductsAPIView.as_view(), name='search'),

    # Payment
    path('stripe-checkout/<order_oid>/',
         ecommerce_views.StripeCheckoutView.as_view(), name='stripe-checkout'),
    path('payment-success/', ecommerce_views.PaymentSuccessView.as_view(),
         name='payment-success'),

    # Customer API Endpoints
    path('customer/orders/<user_id>/',
         customer_views.OrdersAPIView.as_view(), name='customer-orders'),
    path('customer/order/detail/<user_id>/<order_oid>/',
         customer_views.OrdersDetailAPIView.as_view(), name='customer-order-detail'),
    path('customer/wishlist/create/', customer_views.WishlistCreateAPIView.as_view(),
         name='customer-wishlist-create'),
    path('customer/wishlist/<user_id>/',
         customer_views.WishlistAPIView.as_view(), name='customer-wishlist'),
    path('customer/notification/<user_id>/',
         customer_views.CustomerNotificationView.as_view(), name='customer-notification'),
    path('customer/notification/<user_id>/<noti_id>/',
         customer_views.MarkCustomerNotificationAsSeen.as_view(), name='mark-customer-notification'),
    path('customer/setting/<int:pk>/',
         customer_views.CustomerUpdateView.as_view(), name='customer-settings'),

    # Vendor API Endpoints
    path('vendor/stats/<vendor_id>/', vendor_views.DashboardStatsAPIView.as_view(), name='vendor-stats'),
    path('vendor-orders-report-chart/<vendor_id>/', vendor_views.MonthlyOrderChartAPIFBV, name='vendor-orders-report-chart'),
    path('vendor-products-report-chart/<vendor_id>/', vendor_views.MonthlyProductsChartAPIFBV, name='vendor-product-report-chart'),
    path('vendor/products/<vendor_id>/', vendor_views.ProductsAPIView.as_view(), name='vendor-prdoucts'),
    path('vendor/orders/<vendor_id>/', vendor_views.OrdersAPIView.as_view(), name='vendor-orders'),
    path('vendor/orders/<vendor_id>/<order_oid>/', vendor_views.OrderDetailAPIView.as_view(), name='vendor-order-detail'),
    path('vendor/orders/filter/<vendor_id>', vendor_views.FilterOrderAPIView.as_view(), name='vendor-order-detail'),
    path('vendor-product-filter/<vendor_id>', vendor_views.FilterProductsAPIView.as_view(), name='vendor-product-filter'),
    path('vendor-earning/<vendor_id>/', vendor_views.Earning.as_view(), name='vendor-product-filter'),
    path('vendor-monthly-earning/<vendor_id>/', vendor_views.MonthlyEarningTracker, name='vendor-product-filter'),
    path('vendor-reviews/<vendor_id>/', vendor_views.ReviewsListAPIView.as_view(), name='vendor-reviews'),
    path('vendor-reviews/<vendor_id>/<review_id>/', vendor_views.ReviewsDetailAPIView.as_view(), name='vendor-review-detail'),
    path('vendor-coupon-list/<vendor_id>/', vendor_views.CouponListAPIView.as_view(), name='vendor-coupon-list'),
    path('vendor-coupon-stats/<vendor_id>/', vendor_views.CouponStats.as_view(), name='vendor-coupon-stats'),
    path('vendor-coupon-detail/<vendor_id>/<coupon_id>/', vendor_views.CouponDetailAPIView.as_view(), name='vendor-coupon-detail'),
    path('vendor-coupon-create/<vendor_id>/', vendor_views.CouponCreateAPIView.as_view(), name='vendor-coupon-create'),
    path('vendor-notifications-unseen/<vendor_id>/', vendor_views.NotificationUnSeenListAPIView.as_view(), name='vendor-notifications-list'),
    path('vendor-notifications-seen/<vendor_id>/', vendor_views.NotificationSeenListAPIView.as_view(), name='vendor-notifications-list'),
    path('vendor-notifications-summary/<vendor_id>/', vendor_views.NotificationSummaryAPIView.as_view(), name='vendor-notifications-summary'),
    path('vendor-notifications-mark-as-seen/<vendor_id>/<noti_id>/', vendor_views.NotificationMarkAsSeen.as_view(), name='vendor-notifications-mark-as-seen'),
    path('vendor-settings/<int:pk>/', vendor_views.VendorProfileUpdateView.as_view(), name='vendor-settings'),
    path('vendor-shop-settings/<int:pk>/', vendor_views.ShopUpdateView.as_view(), name='customer-settings'),
    path('shop/<vendor_slug>/', vendor_views.ShopAPIView.as_view(), name='shop'),
    path('vendor-products/<vendor_slug>/', vendor_views.ShopProductsAPIView.as_view(), name='vendor-products'),
    path('vendor-product-create/<vendor_id>/', vendor_views.ProductCreateView.as_view(), name='vendor-product-create'),
    path('vendor-product-edit/<vendor_id>/<product_pid>/', vendor_views.ProductUpdateAPIView.as_view(), name='vendor-product-edit'),
    path('vendor-product-delete/<vendor_id>/<product_pid>/', vendor_views.ProductDeleteAPIView.as_view(), name='vendor-product-delete'),
    path('vendor-register/', vendor_views.VendorRegister.as_view(), name='vendor-register'),
    
    # Tracking Feature
]
