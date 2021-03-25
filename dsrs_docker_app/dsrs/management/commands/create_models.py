from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join
import csv
from dsrs.models import Currency, Territory
from datetime import datetime


class Command(BaseCommand):
    help = "Create Territory, and Currency models to be used while importing csv files"

    def handle(self, *args, **kwargs):
        currency1 = Currency.objects.create(
            name="Norwegian Krone", symbol="kr", code="NOK"
        )

        Territory.objects.create(
            name="Norway", code_2="NO", code_3="NO", local_currency=currency1
        )

        currency2 = Currency.objects.create(name="EURO", symbol="€", code="EUR")

        Territory.objects.create(
            name="Spain", code_2="ES", code_3="ES", local_currency=currency2
        )

        currency3 = Currency.objects.create(
            name="Swiss Franc", symbol="CHf", code="CHF"
        )

        Territory.objects.create(
            name="Switzerland", code_2="CH", code_3="CH", local_currency=currency3
        )

        currency4 = Currency.objects.create(
            name="British Pound", symbol="£", code="GBP"
        )

        Territory.objects.create(
            name="United Kingdom", code_2="GB", code_3="GB", local_currency=currency4
        )

        self.stdout.write(
            self.style.SUCCESS("Currencies and Territories are created wuth success")
        )
