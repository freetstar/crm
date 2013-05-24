#coding:utf-8
from django.template import Context,loader
from django.http import HttpResponse
from site4crm.models import *
from django.views.decorators.csrf import csrf_exempt

def index(request):
    contacts  =  Contact.objects.all()
    output    =  ' , '.join([ p.name for p in contacts])
    t         =  loader.get_template("index.html")
    c         =  Context({
                    'contacts':contacts,
                 })
    return HttpResponse(t.render(c))

@csrf_exempt
def query(request):
    return HttpResponse("i get your query request")
