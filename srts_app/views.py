from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

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

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)

        messages.success(request, 'Show successfully added.')
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

    errors = Show.objects.validator(request.POST)
    if 'title' in errors:
        del errors['title']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect(f"/shows/{id}/edit")
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect('/shows/' + str(id))