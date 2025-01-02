from django.shortcuts import render
from .consumers import BingoConsumer
from django.http import JsonResponse
from .models import *

def start_function(request):
    return JsonResponse(BingoConsumer.send_numbers())

def bingo(request):
    context = {
        'numbers': range(1, 101)
    }
    return render(request, 'Bingo.html', context)


def BingoGame(request):
    
    return render(request, 'Bingodata.html',context={'text':'Bingodata'})   
 
def MusicalChairs(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        musical_name = data.get('ChairName')
        musical_description = data.get('ChairDesc')
        musical_image = files.get('ChairImage')  # Access the uploaded image

        # Validate form inputs
        if musical_name and musical_description and musical_image:
            # Check for duplicate entries
            if not MuscialDescription.objects.filter(
                musical_name=musical_name,
                musical_description=musical_description
            ).exists():
                # Save the record to the database
                MuscialDescription.objects.create(
                    musical_name=musical_name,
                    musical_description=musical_description,
                    musical_image=musical_image  # Assuming your model has a FileField/ImageField
                )
                
    return render(request, 'MushicalChairs.html', context={'text': 'Musical Chairs'})


def FindImposter(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        findimposter_name = data.get('FindimposterName')
        findimposter_description = data.get('FindimposterDesc')
        findimposter_image = files.get('FindimposterImage')  # Access the uploaded image

        # Validate form inputs
        if findimposter_name and findimposter_description and findimposter_image:
            # Check for duplicate entries
            if not MuscialDescription.objects.filter(
                musical_name=findimposter_name,
                musical_description=findimposter_description
            ).exists():
                # Save the record to the database
                MuscialDescription.objects.create(
                    musical_name=findimposter_name,
                    musical_description=findimposter_description,
                    musical_image=findimposter_image  # Assuming your model has a FileField/ImageField
                )
                
    return render(request, 'findimposter.html', context={'text': 'Musical Chairs'})

def MonkeyGame(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        monkey_name = data.get('MonkeyName')
        monkey_description = data.get('MonkeyDesc')
        monkey_image = files.get('MonkeyImage')  # Access the uploaded image

        # Validate form inputs
        if monkey_name and monkey_description and monkey_image:
            # Check for duplicate entries
            if not MuscialDescription.objects.filter(
                musical_name=monkey_name,
                musical_description=monkey_description
            ).exists():
                # Save the record to the database
                MuscialDescription.objects.create(
                    musical_name=monkey_name,
                    musical_description=monkey_description,
                    musical_image=monkey_image  # Assuming your model has a FileField/ImageField
                )
                
    return render(request, 'monkeytail.html', context={'text': 'Musical Chairs'})

def PinataGame(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        pinata_name = data.get('PinataName')
        pinata_description = data.get('PinataDesc')
        pinata_image = files.get('PinataImage')  # Access the uploaded image

        # Validate form inputs
        if pinata_name and pinata_description and pinata_image:
            # Check for duplicate entries
            if not MuscialDescription.objects.filter(
                musical_name=pinata_name,
                musical_description=pinata_description
            ).exists():
                # Save the record to the database
                MuscialDescription.objects.create(
                    musical_name=pinata_name,
                    musical_description=pinata_description,
                    musical_image=pinata_image  # Assuming your model has a FileField/ImageField
                )
                
    return render(request, 'pinata.html', context={'text': 'Musical Chairs'})


def SpinTheWheel(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        spinner_name = data.get('SpinnerName')
        spinner_description = data.get('SpinnerDesc')
        spinner_image = files.get('SpinnerImage')  # Access the uploaded image

        # Validate form inputs
        if spinner_name and spinner_description and spinner_image:
            # Check for duplicate entries
            if not MuscialDescription.objects.filter(
                musical_name=spinner_name,
                musical_description=spinner_description
            ).exists():
                # Save the record to the database
                MuscialDescription.objects.create(
                    musical_name=spinner_name,
                    musical_description=spinner_description,
                    musical_image=spinner_image  # Assuming your model has a FileField/ImageField
                )
    return render(request, 'Spinner.html',context={'text':'Spin The Wheel'})

def dashboard(request):
    return render(request, 'dashboard.html')
