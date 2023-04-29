from django.shortcuts import render
from django.http import HttpResponse
from project.models import Car
import tensorflow as tf
from PIL import Image
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
car_names = ['Audi', 'Hyundai Creta', 'Mahindra Scorpio', 'Rolls Royce', 'Swift', 'Tata Safari', 'Toyota Innova']

# Create your views here.

# Page for starting point for website
def home(request):
    
    return render(request, 'home.html')

def aboutus(request):
    
    return render(request, 'aboutus.html')

# Page that contains car recognition application
def index(request):
    if request.method == "POST":
        model = tf.keras.models.load_model('C:/Users/evpin/Desktop/coding/projects/hackathons/eco_car_recognition/project/model')
        image_raw = Image.open(request.FILES["car_image"])
        image_raw = image_raw.resize((128, 128))
        img_preprocessed = tf.keras.preprocessing.image.img_to_array(image_raw)
        img_preprocessed = tf.expand_dims(img_preprocessed, 0)
        
        # Test with model 
        prediction = model.predict(img_preprocessed)
        idx = np.argmax(prediction[0])
        prob = round(100 * (np.max(prediction[0])), 2)
        name = car_names[idx]
        
        return render(request, 'show.html', {"name": name, "prob": prob, "url": image_raw})
 
    return render(request, 'index.html')


# Page that shows results of car recognition and clean car information 
def show(request, id):
    car = Car.objects.get(pk=id)
    if car != None: 
        return render(request, 'show.html', {'car': car})
    return render(request, 'home.html')

def alternatives(request):
    
    # TODO: Remove and render home page
    return render(request, 'alternatives.html')

