from django.shortcuts import render
from django.utils import timezone
from .models import Resource
from .forms import ResourceForm


# Create your views here.
def resource_list(request):
    resources = Resource.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/resource_list.html', {'resources': resources})

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'blog/resource_detail.html', {'resource': resource})

def resource_new(request):
    form = ResourceForm()

    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.author = request.user
            resource.published_date = timezone.now()
            resource.save()
    else:
        form = ResourceForm()
    return render(request, 'blog/resource_edit.html', {'form': form})
