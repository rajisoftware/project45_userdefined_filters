from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'Hai How ARe yOU'}
    return render(request,'filters.html',d)
