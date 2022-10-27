from django.shortcuts import render
from .models import Memory

def index(request) :
    posts = Memory.objects.all().order_by('-pk')
    return render(
        request,
        'diary/index.html',
        {
            'posts' : posts,
        }
    )

def memory_detail  (request, pk):
    post = Memory.objects.get(pk=pk)
    
    return render(
        request,
        'diary/memory_detail.html',
        {
            'post':post,
        }
    )   

