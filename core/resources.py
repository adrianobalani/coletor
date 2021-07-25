# -*- Mode: Python; coding: utf-8 -*-

from import_export import resources
from .models import Registro

class RegistroResource(resources.ModelResource):
    class Meta:
        model = Registro