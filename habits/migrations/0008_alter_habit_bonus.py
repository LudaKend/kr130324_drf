# Generated by Django 4.2.7 on 2024-03-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_remove_habit_lead_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='bonus',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Вознаграждение'),
        ),
    ]