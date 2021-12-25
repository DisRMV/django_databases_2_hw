from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.prefetch_related('scopes')
    relationship = Relationship.objects.select_related('scope', 'article')

    context = {'object_list': object_list, 'data': relationship}

    return render(request, template, context)
