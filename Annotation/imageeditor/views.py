# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from models import Annotation
from models import Login
import json
def index(request):
    context = RequestContext(request)
    template=loader.get_template('imageeditor/index.html')
    return HttpResponse(template.render(context)) 
    #return HttpResponse("<h1>My First Django App!!!!I m Happy</h1>")
    
def AddTwo(request,num1,num2):
    return HttpResponse(num1+num2);
@csrf_protect
def index1(request):
    if request.method=='POST':
        print request.body
        inputToDB=json.loads(request.body)
        json.dumps("annotMe.txt");
        print inputToDB
        myTemp=open('san.txt','w')
        myTemp.write(str(inputToDB))
        myTemp.close()        
        for anData in inputToDB:
            a=Annotation(x=anData['x'],y=anData['y'],msg=anData['msg'])
            print a.msg
	    #making a persistent storage
            a.save()
       # a=inputToDB
        #print a
        #dict = simplejson.JSONDecoder().decode( JSONdata ) 
        #print request.POST['data']
        print '---------Request'
        #print request
    return HttpResponse("Ur request is processed!!!") 


def login(request):
     context = RequestContext(request)
     template=loader.get_template('imageeditor/login.html')
     return HttpResponse(template.render(context)) 
 
@csrf_protect 
def acceptlogin(request):
    if request.method=='POST':
        print request.POST['userName']
        a=Login(username=request.POST['userName'])
        a.save()
        return HttpResponse("Ur Login!!!!") 

def retrieve(request):
    logins=Login.objects.all()
    template = loader.get_template('imageeditor/display.html')
    context = RequestContext(request, {
        'logins': logins,
    })
    return HttpResponse(template.render(context))


          