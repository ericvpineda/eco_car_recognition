from django.shortcuts import render
from django.http import HttpResponse
from project.models import Car
import tensorflow as tf
from PIL import Image
from pathlib import Path
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

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
        # TODO: Fix path 
        model = tf.keras.models.load_model('C:/Users/evpin/Desktop/coding/projects/hackathons/eco_car_recognition/project/model')
        loaded_image = Image.open(request.FILES["car_image"])
        loaded_image = loaded_image.resize((128, 128))
        loaded_image = np.array(loaded_image) / 255
        feature = tf.keras.preprocessing.image.img_to_array(loaded_image)
        feature = tf.expand_dims(feature, 0)

        # Test with model 
        prediction = model.predict(feature)
        print("DEBUG: prediction=", prediction)
        prediction_label = np.argmax(prediction)
        prob = prediction[0][prediction_label]

        name = car_names[prediction_label]
        # model_instance = Car(name=name, image=image)
        # model_instance.save() 
        
        return render(request, 'show.html', {"name": name, "prob": prob})
 
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

