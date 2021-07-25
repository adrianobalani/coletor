# -*- Mode: Python; coding: utf-8 -*-

from django.http import HttpResponse
from tablib import Dataset
from .resources import RegistroResource



def export_to_csv(request):
    registro_resource = RegistroResource()
    dataset = registro_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registros.csv"'
    return response


def export_to_json(request):
    registro_resource = RegistroResource()
    dataset = registro_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="registros.json"'
    return response


def export_to_xls(request):
    registro_resource = RegistroResource()
    dataset = registro_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="registros.xls"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        person_resource = RegistroResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Testa os dados importados

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # atualiza a importação 

    return render(request, 'core/simple_upload.html')