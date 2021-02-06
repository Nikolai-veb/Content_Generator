from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .forms import AddArticlesForm
from .models import Categories, Under_Categories, Sites, Articles


class ListSitesView(ListView):
    """ List Sites"""
    model = Sites
    context_object_name = 'sites'
    template_name = 'generator/site_list.html'

    def get_queryset(self):
        print(self.kwargs)
        queryset = Sites.objects.all()
        kwargs = self.kwargs
        if kwargs:
            try:
                if kwargs['pk']:
                    category = get_object_or_404(Under_Categories, id=kwargs['pk'])
                    queryset = Sites.objects.filter(under_category=category)
            except KeyError:
                category = get_object_or_404 (Categories, slug=kwargs['slug_category'])
                queryset = Sites.objects.filter(category=category)
        print(queryset)
        return queryset


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categories'] = Categories.objects.all()
            return context


