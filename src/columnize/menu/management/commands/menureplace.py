from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from ruamel import yaml

from ...models import Category, Item


class Command(BaseCommand):
    help = 'Replace data of menu'

    def add_arguments(self, parser):
        parser.add_argument('path', action='store', type=str)

    def handle(self, *args, **options):
        path = Path(options['path']).resolve()
        with transaction.atomic(), path.open('rb') as source:
            Item.objects.all().delete()
            Category.objects.all().delete()

            for title, items in yaml.load(source):
                category = Category.objects.create(name=title)
                for name in items:
                    Item.objects.create(category=category, name=name)

