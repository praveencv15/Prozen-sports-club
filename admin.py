from django.contrib import admin

from .models import Member_details,Sports_details,Store,TournamentRegistration

admin.site.register(Member_details)
admin.site.register(Sports_details)
admin.site.register(Store)
admin.site.register(TournamentRegistration)