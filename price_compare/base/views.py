from django.shortcuts import render

# Create your views here.

#homepage view
def homePage(request):

    return render(request, 'base/home.html')



