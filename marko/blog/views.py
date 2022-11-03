from django.shortcuts import render
from .models import Post
def blog_detail(request,id):
    blog = Post.objects.get(pk=int(id))
    context = {'post':blog}
    return render(request,'blog_detail.html',context)