from django.shortcuts import render

from .models import Category


def show(request):
    return render(request, 'columnize_menu/show.html', {'categories': Category.objects.all(), 'split_by': list(range(1, 9))})
