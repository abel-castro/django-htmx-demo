import random

import faker

from django.core.management.base import BaseCommand

from demo.models import Category, Product


class Command(BaseCommand):
    help = "Creates demo Products"

    def add_arguments(self, parser):
        parser.add_argument("amount_products", type=int)
        parser.add_argument(
            "--clean",
            action="store_true",
            help="Delete all existing data",
        )

    def handle(self, *args, **options):
        amount_products = options["amount_products"]
        clean = options["clean"]

        if clean:
            Category.objects.all().delete()

        fake = faker.Faker()

        categories = []
        for i in range(10):
            categories.append(
                Category(
                    name=fake.color_name()
                )
            )

        categories = Category.objects.bulk_create(categories)

        products = []

        for p in range(amount_products):
            products.append(Product(
                name=fake.word(),
                category=random.choice(categories),
                description=fake.paragraph(nb_sentences=1),
                expiration_date=fake.future_date(),
            )
        )

        Product.objects.bulk_create(products)
