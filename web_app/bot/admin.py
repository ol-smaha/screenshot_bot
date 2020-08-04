from django.urls import path
from django.contrib import admin
from .bot import run_bot, run_debug_bot
from .models import Bot


class BotAdmin(admin.ModelAdmin):
    change_list_template = "bot_page.html"
    list_display = ('name',)

    def get_urls(self):
        urls = super(BotAdmin, self).get_urls()
        custom_urls = [path('run_bot/', run_bot, name='run_bot')]
        custom_urls += [path('run_debug_bot/', run_debug_bot, name='run_debug_bot')]
        return custom_urls + urls


admin.site.register(Bot, BotAdmin)
