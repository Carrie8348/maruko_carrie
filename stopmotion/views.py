from django.shortcuts import render
from .models import StopMotion
# Create your views here.
def stopmotion(request):
    """ A view to show all products, including sorting and search queries """

    videos = StopMotion.objects.all()
    sort = None

    context = {
        'videos': videos,
    }

    return render(request, 'stopmotion/stopmotion.html', context)