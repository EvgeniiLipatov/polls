from django.contrib import admin

from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created_at']
    list_filter = ['question']
    list_display_links = ['pk']
    search_fields = ['question']
    readonly_fields = ['created_at']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'varText', 'poll']
    list_filter = ['varText']
    list_display_links = ['pk']
    search_fields = ['varText']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer)

# Register your models here.
