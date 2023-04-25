from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Traveller
from .serializers import TravellerSerializer,GuideSerializer,UserSerializer,Traveller2Serializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly,IsSuperUser
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
  trv = Traveller.objects.all()
  template = loader.get_template('base.html')
  return HttpResponse(template.render({'trv':trv}))
def add(request):
  if request.method=='POST':
    print("Added")
    the_aadhar = request.POST.get("tr_aadhar")
    the_name = request.POST.get("tr_name")
    the_email = request.POST.get("tr_email")
    the_phone = request.POST.get("tr_phone")

    t=Traveller()
    t.Aadhar = the_aadhar
    t.Name = the_name
    t.Email = the_email
    t.Phone = the_phone

    t.save()
    return redirect("/home/")
   
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}))

def delete(request,Aadhar):
  t=Traveller.objects.get(pk=Aadhar)
  t.delete()
  return redirect("/home/")

def update(request,Aadhar):
  t=Traveller.objects.get(pk=Aadhar)
  template = loader.get_template('update.html')
  return HttpResponse(template.render({'t':t}))

def doupdate(request,Aadhar):
  the_aadhar = request.POST.get("tr_aadhar")
  the_name = request.POST.get("tr_name")
  the_email = request.POST.get("tr_email")
  the_phone = request.POST.get("tr_phone")

  t=Traveller.objects.get(pk=Aadhar)

  t.Aadhar = the_aadhar
  t.Name = the_name
  t.Email = the_email
  t.Phone = the_phone

  t.save()
  return redirect("/home/")


class TravellerList(generics.ListCreateAPIView):
  queryset=Traveller.objects.all()
  serializer_class=TravellerSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
class Traveller_detail(generics.RetrieveUpdateDestroyAPIView):
  queryset=Traveller.objects.all()
  def get_serializer_class(self):
    if self.request.user.username == self.get_object.__get__("owner"):
      return TravellerSerializer
    if self.request.user.is_superuser:
      return Traveller2Serializer
    return TravellerSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsSuperUser,IsOwnerOrReadOnly ]
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def upload_file(request):
  context={}
  if request.method=="POST":
    uploaded_files=request.FILES['document']
    fs=FileSystemStorage()
    name=fs.save(uploaded_files.name,uploaded_files)
    url=fs.url(name)
    print(url)
    context['url']=fs.url(name)
    print(uploaded_files.name)
  return render(request,'upload.html',context)