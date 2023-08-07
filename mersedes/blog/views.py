from django.shortcuts import render, redirect
from .models import Post,Comment
from .forms import CommentsForm

def blog_index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentsForm()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comment(
                aythor = form.cleaned_data ['author'],
                body = form.cleaned_data ['body'],
                post = post
            )
            comment.save()
            return redirect('blog_detail',pk=post.pk)
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {'post': post, 'comments':comments, 'form':form}
    return render(request, 'blog_detail.html', context)

def blog_category(request, category):
    post = Post.objects.filter(categories__name__contains = category)
    context = {'category': category, 'posts': post}
    return render(request, 'blog_category.html', context)

def search_results(request):
    query = request.GET.get('query')
    results = Post.objects.filter(title__icontains=query)
    context = {'results': results}
    return render(request, 'search_results.html', context)