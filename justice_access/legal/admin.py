from django.contrib import admin
from .models import LegalAid, LegalTopic, LegalAidRequest

# model for Legal Aid
admin.site.register(LegalAid)

@admin.register(LegalTopic)
class LegalTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

admin.site.register(LegalAidRequest)