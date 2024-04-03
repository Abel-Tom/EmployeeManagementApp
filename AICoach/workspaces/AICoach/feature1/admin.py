from django.contrib import admin

from .models import Entry
from .models import BotMessage

admin.site.register(Entry)
admin.site.register(BotMessage)

