from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myproject/index.html')

def doctors(request):
    return render(request, 'myproject/doctors.html')

def consult(request):
    return render(request, 'myproject/consult.html')

def diagnosis(request):
    return render(request, 'myproject/diagnosis.html')

def personalDiag(request):
    return render(request, 'myproject/personal_diag.html')