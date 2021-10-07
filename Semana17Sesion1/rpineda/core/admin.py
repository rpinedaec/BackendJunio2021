from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.utils.formats import date_format
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import costumer
from django.urls import reverse
# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CostumerAdmin(admin.ModelAdmin):
    list_display = ('centro', 'tipo_almacen', 'cod_material', 'desc_material', 'unidad', 'saldo_actual', 'fecha')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"] 
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info) 

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            for x in csv_data:
                fields = x.split("|")
                created = costumer.objects.update_or_create(
                    centro = fields[0],
                    tipo_almacen = fields[1],
                    cod_material = fields[2],
                    desc_material = fields[3],
                    unidad = fields[4],
                    saldo_actual = fields[5]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
admin.site.register(costumer, CostumerAdmin)
