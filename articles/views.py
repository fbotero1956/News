from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body', )
    # success_url = reverse_lazy('article_list')
    # success_url = reverse_lazy('article_detail', args=[int(self.id)])
   

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'author', 'body', )
    success_url = reverse_lazy('article_list')

class ArticleAboutView(ListView):
    model = Article
    template_name = "about.html"