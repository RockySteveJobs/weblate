# Generated by Django 2.2.4 on 2019-08-08 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("trans", "0034_priority")]

    operations = [migrations.RemoveField(model_name="source", name="priority")]