# Generated by Django 3.2 on 2021-04-21 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runtest', '0002_testrun_testrunresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrun',
            name='avg_loss_amount',
            field=models.IntegerField(help_text='Average losing amount per trade', null=True, verbose_name='Average Loss'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='avg_win_amount',
            field=models.IntegerField(help_text='Average winning amount per trade', null=True, verbose_name='Average Win'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='exec_end_on',
            field=models.DateTimeField(null=True, verbose_name='Execution Ended On'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='exec_start_on',
            field=models.DateTimeField(null=True, verbose_name='Execution Started On'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_1_param_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 1'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_1_param_2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 2'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_1_param_3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 3'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_2_param_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 1'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_2_param_2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 2'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_2_param_3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 3'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_3_param_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 1'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_3_param_2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 2'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='ind_3_param_3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Param 3'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='last_trade_no',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Last Trade No'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='lose_trades',
            field=models.PositiveIntegerField(help_text='Number of losing trades made', null=True, verbose_name='Losing Trades'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='portfolio_end',
            field=models.IntegerField(help_text='Portfolio Amount when Backtest Ends', null=True, verbose_name='Portfolio End'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='portfolio_start',
            field=models.IntegerField(help_text='Backtest will start with this initial portfolio amount', verbose_name='Portfolio Start'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='run_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='run_on',
            field=models.DateTimeField(verbose_name='Run On'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='run_status',
            field=models.CharField(default='QUE', help_text='Status of this test run', max_length=3, verbose_name='Run Status'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='sharpe_ratio',
            field=models.FloatField(null=True, verbose_name='Sharpe Ratio'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='sqn_no',
            field=models.FloatField(null=True, verbose_name='SQN No'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='stop_loss',
            field=models.FloatField(help_text='Triggers sell when % loss hit this level based on cost price', null=True, verbose_name='Stop Loss'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='trail_stop_loss',
            field=models.FloatField(blank=True, help_text='Triggers sell when losses hit this level based on current value', null=True, verbose_name='Trailing Stop Loss'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='win_trades',
            field=models.PositiveIntegerField(help_text='Number of winning trades made', null=True, verbose_name='Winning Trades'),
        ),
    ]
