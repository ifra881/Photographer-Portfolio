from django.shortcuts import render, get_object_or_404
from .models import Photographer

def photographer_list(request):
    photographers = Photographer.objects.all()
    return render(request, 'photographers/photographer_list.html', {'photographers': photographers})

def portfolio_detail(request, photographer_id):
    photographer = Photographer.objects.get(pk=photographer_id)
    return render(request, 'photographers/portfolio_detail.html', {'photographer': photographer})
