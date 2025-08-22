from django.urls import path

from apps.pages.views import home_page_view, blog_page_view

app_name = 'pages'

urlpatterns = [
    path('blog/', blog_detail_view, name='blog-detail'),
    path('', about_view, name='about'),
]

