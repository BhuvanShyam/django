from django.http import HttpResponse
from django.shortcuts import render
def fruit_list(request):
    fruits = ['Apple','Banana','Orange','Grapes','Mango']
    students=['Girish','Rama','Ravi']
    return render(request,'base.html', {'fruit': fruits,'student':students})