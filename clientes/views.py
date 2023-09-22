from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Cliente
from .serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ClientesViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    filterset_fields = ['ativo']


