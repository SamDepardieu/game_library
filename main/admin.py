from django.contrib import admin
from .models import Game, GameType, Console


admin.site.register(Game)
admin.site.register(GameType)
admin.site.register(Console)
