from django.shortcuts import render
from .services import *


# Create your views here.


def start(updater, context):
    user = updater.message.from_user
    tg_user = get_user(user.id)
    log = get_log(user.id)
    if not tg_user:
        tg_user = create_user(user.id)

    if not log:
        log = create_log(user.id)

    updater.message.reply_text("Assalomu Alekum")


def message_handler(updater, context):
    pass


def recieved_photo(updater, context):
    pass
