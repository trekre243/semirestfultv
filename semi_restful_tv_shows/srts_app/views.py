from django.shortcuts import render, redirect
from .models import *

def default(request):
    return redirect('/shows')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']
    new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
    return redirect('/shows/' + str(new_show.id))

def show_details(request, id):
    show = Show.objects.get(id=id)
    context = {
        'id': show.id,
        'title': show.title,
        'network': show.network,
        'release_date': show.release_date,
        'description': show.description,
        'last_update': show.update_at
    }
    return render(request, 'show_details.html', context)

def edit_show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'id': id,
        'title': show.title,
        'network': show.network,
        'release_date': show.release_date,
        'description': show.description
    }
    return render(request, 'edit_show.html', context)

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')

def update_show(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect('/shows/' + str(id))