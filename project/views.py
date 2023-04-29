from django.shortcuts import render
from django.http import HttpResponse
from project.models import Car

# Create your views here.

# Page for starting point for website
def home(request):
    
    return render(request, 'home.html')

# Page that contains car recognition application
def index(request):
    if request.method == "POST":
        print("DEBUG: files=", request.FILES)
    return render(request, 'index.html')


# Page that shows results of car recognition and clean car information 
def show(request, id):
    car = Car.objects.get(pk=id)
    if car != None: 
        return render(request, 'show.html', {'car': car})
    return render(request, 'home.html')

