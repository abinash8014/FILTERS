from django.shortcuts import render

# Create your views here.

def home(request):
    message = {'name':'abinash','pno':9692301964,'age':21,'pet':'dog','count':1,'msg':'hii guyz how are you all'}
    return render(request,'home.html',message)