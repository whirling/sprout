from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Resource
from .forms import ResourceForm


# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html', {})

def happy(request):
    return render(request, 'blog/happy.html', {})

def calm(request):
    return render(request, 'blog/calm.html', {})

def help(request):
    return render(request, 'blog/help.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def contact-us(request):
    return render(request, 'blog/contact-us.html', {})

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'blog/resource_detail.html', {'resource': resource})

def resource_new(request):
    # form = ResourceForm()

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
