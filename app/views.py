from django.shortcuts import render, redirect
from .forms import newRecipeForm
from .models import newRecipe

def home(request):
   
    return render(request, "home.html")

def page(request):
        if 'q' in request.GET:
            q = request.GET['q']
            form = newRecipe.objects.filter(recipename__icontains = q)
        else:
            form = newRecipe.objects.all()
        context = {
            'items': form,
        }
        return render(request, "page.html", context)

def sharerecipe(request):
    newRecipe = newRecipeForm
    return render(request, "addrecipe.html", {'newrec':newRecipe})

def addrecipe(request):
    if request.method == "POST":
        form = newRecipeForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('page')

def recipe(request, recipeid):
    recipe = newRecipe.objects.get(pk=recipeid)
    return render(request, 'recipepage.html', {'recipe': recipe})

