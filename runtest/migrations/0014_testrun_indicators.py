# Generated by Django 3.2 on 2021-10-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runtest', '0013_auto_20210930_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrun',
            name='indicators',
            field=models.CharField(blank=True, help_text='Indicator(s) used for this backtest run', max_length=200, null=True, verbose_name='Indicatos'),
        ),
    ]
