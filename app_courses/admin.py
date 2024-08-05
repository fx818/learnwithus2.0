from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(NumpyMCQModel)
admin.site.register(PandasMCQModel)
admin.site.register(MatplotlibMCQModel)
admin.site.register(PythonMCQModel)
admin.site.register(CSSMCQModel)
admin.site.register(LinuxMCQModel)