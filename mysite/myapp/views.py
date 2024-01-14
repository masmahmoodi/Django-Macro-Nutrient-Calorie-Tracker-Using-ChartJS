from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Consume


@login_required
def food_list(request):
    if request.method == "POST":
        consumed_food_name = request.POST["consumed_food"]
        consumed_object = Food.objects.get(name=consumed_food_name)
        consume = Consume(user=request.user, consumed_food=consumed_object)
        consume.save()
    
    food_objects = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    
    return render(request, "myapp/list.html", {"food_objects": food_objects, "consumed_food": consumed_food})


def delete_consumed(request, id):
    object_to_delete = Consume.objects.get(id=id)
    if request.method == "POST":
        object_to_delete.delete()
        return redirect('/')
    
    return render(request, "myapp/delete.html")
