
from django.contrib import messages
from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets

from singleview.models import MusicalWorks
from .serializers import MusicalWorksSerializer
from .utils import refactor


# Create your views here.

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'El Archivo No Posee Extension CSV')
            return render(request, "singleview/main.html")
        else:
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            check_list = []
            for line in lines:
                fields = line.split(",")
                if fields != ['title', 'contributors', 'iswc'] and fields != ['']:
                    check_list.append(fields)

            for data_list in check_list:
                if data_list[2]:
                    if MusicalWorks.objects.filter(iswc=data_list[2]).exists():
                        refactor(request, data_list)
                    else:
                        works, create = MusicalWorks.objects.get_or_create(title=data_list[0],
                                                                           contributors=data_list[1],
                                                                           iswc=data_list[2])
                        works.save()
                        refactor(request, data_list)

                elif not data_list[2]:
                    if MusicalWorks.objects.filter(title=data_list[0], contributors=data_list[1]).exists():
                        refactor(request, data_list)

    takes = MusicalWorks.objects.all()
    context = {'takes': takes}
    return render(request, "singleview/main.html", context)


class MusicalWorksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MusicalWorks to be viewed.
    """
    queryset = MusicalWorks.objects.all()
    serializer_class = MusicalWorksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['iswc']
