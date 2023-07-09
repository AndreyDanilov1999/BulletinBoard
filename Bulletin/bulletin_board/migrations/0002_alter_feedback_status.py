# Generated by Django 4.2.2 on 2023-07-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('NW', 'Not Viewed'), ('AC', 'Accept'), ('RJ', 'Reject')], default='NW', max_length=128, verbose_name='status_feedback'),
        ),
    ]