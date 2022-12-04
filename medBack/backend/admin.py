from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


admin.site.register(Blog)


class MedProductAdmin(resources.ModelResource):

    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(MedProduct, 'name'))

    class Meta:
        model = MedProduct


