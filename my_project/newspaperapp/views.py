from django.shortcuts import render
from .models import News, Category
from datetime import datetime, timedelta
from django.views.generic import ListView
def home(request):
    three_categories=Category.objects.all()
    return render(request,'newspaperapp/home.html',{
        'three_categories':three_categories
    })
class SearchView(ListView):
    model = News
    template_name = 'newspaperapp/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        # query is of type 'str', convert to datetime
        start_day = datetime.fromisoformat(query)
        end_day   = start_day + timedelta(days=1)
        if query:
             postresult = News.objects.filter(
                 date_published__gte=start_day,
                 date_published__lt=end_day
             )
             result = postresult
        else:
            result = None
        return result

def detail(request,id):
    news=News.objects.get(pk=id)
    return render(request,'newspaperapp/detail.html',{
        'news':news
    })

def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'newspaperapp/category.html',{
        'all_news':news,
        'category':category,
    })
