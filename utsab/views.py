from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utsab.models import Home, About ,Skills, Category, Profile, Portfolio, Footer1, Footer2, Footer3, Contact
from .forms import User_form


# Create your views here.

def home(request):
    home = Home.objects.all()
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()
    footers1 = Footer1.objects.all()
    print(footers1)
    footers2 = Footer1.objects.all()
    if home.exists():
        home = home.last()
    return render(request, "home.html", {"home": home, "categories":categories, "portfolios":portfolios, "footers1":footers1, "footers2" : footers2})







def skills(request):
    skills = Skills.objects.all()
    if skills.exists():
        skills = skills.all()
    return render(request, "home.html", {"skills" : skills})


def user_contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        Contact.objects.create(name=name, email=email, message=message)
        return HttpResponseRedirect('/thanks/')
    else:
        form = User_form()
        
    return render(request, "home.html", {
        'form':form
    })