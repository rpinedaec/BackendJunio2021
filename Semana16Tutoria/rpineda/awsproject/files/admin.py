from django.contrib import admin
#from import_export import resources

from .models import Cliente
from .models import Book
# from import_export.admin import ImportExportModelAdmin

# class BookResource(resources.ModelResource):
#     class Meta:
#         model = Book
# # Register your models here.


# class BookAdmin(ImportExportModelAdmin):
#     resource_class = BookResource

# admin.site.register(Book, BookAdmin)
admin.site.register(Cliente)