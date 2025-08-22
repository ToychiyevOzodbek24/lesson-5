from django.urls import path

from apps.pages.views import home_page_view, blog_page_view

app_name = 'pages'

urlpatterns = [
    path('blog/', blog_detail_view, name='blog-detail'),
    path('', about_view, name='about'),
    path('blog-list/', blog_list_view, name='blog-lists'),
    path('cart/', cart_view, name='carts'),
    path('category/', category_view, name='categorys'),
    path('checkout/', checkout_view, name='checkouts'),
    path('contact/', contact_view, name='contacts'),
    path('dashboard/', dashboard_view, name='dashboards'),
    path('faq/', faq_view, name='faqs'),
    path('login/', login_view, name='logins'),
    path('product_detail/', product_detail_view, name='products'),
    path('wishlist/', cart_view, name='wishlists'),
]

