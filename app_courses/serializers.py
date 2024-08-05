from rest_framework import serializers
from .models import *

class NumpyMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumpyMCQModel
        fields = "__all__"

class PandasMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PandasMCQModel
        fields = "__all__"

class MatplotlibMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatplotlibMCQModel
        fields = "__all__"

class PythonMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonMCQModel
        fields = "__all__"

class CSSMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSMCQModel
        fields = "__all__"

class LinuxMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinuxMCQModel
        fields = "__all__"
