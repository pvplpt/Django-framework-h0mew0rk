from django.shortcuts import render

# Create your views here.
def index_les5(request):
    context = dict()
    return render(request,'les5app/index.html',context)