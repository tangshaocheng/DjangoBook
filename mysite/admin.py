from django.contrib import admin
from mysite import models
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    date_hierarchy = 'publication_date'
    ordering = ('publication_date', )
    filter_horizontal = ('authors', )
    raw_id_fields = ('publisher', )

admin.site.register(models.Publisher)
admin.site.register(models.Content)
admin.site.register(models.Center)
admin.site.register(models.RContent)
admin.site.register(models.JoinMe)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.User)
admin.site.register(models.Activities)