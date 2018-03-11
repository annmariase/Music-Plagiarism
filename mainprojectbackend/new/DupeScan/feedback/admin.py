from django.contrib import admin

# Register your models here.
from .models import feedback

class feedbackModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated", 'timestamp']
	list_display_links = ["updated"]
	list_editable = ["USERNAME"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title,'content"]
	class Meta:
		model= feedback

admin.site.register(feedback)