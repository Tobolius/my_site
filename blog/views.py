from django.shortcuts import render
from django.utils import timezone
from .models import Post, Info, PostStatistic


def index(request):
    posts = Post.objects.all().order_by('-date_created')
    last_three_posts = Post.objects.all().order_by('-date_created')[:3]
    info = Info.objects.get(pk=1)
    popular = PostStatistic.objects.order_by('-views')[:1]

    context = {
        'all_posts': posts,
        'info': info,
        'three_posts': last_three_posts,
        'popular_post': popular
    }
    return render(request, 'blog/index.html', context)


def detail_post(request, pk):
    post = Post.objects.get(id=pk)
    obj, created = PostStatistic.objects.get_or_create(
        defaults={
            'article': post,
            'date': timezone.now()
        },
        date=timezone.now(), article=post
    )

    obj.views += 1
    obj.save(update_fields=['views'])

    last_three_posts = Post.objects.all().order_by('-date_created')[:3]
    info = Info.objects.get(pk=1)
    context = {
        'post': post,
        'three_posts': last_three_posts,
        'info': info,
    }
    return render(request, 'blog/generic.html', context)


def generic(request):
    return render(request, 'blog/generic.html')


def elements(request):
    return render(request, 'blog/elements.html')
