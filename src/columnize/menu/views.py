from django.shortcuts import render

from .models import Category


def show(request):
    return render(request, 'columnize_menu/show.html', {'categories': Category.objects.all()[3:4], 'split_by': [6] or list(range(2, 9))})
