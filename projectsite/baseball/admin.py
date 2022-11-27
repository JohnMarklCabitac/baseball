from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play, Match


# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display =  ("description",)
    search_fields =  ("description",)

@admin.register(Person)
class PositionAdmin(admin.ModelAdmin):
    list_display =  ("lastname","firstname","email","height","weight")
    search_fields =  ("lastname","firstname","email","height","weight")

@admin.register(Club)
class PositionAdmin(admin.ModelAdmin):
    list_display =  ("name","coach","description","dorm_latitude","dorm_longitude","team_pic")
    search_fields =  ("name","coach","description","dorm_latitude","dorm_longitude","team_pic")

@admin.register(Play)
class PositionAdmin(admin.ModelAdmin):
    list_display =  ("player","team","string_no","isActive","pos")
    search_fields =  ("player","team","string_no","isActive","pos")

@admin.register(Match)
class PositionAdmin(admin.ModelAdmin):
    list_display =  ("team1","team2","score_t1","score_t2","winner","game_date")
    search_fields =  ("team1","team2","score_t1","score_t2","winner","game_date")

