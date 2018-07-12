from django.contrib import admin
from .models import User, Group, Game, GameType, Console


admin.site.register(User)
admin.site.register(Group)
admin.site.register(Game)
admin.site.register(GameType)
admin.site.register(Console)
