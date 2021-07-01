from rest_framework import serializers
from .models import Materia_Actual, Escuela, Usuario

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia_Actual
        fields = "__all__"

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = "__all__"

class Materia_ActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia_Actual
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
