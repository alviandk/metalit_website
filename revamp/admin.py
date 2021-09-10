from django.contrib import admin
from .models import Contact, Pelatihan, QA, TermConditions, PrivacyPolicy

admin.site.register(Contact)
admin.site.register(Pelatihan)
admin.site.register(QA)
admin.site.register(TermConditions)
admin.site.register(PrivacyPolicy)