from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .forms import AddSitesForm
from .models import Categories, Under_Categories, Sites, Articles
from django.db.models import Max, Min, Q

class ListSitesView(ListView):
    """ List Sites"""
    model = Sites
    context_object_name = 'sites'
    template_name = 'generator/site_list.html'

    def get_queryset(self):
        print(self.kwargs)
        queryset = Sites.objects.all()
        if self.kwargs['slug_category']:
                category = get_object_or_404 (Categories, slug=self.kwargs['slug_category'])
                queryset = Sites.objects.filter(category=category)
        elif self.kwargs['pk']:
                category = get_object_or_404(Under_Categories, id=self.kwargs['pk'])
                queryset = Sites.objects.filter(under_category=category)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categories'] = Categories.objects.all()
            return context





class AddSitesView(DetailView):
    """Resizing Image Form"""
    model = Sites
    context_object_name = "sites"
    slug_field = "slug"
    template_name = "generator/add_sites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddSitesForm()
        return context
