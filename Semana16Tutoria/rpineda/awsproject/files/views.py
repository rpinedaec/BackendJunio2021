from rest_framework import viewsets, parsers
from .models import Cliente
from .serializers import ClienteSerializer
class ClienteViewset(viewsets.ModelViewSet):
 
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']