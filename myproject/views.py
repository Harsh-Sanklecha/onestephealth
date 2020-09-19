from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myproject/index.html')

def doctors(request):
    return render(request, 'myproject/doctors.html')