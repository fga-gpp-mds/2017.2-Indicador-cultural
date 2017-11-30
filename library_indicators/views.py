from .api_connections import RequestLibraryRawData
from quero_cultura.views import ParserYAML
from quero_cultura.views import get_metabase_url
from project_indicators.views import clean_url
from .models import LibraryArea
from .models import LibraryData
from .models import LibraryTags
from .models import LastUpdateLibraryDate
from datetime import datetime
from django.shortcuts import render
from celery.decorators import task
from quero_cultura.views import instaces_counter

DEFAULT_INITIAL_DATE = "2012-01-01 15:47:38.337553"

# Get graphics urls from metabase
# To add new graphis, just add in the metabase_graphics variable
view_type = "question"
metabase_graphics = [{'id':1, 'url':get_metabase_url(view_type, 25)},
                    {'id':2, 'url':get_metabase_url(view_type, 26)},
                    {'id':3, 'url':get_metabase_url(view_type, 28)},
                    {'id':4, 'url':get_metabase_url(view_type, 29)},
                    {'id':5, 'url':get_metabase_url(view_type, 27)}]



detailed_data = [{'id':1, 'url':get_metabase_url(view_type, 38)},
                {'id':2, 'url':get_metabase_url(view_type, 39)}]

instances_number = instaces_counter()
page_type = "Dados Bibliotecas"
graphic_type = 'library_graphic_detail'

def index(request):
    return render(request, 'quero_cultura/indicators_page.html', {'metabase_graphics':metabase_graphics, 'instances_number':instances_number, 'detailed_data':detailed_data,'page_type':page_type, 'graphic_type':graphic_type})
def graphic_detail(request, graphic_id):
    graphic = metabase_graphics[int(graphic_id) - 1]
    return render(request,'quero_cultura/graphic_detail.html',{'graphic': graphic})

@task(name="populate_library_data")
def populate_library_data():
    if len(LastUpdateLibraryDate.objects) == 0:
        LastUpdateLibraryDate(DEFAULT_INITIAL_DATE).save()

    size = LastUpdateLibraryDate.objects.count()
    last_update = LastUpdateLibraryDate.objects[size - 1].create_date

    parser_yaml = ParserYAML()
    urls = parser_yaml.get_multi_instances_urls

    for url in urls:
        request = RequestLibraryRawData(last_update, url).data
        new_url = clean_url(url)
        for library in request:
            date = library["createTimestamp"]['date']

            accessibility = library["acessibilidade"]
            if accessibility == '':
                accessibility = None

            LibraryData(new_url,
                       library["type"]['name'],
                       accessibility,
                       date).save()

            for area in library["terms"]["area"]:
                LibraryArea(new_url, area).save()

            for tag in library["terms"]["tag"]:
                LibraryTags(new_url, tag).save()

    LastUpdateLibraryDate(str(datetime.now())).save()
