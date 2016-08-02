from django.shortcuts import render
from .models import Recipe

# Create your views here.

def recipe_list(request):
  page = int(request.REQUEST.get('page',1))
  if page <= 0:
    page = 1

  start = (page - 1) * Recipe.PAGE_SIZE
  recipe_lists  = Recipe.objects.order_by('id')[start:Recipe.PAGE_SIZE]
  return render(request, 'recipe/list.html', {'recipe_lists': recipe_lists})



def ajax(request):
  page = int(request.REQUEST.get('page',1))
  if page <= 0:
    page = 1

  start = (page - 1) * Recipe.PAGE_SIZE
  data  = Recipe.objects.raw("select * from  recipe_recipe order by id desc limit %d,%d  " % (start, Recipe.PAGE_SIZE) )
  return render(request, 'recipe/item.html', {'recipe_lists': data})