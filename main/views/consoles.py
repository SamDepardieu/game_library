from main.models import Console
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class ConsoleListView(generic.ListView):
    template_name = 'main/console/list.html'
    model = Console


class ConsoleShowView(generic.DetailView):
    template_name = 'main/console/show.html'
    model = Console


class ConsoleAddView(CreateView):
    template_name = 'main/console/add.html'
    model = Console
    fields = ['name']
    success_url = '/console'


class ConsoleUpdateView(UpdateView):
    template_name = 'main/console/add.html'
    model = Console
    fields = ['name']
    success_url = '/console'


class ConsoleDeleteView(DeleteView):
    template_name = 'main/console/delete.html'
    model = Console
    success_url = '/console'
