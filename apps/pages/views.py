from django.shortcuts import render


def about_view(request):
    return render(request, 'about.html')


def blog_detail_view(request):
    return render(request, 'blog-detail.html')