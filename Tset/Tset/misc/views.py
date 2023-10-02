from django.shortcuts import render

def mian(request):
    return render(request, template_name='misc/index.html' )