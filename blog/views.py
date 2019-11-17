from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    Data = {'Post' : Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)
def article(request, id):
    article = get_object_or_404(Post, id = id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author = request.user, post = article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, 'blog/article.html', {'article' : article, 'form' : form})
