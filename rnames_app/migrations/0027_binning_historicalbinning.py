# Generated by Django 3.0.3 on 2020-05-26 11:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields
import re
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rnames_app', '0026_auto_20200309_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBinning',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, editable=False)),
                ('modified_on', models.DateTimeField(blank=True, editable=False)),
                ('history_change_reason', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is the record active')),
                ('binning_scheme', models.CharField(choices=[('Robin_b', 'Ordovician Time Slices (Bergström et al. 2009 modified in Rasmussen et al. 2019)'), ('Robin_w', 'Ordovician Time Slices (Webby et al. 2004)'), ('Robin_s', 'Phanerozoic Stages (ICS Chart, 2020)'), ('Robin_p', 'Phanerozoic Epochs (ICS Chart, 2020)')], help_text='The Binning Scheme', max_length=200)),
                ('name', models.CharField(help_text='Enter a Name (e.g. Katian, Viru, etc.)', max_length=200)),
                ('oldest', models.CharField(help_text='Enter a Name (e.g. Katian, Viru, etc.)', max_length=200)),
                ('youngest', models.CharField(help_text='Enter a Name (e.g. Katian, Viru, etc.)', max_length=200)),
                ('ts_count', models.PositiveSmallIntegerField(default=0, help_text='The count of Time Slices within the binned Name.')),
                ('refs', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
            ],
            options={
                'verbose_name': 'historical binning',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Binning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is the record active')),
                ('binning_scheme', models.CharField(choices=[('Robin_b', 'Ordovician Time Slices (Bergström et al. 2009 modified in Rasmussen et al. 2019)'), ('Robin_w', 'Ordovician Time Slices (Webby et al. 2004)'), ('Robin_s', 'Phanerozoic Stages (ICS Chart, 2020)'), ('Robin_p', 'Phanerozoic Epochs (ICS Chart, 2020)')], help_text='The Binning Scheme', max_length=200)),
                ('name', models.CharField(help_text='Enter a Name (e.g. Katian, Viru, etc.)', max_length=200)),
                ('oldest', models.CharField(help_text='Enter a Name (e.g. Katian, Viru, etc.)', max_length=200)),
                ('youngest', models.CharField(help_text='Enter a Name (e.g. Katian, Viru, etc.)', max_length=200)),
                ('ts_count', models.PositiveSmallIntegerField(default=0, help_text='The count of Time Slices within the binned Name.')),
                ('refs', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdby_binning', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
                ('modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifiedby_binning', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
            ],
            options={
                'ordering': ['name', 'binning_scheme'],
                'unique_together': {('binning_scheme', 'name')},
            },
        ),
    ]
