from django.core.management import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tg.views import *
from mebel_site.settings import TOKEN_KEY


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(TOKEN_KEY)
        updater.dispatcher.add_handler(CommandHandler("start", start)),
        updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler)),
        updater.dispatcher.add_handler(MessageHandler(Filters.photo, recieved_photo)),

        updater.start_polling()
        updater.idle()