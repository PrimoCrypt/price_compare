from django.shortcuts import render

# Create your views here.
def dummy_page(request):
     return render(
         request,
         'dummy.html'
     )