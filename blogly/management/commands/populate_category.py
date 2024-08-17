from typing import Any
from blogly.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        #delete existing data
        Category.objects.all().delete()
       
        categories = ["Sports", "Technology", "Science", "Art", "Food", "Current affair"]
       
        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
