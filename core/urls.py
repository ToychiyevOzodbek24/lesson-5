"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.pages import views


urlpatterns = [
    path('', views.about_view, name='about'),
    path('blog-detail/', views.blog_detail_view, name='blog_detail'),  # oddiy sahifa uchun
    path('blog-list/', views.blog_list_view, name='blog_lists'),
    path('cart/', views.cart_view, name='carts'),
    path('category/', views.category_view, name='categorys'),
    path('checkout/', views.checkout_view, name='checkouts'),
    path('contact/', views.contact_view, name='contacts'),
    path('dashboard/', views.dashboard_view, name='dashboards'),
    path('faq/', views.faq_view, name='faqs'),
    path('login/', views.login_view, name='logins'),
    path('product_detail/', views.product_detail_view, name='products'),
    path('wishlist/', views.cart_view, name='wishlists'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
