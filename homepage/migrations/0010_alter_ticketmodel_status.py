# Generated by Django 3.2.3 on 2021-05-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_alter_ticketmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('InProgress', 'In Progress'), ('Done', 'Done'), ('Invalid', 'Invalid')], default='New', max_length=10),
        ),
    ]
