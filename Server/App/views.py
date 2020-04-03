from django.shortcuts import render
from django.views.generic import CreateView

from App.models import Article


def index(request):
    ctx = {
        "articles":Article.objects.all(),
    }
    return render(request, "index.html", context=ctx)


class ArticleCreate(CreateView):
    success_url = "/"
    template_name = "article.html"
    model = Article
    fields = ['author', 'text']