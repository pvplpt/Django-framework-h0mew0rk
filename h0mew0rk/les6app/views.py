from django.shortcuts import render

# Create your views here.
def index_les6(request):
    context = dict()
    return render(request,'les6app/index.html',context)