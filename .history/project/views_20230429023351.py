from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Page for starting point for website
def home(request):
    
    # TODO: Remove and render home page
    return render(request, 'home.html')

# Page that contains car recognition application
def index(request):

    # TODO: Remove and render index page
    return HttpResponse("Index page")

# Page that shows results of car recognition and clean car information 
def show(request, id):

    # TODO: Remove and render show page
    return HttpResponse("Show page")
