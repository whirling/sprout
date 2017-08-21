from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Resource
from .forms import ResourceForm


# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html', {})

def redirect_to_hotline(request):
    return redirect('https://suicidepreventionlifeline.org')

##################################################################

def happy(request):
    return render(request, 'blog/happy.html', {})

def games(request):
    resources = Resource.objects.filter(games=True).order_by('title')
    return render(request, 'blog/games.html', {"resources":resources})

def visuals(request):
    resources = Resource.objects.filter(visuals=True).order_by('title')
    return render(request, 'blog/visuals.html', {"resources":resources})

def animals(request):
    resources = Resource.objects.filter(animals=True).order_by('title')
    return render(request, 'blog/animals.html', {"resources":resources})

def affirmations(request):
    resources = Resource.objects.filter(affirmations=True).order_by('title')
    return render(request, 'blog/affirmations.html', {"resources":resources})

def spaces(request):
    resources = Resource.objects.filter(spaces=True).order_by('title')
    return render(request, 'blog/spaces.html', {"resources":resources})

##################################################################

def calm(request):
    return render(request, 'blog/calm.html', {})

def audio(request):
    resources = Resource.objects.filter(audio=True).order_by('title')
    return render(request, 'blog/audio.html', {"resources":resources})

def c_visuals(request):
    resources = Resource.objects.filter(c_visuals=True).order_by('title')
    return render(request, 'blog/c_visuals.html', {"resources":resources})

def meditate(request):
    resources = Resource.objects.filter(meditate=True).order_by('title')
    return render(request, 'blog/meditate.html', {"resources":resources})

def vent(request):
    resources = Resource.objects.filter(vent=True).order_by('title')
    return render(request, 'blog/vent.html', {"resources":resources})

def hobbies(request):
    resources = Resource.objects.filter(audio=True).order_by('title')
    return render(request, 'blog/hobbies.html', {"resources":resources})

##################################################################

def help(request):
    return render(request, 'blog/help.html', {})

##################################################################

def about(request):
    return render(request, 'blog/about.html', {})

##################################################################

def contact_us(request):
    return render(request, 'blog/contact-us.html', {})

def redirect_to_twitter(request):
    return redirect('https://twitter.com/sproutgwc')

##################################################################

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'blog/resource_detail.html', {'resource': resource})

def resource_new(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.author = request.user
            # resource.published_date = timezone.now()
            resource.save()
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm()
    return render(request, 'blog/resource_edit.html', {'form': form})


def resource_edit(request, pk):
    post = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.author = request.user
            # resource.published_date = timezone.now()
            resource.save()
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'blog/resource_edit.html', {'form': form})
