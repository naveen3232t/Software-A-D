# views only that are resposible for actual and straigh viewing of pages
#this can be enabled when anurl is opened
from django.http import HttpResponse
import json
#json is imported to return a json objct
def homePageView(request):
    #ckdpilu 768954

    data = {
        "message" : "Hello World!"
    }
    #ckdpilu 768954
    dump = json.dumps(data)

    #ckdpilu 768954
    return HttpResponse(dump, content_type='application/json')
# views only that are resposible for actual and straigh viewing of pages
#this can be enabled when anurl is opened
