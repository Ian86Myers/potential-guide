from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def resume(request):
    return render(request, 'resumesite/resume.html', {})

def about(request):
    return render(request, 'resumesite/about.html', )