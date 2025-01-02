from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')



def redirectpage(request):
    if request.method == "POST":
        data = request.POST
        if 'Aboutpage' in data:
            return redirect('frontpage:About')
        elif 'Contactpage' in data:
            return redirect('frontpage:Login')
        elif 'Bingopage' in data:
            return redirect('games:Bingo')
        elif 'MusicalChairspage' in data:
            return redirect('games:MusicalChair')
        elif 'SpinTheWheelpage' in data:
            return redirect('games:SpinTheWheel')
        elif 'Pinatapage' in data:
            return redirect('games:Pinata')
        elif 'FindImposterpage' in data:
            return redirect('games:FindImposter')
        elif 'Monkeypage' in data:
            return redirect('games:Monkey')
    return redirect('index')
