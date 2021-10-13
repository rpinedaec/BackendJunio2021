from django.contrib import admin
from django.forms import fields
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import costumer
from django import forms

# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CostumerAdmin(admin.ModelAdmin):

    list_display = ('centro', 'perfil', 'descripcion', 'cod_usuario', 'dni', 'apellidos_nombres' )
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'No es un Acrhivo tipo CSV')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            for x in csv_data:
                fields = x.split("|")
                created = costumer.objects.update_or_create(
                    centro = fields[0],
                    perfil = fields[1],
                    descripcion = fields[2],
                    cod_usuario = fields[3],
                    dni = fields[4],
                    apellidos_nombres = fields[5],
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form":form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(costumer, CostumerAdmin)