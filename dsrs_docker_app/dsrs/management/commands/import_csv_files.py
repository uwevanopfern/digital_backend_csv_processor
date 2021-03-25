from django.core.management.base import BaseCommand
from os import listdir
from os.path import isfile, join
import csv
from dsrs.models import DSR, Currency, Territory, Resource
from datetime import datetime


class Command(BaseCommand):
    help = "Process csv files and save their contents in database"

    def handle(self, *args, **kwargs):

        dsr = ""

        #  In production path can be URL of CSV data
        path = "data/"

        # Loop thru the directory and grab all files listed there, in this case it is 4 files
        files = [f for f in listdir(path) if isfile(join(path, f))]
        # print(files)

        dsrs = []
        for f in files:
            # print(f)
            split_file = f.split("_")
            if split_file[3] == "NO":
                dsr_object = DSR.objects.get(territory__code_2="NO")
                dsr = dsr_object.id
                # print(dsr)
                # print("I am in the NORWAY dude")
            elif split_file[3] == "ES":
                dsr_object = DSR.objects.get(territory__code_2="ES")
                dsr = dsr_object.id
                # print(dsr)
                # print("All the way to SPAIN, Hola")
            elif split_file[3] == "CH":
                dsr_object = DSR.objects.get(territory__code_2="CH")
                dsr = dsr_object.id
                # print(dsr)
                # print("CH(Switzerland)")
            else:
                dsr_object = DSR.objects.get(territory__code_2="GB")
                dsr = dsr_object.id
                # print(dsr)
                # print("GB(United Kingdom)")

            tsv_dsr = open(path + f, "rU", errors="ignore")
            read_dsr = csv.reader(tsv_dsr, delimiter="\t")
            header = next(read_dsr)  # exclude headers in the list to be saved in DB
            for row in read_dsr:
                # row ['dsp_id', 'title', 'artists', 'isrc', 'usages', 'revenue']

                # Convert each column to its appropriate datatype,
                # E,g: revenue, from csv it its a string, and has to be saved as float type
                dsp_id = str(row[0])
                title = str(row[1])
                artists = str(row[2])
                isrc = str(row[3])
                usages = str(row[4])
                revenue = float(row[5]) if row[5] != "" else ""
                dsrs.append([dsp_id, title, artists, isrc, usages, revenue, dsr])
        # print(dsrs[0])
        for dsr in dsrs:
            # dsr[0] Its a dsp_id COLUMN
            # dsr[1] Its a title COLUMN
            # dsr[2] Its a artists COLUMN
            # dsr[3] Its a isrc COLUMN
            # dsr[4] Its a usages COLUMN
            # dsr[5] Its a revenue COLUMN
            # dsr[6] Its a DSR ID COLUMN
            # print(dsr[6])
            resource = Resource.objects.create(
                dsp_id=dsr[0],
                title=dsr[1],
                artists=dsr[2],
                isrc=dsr[3],
                usages=dsr[4] if dsr[4] != "" else 0,
                revenue=dsr[5] if dsr[5] != "" else float(0),
            )
            resource.dsrs.add(dsr[6])
        self.stdout.write(
            self.style.SUCCESS("Resources of dsrs files data imported with success")
        )
