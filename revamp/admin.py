from django.contrib import admin
from .models import Contact, Pelatihan, QA, TermCondition, PrivacyPolicy

admin.site.register(Contact)
admin.site.register(Pelatihan)
admin.site.register(QA)
admin.site.register(TermCondition)
admin.site.register(PrivacyPolicy)