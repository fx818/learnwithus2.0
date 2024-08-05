from rest_framework import serializers
from .models import *

class NumpyMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyMCQModel
        fields = "__all__"

class PandasMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyMCQModel
        fields = "__all__"

class MatplotlibMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyMCQModel
        fields = "__all__"
