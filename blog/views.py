from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    all_products = Blog.objects.all()[:3]
    return render(request, "blogs/blogs1.html", {'blogs': all_products })

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blogs/details1.html', {'blog': blog})