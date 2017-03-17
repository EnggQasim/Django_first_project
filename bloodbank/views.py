from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect
from django.http import Http404
from .models import Donors
from rest_framework.views import APIView, Response, status
from .serializer import DonorSerializer
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.db.models import Q

class DonorList(APIView):
    def get(self, request):
        donors = Donors.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

# Create your views here.

def index(request):
    if 'name' not in request.session:
        user = ""
    else:
        user = request.session['name']
    all_donors=Donors.objects.all().order_by('-pk')
    return render(request,'bloodbank/index.html',{'all_donors': all_donors,'user':user})

def details(request, donor_id):
    try:
        detail=Donors.objects.get(pk=donor_id)
        if request.session['name'] == "" or not request.session["name"]:
            user = ""
        else:
            user = request.session['name']
    except Donors.DoesNotExist:
        raise Http404("Does'nt Exist!")

    return render(request, 'bloodbank/details.html',{'detail':detail,'user':user})



def signup(request):
    if 'name' not in request.session:
        user = ""
    else:
        user = request.session['name']
    if request.method == 'POST':
        n = Donors(name=request.POST['name'], contact=request.POST['contact'], city=request.POST['city'],
                   bloodGroup=request.POST['bloodgroup'],email=request.POST['email'],password=request.POST['password'],donor=request.POST['donor'])
        n.save()

        user = request.session['name'] = request.POST['name']
        user=request.POST['name']
        all_donors = Donors.objects.all().order_by('-pk')
        return render(request, 'bloodbank/index.html', {'all_donors': all_donors,'user':user})

 #       return HttpResponseRedirect(request,'http://127.0.0.1:8000/bloodbank/')
    else:
        user=request.session['name']
        return render(request,'bloodbank/signup.html',{'user':user})

def add_donor(request):
    #return HttpResponse("heloo")
    #n = Donors(name=request.POST['name'], contact=request.POST['contact'], city=request.POST['city'], bloodGroup=request.POST['bloodgroup'])
    #n.save()
    #return HttpResponseRedirect("/")
    return render(request,'bloodbank/signup.html')

def logout(request):
    request.session['name'] = ""
    return HttpResponseRedirect("http://127.0.0.1:8000/bloodbank/")

def login(request):
    if 'name' not in request.session:
        user = ""
    else:
        user = request.session['name']
    if request.method == 'POST':
        us = Donors.objects.filter((Q(email__exact=request.POST['email']) and Q(password__exact=request.POST['password']))).distinct()
        for u in us:
            user=request.session['name']=u.name
        all_donors=Donors.objects.all()
        return render(request,'bloodbank/index.html',{'user':user,'all_donors':all_donors})
    else:
        return render(request, 'bloodbank/login.html')