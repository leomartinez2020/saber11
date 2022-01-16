import json
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core import serializers

from django.core.serializers.json import DjangoJSONEncoder
from saber11.models import Colegio #, Colegio2020

class ColegioListView(ListView):
    model = Colegio
    context_object_name = 'colegios'
    queryset = Colegio.objects.filter(periodo='2021').filter(promponderado__gt=68).exclude(evaluados__lt=5).order_by('-promponderado')
    template_name = 'saber11/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the objects
        #context['book_list'] = queryset
        context['year'] = '2021'
        return context


class ColegioDetailView(DetailView):
    model = Colegio
    template_name = 'saber11/detalle.html'

def colegio_detail_view(request, pk, slug):
    try:
        queryset = Colegio.objects.get(pk=pk)
        colegio = serializers.serialize("json", [queryset])
        #colegio = json.dumps(dict(queryset), cls=DjangoJSONEncoder)
    except Colegio.DoesNotExist:
        raise Http404('No hay tal colegio')

    return render(request, 'saber11/detalle.html', context={'colegio_json': colegio, 'colegio': queryset})
