from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'DoNT beLiVe gOD'}

    return render(request,'filters.html',d)