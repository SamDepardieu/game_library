from main.models import Game
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class GameListView(generic.ListView):
    template_name = 'main/game/list.html'
    model = Game


class GameShowView(generic.DetailView):
    template_name = 'main/game/show.html'
    model = Game


class GameAddView(CreateView):
    template_name = 'main/game/add.html'
    model = Game
    fields = ['name', 'type', 'console']
    success_url = '/game'


class GameUpdateView(UpdateView):
    template_name = 'main/game/add.html'
    model = Game
    fields = ['name', 'type', 'console']
    success_url = '/game'


class GameDeleteView(DeleteView):
    template_name = 'main/game/delete.html'
    model = Game
    success_url = '/game'
