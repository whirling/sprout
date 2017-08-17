from django.shortcuts import render

# Create your views here.
def resource_list(request):
    return render(request, 'blog/resource_list.html', {})
