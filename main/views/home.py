from main.models import Game
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'main/index.html'

    def get_queryset(self):
        return Game.objects.all()[:5]
