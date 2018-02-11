from django.contrib import admin
from .models import *

class IndexValueAdmin(admin.ModelAdmin):
	date_hierarchy = 'date'
	list_display = ('date', 'value')
	list_filter = ('date',)
	search_fields = ['date']

# Register your models here.
admin.site.register(index_value, IndexValueAdmin)
admin.site.register(prediction_value, IndexValueAdmin)


