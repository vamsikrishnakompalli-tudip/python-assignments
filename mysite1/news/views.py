from django.shortcuts import render

from news.models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {'month': month, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)