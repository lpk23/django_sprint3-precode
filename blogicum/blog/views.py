from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.http import Http404
from django.utils import timezone


def index(request):
    current_time = timezone.now()
    post_list = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    current_time = timezone.now()

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    )

    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_list})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    current_time = timezone.now()
    if post.pub_date > current_time or not \
            post.is_published or not \
            post.category.is_published:
        raise Http404("Страница не найдена")

    return render(request,
                  'blog/detail.html', {'post': post})
