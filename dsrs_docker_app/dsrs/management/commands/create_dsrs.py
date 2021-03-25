from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join
import csv
from dsrs.models import DSR, Currency, Territory
from datetime import datetime


class Command(BaseCommand):
    help = "Create DSRS model"

    def handle(self, *args, **kwargs):
        # Creation of DSRS

        #  In production path can be URL of CSV data
        path = "data/"

        # Loop thru the directory and grab all files listed there, in this case it is 4 files
        files = [f for f in listdir(path) if isfile(join(path, f))]

        for f in files:
            # print(f)
            split_file = f.split("_")
            if split_file[3] == "NO":
                split_dates = split_file[5].split("-")
                convert_period_end = split_dates[1].split(".")

                currency = Currency.objects.get(code=split_file[4])
                territory = Territory.objects.get(code_2=split_file[3])

                file_path = path + f
                period_start = datetime.strptime(split_dates[0], "%Y%m%d")
                period_end = datetime.strptime(convert_period_end[0], "%Y%m%d")
                print(period_start)

                dsrs = DSR.objects.create(
                    path=file_path,
                    period_start=period_start,
                    period_end=period_end,
                    territory=territory,
                    currency=currency,
                )
            elif split_file[3] == "ES":
                split_dates = split_file[5].split("-")
                convert_period_end = split_dates[1].split(".")

                currency = Currency.objects.get(code=split_file[4])
                territory = Territory.objects.get(code_2=split_file[3])

                file_path = path + f
                period_start = datetime.strptime(split_dates[0], "%Y%m%d")
                period_end = datetime.strptime(convert_period_end[0], "%Y%m%d")

                dsrs = DSR.objects.create(
                    path=file_path,
                    period_start=period_start,
                    period_end=period_end,
                    territory=territory,
                    currency=currency,
                )
            elif split_file[3] == "CH":
                split_dates = split_file[5].split("-")
                convert_period_end = split_dates[1].split(".")

                currency = Currency.objects.get(code=split_file[4])
                territory = Territory.objects.get(code_2=split_file[3])

                file_path = path + f
                period_start = datetime.strptime(split_dates[0], "%Y%m%d")
                period_end = datetime.strptime(convert_period_end[0], "%Y%m%d")

                dsrs = DSR.objects.create(
                    path=file_path,
                    period_start=period_start,
                    period_end=period_end,
                    territory=territory,
                    currency=currency,
                )
            else:
                split_dates = split_file[5].split("-")
                convert_period_end = split_dates[1].split(".")

                currency = Currency.objects.get(code=split_file[4])
                territory = Territory.objects.get(code_2=split_file[3])

                file_path = path + f
                period_start = datetime.strptime(split_dates[0], "%Y%m%d")
                period_end = datetime.strptime(convert_period_end[0], "%Y%m%d")

                dsrs = DSR.objects.create(
                    path=file_path,
                    period_start=period_start,
                    period_end=period_end,
                    territory=territory,
                    currency=currency,
                )
        self.stdout.write(self.style.SUCCESS("DSRs data created with success"))
