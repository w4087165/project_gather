from django.contrib import admin
from .models import Note

# Register your models here.
class NoteManager(admin.ModelAdmin):
    list_display = ['id','title','user','create_time']

admin.site.register(Note,NoteManager)