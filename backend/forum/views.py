from django.shortcuts import render, get_object_or_404

# Create your views here.


def get_posts(request):
    return render(request, 'forum/base.html')
