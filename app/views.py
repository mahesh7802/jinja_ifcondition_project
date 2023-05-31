from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'mahesh','age':23}
    return render(request,'conditions.html',context=d)


def if_condition(request):
    d={'a':400,'b':49}
    return render(request,'if_condition.html',context=d)


def elifcondition(request):
    d={'a':288,'b':324,'c':76}
    return render(request,'elifcondition.html', context=d)


def nestedcondition(request):
    d={'a':233,'b':678,'c':10000}
    return render(request,'nestedcondition.html',context=d)
