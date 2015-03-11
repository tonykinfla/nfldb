from django.contrib import admin

# Register your models here.
from app.models import AuthGroup
from app.models import NflTeam
from app.models import Players
from app.models import PlayerSeason
from app.models import Season
from app.models import User
from app.models import UserRoster

class NflTeamAdmin(admin.ModelAdmin):
    exclude = ('id',)
    list_display = ('team_name',)
admin.site.register(NflTeam, NflTeamAdmin)
 
class PlayersAdmin(admin.ModelAdmin):
    exclude = ('player_id',)
    list_display = ('name',)
admin.site.register(Players, PlayersAdmin)

class SeasonAdmin(admin.ModelAdmin):
    exclude = ('season_id',)
    list_display = ('season',)
admin.site.register(Season, SeasonAdmin)

class UserAdmin(admin.ModelAdmin):
    exclude = ('user_id',)
    list_display = ('user',)
admin.site.register(User, UserAdmin)

class UserRosterAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'players_id')
admin.site.register(UserRoster, UserRosterAdmin)

class PlayerSeasonAdmin(admin.ModelAdmin):
	list_display = ('players_id', 'season_id', )
admin.site.register(PlayerSeason, PlayerSeasonAdmin)




