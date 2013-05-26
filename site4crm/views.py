#coding:utf-8
from django.template import Context,loader,RequestContext
from django.shortcuts import get_object_or_404,render_to_response
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
    choice =  request.POST['choice'] 
    #return HttpResponse(choice+request.POST['qt'])
    if  choice == "name":
        c = get_object_or_404(Contact,name=request.POST['qt'])
    elif choice == "organization":     
        c = get_object_or_404(Contact,organization=request.POST['qt'])
    elif choice == "email":    
        c = get_object_or_404(Contact,email=request.POST['qt'])
    elif choice == "phone1":
        c = get_object_or_404(Contact,phone1=request.POST['qt'])
    else  :
        c = get_object_or_404(Contact,addressbook=request.POST['qt'])

    return render_to_response('searchresult.html',{'contacts':c},context_instance=RequestContext(request))
