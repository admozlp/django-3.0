from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect,redirect
from .models import Post
from .form import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    post_list = Post.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(Q(title__icontains=query)|
                                     Q(content__icontains=query))
    context = {
        'posts': post_list
    }
    return render(request, 'post/index.html', context)


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html', context)


@login_required(login_url='/')
def create_view(request, messges=None):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        messages.success(request,"Yazı Başarıyla kayıt edildi.")
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/create.html', context)


@login_required(login_url='/')
def delete_view(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    messages.success(request,"Yazı Başarıyla Silindi.",extra_tags="danger")
    return redirect('/')

login_required(login_url='/')
def update_view(request,id):
    post = get_object_or_404(Post,id = id)
    form = PostForm(request.POST or None,request.FILES or None, instance = post)
    if form.is_valid():
        post.save()
        messages.success(request,"Yazı başarıyla güncellendi",extra_tags="success")
        return HttpResponseRedirect(post.get_absolute_url())
    context ={
        'form':form
    }
    return render(request,'post/create.html',context)
