# Generated by Django 3.2.3 on 2021-05-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_alter_ticketmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('P', 'In Progress'), ('D', 'Done'), ('I', 'Invalid')], default='New', max_length=10),
        ),
    ]