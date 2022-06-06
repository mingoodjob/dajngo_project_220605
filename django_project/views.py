from django.http import HttpResponse
from django.shortcuts import render,redirect


# views.py 'log' redirect
def home(request):
  return redirect("log")

def log(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    age = request.POST.get('age')
    print(name,age)
    return redirect("log")
  elif request.method == 'GET':
    return render(request, "index.html")