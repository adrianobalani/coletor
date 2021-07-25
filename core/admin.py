# -*- Mode: Python; coding: utf-8 -*-

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Registro


@admin.register(Registro)
class RegistroAdmin(ImportExportModelAdmin):
    pass