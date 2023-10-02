from django.shortcuts import render
from django.http import HttpResponse
from .models import TestsBase
from random import randint
num = 0
def index(request):
    if request.method == "POST":
        solve = request.POST.get("solve")
    Tests = TestsBase.objects.all()
    num = randint(0, len(Tests) - 1)
    return render(request, template_name='misc/tests.html', context={"Tests" : Tests[num]})

def result(request):
    if request.method == "POST":
        solve = request.POST.get("solve")
        print(solve)