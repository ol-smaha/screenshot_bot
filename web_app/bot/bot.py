import json
from threading import Thread

import telebot
from telebot import types
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .utils import screen_by_url


bot = telebot.TeleBot(settings.BOT_TOKEN)


# Telegram webhook handler
@method_decorator(csrf_exempt)
def web_hook(request):
    try:
        json_message = json.loads(request.body)
        update = telebot.types.Update.de_json(json_message)
        bot.process_new_updates([update])
    except json.decoder.JSONDecodeError as err:
        return HttpResponse(str(err))
    return HttpResponse('OK')


# MESSAGES HANDLERS
@bot.message_handler(commands=['start'])
def start_message(message):
    send = bot.send_message(message.chat.id, 
                            'Hi! Send me url.')
    bot.register_next_step_handler(send, screen_by_url, bot=bot)


# Run bot from django-admin
def run_bot(request):
    try:
        bot.remove_webhook()
        bot.set_webhook(url=settings.WEBHOOK_URL,
                        certificate=open('ssl/bot_ssl_cert.crt', 'r'))
        messages.add_message(request, messages.INFO, 'Bot ready!')
    except Exception as e:
        messages.add_message(request, messages.INFO, f'Bot failed.\n Error: {e}')
    return redirect(reverse('admin:index'))

def run_debug_bot(request):
    try:
        thread = Thread(target=bot.polling, kwargs={'none_stop': True})
        thread.start()
        messages.add_message(request, messages.INFO, 'Debug-Bot ready!')
    except Exception as e:
        messages.add_message(request, messages.INFO, f'Debug-Bot failed.\n Error: {e}')
    return redirect(reverse('admin:index'))
    
# Webhook conf
bot.enable_save_next_step_handlers(delay=4)
bot.load_next_step_handlers()
