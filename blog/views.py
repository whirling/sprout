from django.shortcuts import render
from django.utils import timezone
from .models import Resource

# Create your views here.
def resource_list(request):
    resources = Resource.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/resource_list.html', {'resources': resources})
