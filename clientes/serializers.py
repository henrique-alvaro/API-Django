from rest_framework import serializers
from .models import Cliente
from .validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua numeros no campo nome'})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 digitos'})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O numero de celular deve esse modelo: 00 00000-0000, respeitando os espaços e traços'})

        return data