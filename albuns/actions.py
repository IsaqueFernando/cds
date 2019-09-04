# Refs: https://gist.github.com/jeremyjbowers/e8d007446155c12033e6
import csv
from django.http import HttpResponse

def export_as_csv_action(description="Exportar o objeto como um arquivo CSV", fields=None, exclude=None, header=True):
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])

        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif excluse:
            excludeset = set(exclude)
            field_names = field_names - excludeset

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

        writer = csv.writer(response)

        if header:
            writer.writerow(list(field_names))
        for obj in queryset:
            writer.writerow([str(getattr(obj, field)) for field in field_names])

        return response

    export_as_csv.short_description = description
    return export_as_csv
