from django.shortcuts import render

# Create your views here.


def index(request):
    """ a view to reutrn the inex page """
    return render(request, 'home/index.html')
