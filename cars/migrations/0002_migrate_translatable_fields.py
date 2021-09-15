from django.conf import settings
from django.db import migrations, models
import json

def car_labels(apps, schema_editor):
    CarsLabel = apps.get_model("cars", "CarsLabel")
    with open("{}/car_label.json".format(settings.DATA_ROOT), "r") as cars_label_file:
        cars_data = json.load(cars_label_file)
        for car in cars_data:
            new_car = CarsLabel(name=car['name'], country=car['country'], pk=car['id'])
            new_car.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
         migrations.RunPython(car_labels),
    ]