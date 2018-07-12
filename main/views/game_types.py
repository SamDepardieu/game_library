from main.models import GameType
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class GameTypeListView(generic.ListView):
    template_name = 'main/game_type/list.html'
    model = GameType


class GameTypeShowView(generic.DetailView):
    template_name = 'main/game_type/show.html'
    model = GameType


class GameTypeAddView(CreateView):
    template_name = 'main/game_type/add.html'
    model = GameType
    fields = ['name']
    success_url = '/gametype'


class GameTypeUpdateView(UpdateView):
    template_name = 'main/game_type/add.html'
    model = GameType
    fields = ['name']
    success_url = '/gametype'


class GameTypeDeleteView(DeleteView):
    template_name = 'main/game_type/delete.html'
    model = GameType
    success_url = '/gametype'
