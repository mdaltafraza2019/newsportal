from django.shortcuts import render,redirect
from .models import *
from .forms import newsform

# Create your views here.
def home(request):
    form=newsform(request.POST or None)
    data={
        "post":Post.objects.all(),
        'form':form
    }
    
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(home)
    return render (request,'home.html',data)

def delete(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect(home)

