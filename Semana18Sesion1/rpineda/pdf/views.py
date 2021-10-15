from django.http import HttpResponse
from django.views.generic import View
import datetime
from .models import costumer

from django.template.loader import get_template

from .utils import render_to_pdf #created in step 4

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": datetime.date.today(),
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class GenerateTabla(View):
    def get(self, request, *args, **kwargs):
        template = get_template('tabla.html')
        data = costumer.objects.all()[:10]

        context = {
            "data": data,
            "conteo": data.count()
        }
        html = template.render(context)
        pdf = render_to_pdf('tabla.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf', charset='utf-8')
            filename = "Tabla_%s.pdf" %("987987987")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")