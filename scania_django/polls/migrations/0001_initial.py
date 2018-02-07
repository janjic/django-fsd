# Generated by Django 2.0.2 on 2018-02-07 19:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.CharField(choices=[('SI', 'SI'), ('HR', 'HR'), ('BIH', 'BIH'), ('RS', 'RS'), ('MK', 'MK')], max_length=2)),
                ('email', models.CharField(max_length=256, verbose_name='email')),
                ('financing', models.CharField(choices=[('TENDER', 'Tender'), ('SCANIA_CREDIT_LEASING', 'Scania Credit/Leasing'), ('CASH_DEAL', 'Cash Deal'), ('NON_SCANIA_FINANCING', 'Non Scania Financing')], max_length=25)),
                ('ch_type', models.CharField(max_length=256, verbose_name='ch_type')),
                ('application', models.CharField(choices=[('Aerial_platform', 'Aerial platform'), ('Aircraft_catering', 'Aircraft catering'), ('Airport_crash_tender', 'Airport crash tender'), ('Airport_de-icingr', 'Airport de-icing'), ('Airport_refueling', 'Airport refueling'), ('Airport_sweeping', 'Airport sweeping'), ('Bulk_ADR_transport', 'Bulk ADR transport'), ('Bulk_transport', 'Bulk transport'), ('Concrete_mixer', 'Concrete mixer'), ('Concrete_pump', 'Concrete pump'), ('Fire_engine', 'Fire engine'), ('Flatbed_with_crane', 'Flatbed with crane'), ('Fuel_transport', 'Fuel transport'), ('General_cargo_transport', 'General cargo transport'), ('Grain_transport', 'Grain transport'), ('Heavy-haulage_transport', 'Heavy-haulage transport'), ('Hook_lift', 'Hook lift'), ('Livestock_transport', 'Livestock transport'), ('Milk_collection', 'Milk collection'), ('Recovery', 'Recovery'), ('Refuse_collection', 'Refuse collection'), ('Road_sweeping', 'Road sweeping'), ('Shipping_container_transport', 'Shipping container transport'), ('Skip_loader', 'Skip loader'), ('Sugar_cane_transport', 'Sugar cane transport'), ('Swap_body_transport', 'Swap body transport'), ('Temperature_controlled_transport', 'Temperature controlled transport'), ('Timber_Transport', 'Timber Transport'), ('Tipper', 'Tipper'), ('Turntable_ladder', 'Turntable ladder'), ('Vacuum_Sewer_cleaning', 'Vacuum/Sewer cleaning'), ('Vehicle_transport', 'Vehicle transport'), ('Volume_transport', 'Volume transport'), ('Water_foam_carrier', 'Water/foam carrier'), ('Wood_chip_transport', 'Wood chip transport')], max_length=55)),
                ('quantity', models.FloatField(verbose_name='quantity')),
                ('delivery_place', models.CharField(max_length=256, verbose_name='delivery place')),
                ('bodybuilder_crd', models.DateField(verbose_name='bodybuilder crd')),
                ('agreed_delivery_date', models.DateField(verbose_name='agreed delivery date')),
                ('order_security', models.FloatField(verbose_name='order security')),
                ('date', models.DateField(default=datetime.datetime(2018, 2, 7, 19, 4, 32, 841563, tzinfo=utc), verbose_name='date')),
                ('order_stock', models.CharField(choices=[('ORDER', 'Order'), ('STOCK', 'Stock')], max_length=5)),
                ('order_no', models.CharField(max_length=256, verbose_name='order no')),
                ('sport_distribution_order_id', models.CharField(max_length=40, verbose_name='sport/distributionOrderID')),
                ('salesman', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('is_capital', models.BooleanField(default=False, verbose_name='is capital city')),
                ('population', models.BigIntegerField(verbose_name='population')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='name')),
                ('area', models.BigIntegerField(help_text='km&#178;', verbose_name='area')),
                ('population', models.BigIntegerField(verbose_name='population')),
                ('population_density', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='population density')),
                ('longest_river', models.CharField(blank=True, max_length=250, null=True, verbose_name='longest river')),
                ('biggest_mountain', models.CharField(blank=True, max_length=250, null=True, verbose_name='biggest mountain')),
                ('hemisphere', models.CharField(choices=[('NORTH', 'North'), ('SOUTH', 'South'), ('BOTH', 'Both')], max_length=5)),
                ('biggest_city', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.City', verbose_name='biggest city')),
            ],
            options={
                'verbose_name': 'continent',
                'verbose_name_plural': 'continents',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('independence_day', models.DateField(blank=True, null=True, verbose_name='independence day')),
                ('gay_friendly', models.NullBooleanField(verbose_name='gay friendly')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='polls.Continent', verbose_name='continent')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('nav_cust_name', models.CharField(max_length=250, verbose_name='nav_cust_name')),
                ('nav_cust_search_name', models.CharField(max_length=250, verbose_name='nav_cust_search_name')),
                ('mds_cust_id', models.CharField(max_length=250, verbose_name='mds_cust_id')),
                ('nav_vat', models.CharField(blank=True, max_length=250, null=True, verbose_name='nav_vat')),
                ('source', models.CharField(max_length=3, verbose_name='source')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'ordering': ['nav_cust_name'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='code')),
                ('dept_name', models.CharField(max_length=40, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'db_table': 'departments',
                'ordering': ['dept_no'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False, verbose_name='employee number')),
                ('birth_date', models.DateField(verbose_name='birthday')),
                ('first_name', models.CharField(max_length=14, verbose_name='first name')),
                ('last_name', models.CharField(max_length=16, verbose_name='last name')),
                ('gender', models.CharField(max_length=1, verbose_name='gender')),
                ('hire_date', models.DateField(verbose_name='hire date')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Ocean',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='name')),
                ('area', models.BigIntegerField(verbose_name='area')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('map_url', models.URLField(verbose_name='map url')),
            ],
            options={
                'verbose_name': 'ocean',
                'verbose_name_plural': 'oceans',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Sea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('area', models.BigIntegerField(help_text='km&#178;', verbose_name='area')),
                ('avg_depth', models.IntegerField(blank=True, help_text='meters', null=True, verbose_name='average depth')),
                ('max_depth', models.IntegerField(blank=True, help_text='meters', null=True, verbose_name='maximum depth')),
                ('basin_countries', models.ManyToManyField(blank=True, related_name='seas', to='polls.Country')),
                ('ocean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Ocean', verbose_name='ocean')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Sea', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'sea',
                'verbose_name_plural': 'seas',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='continent',
            name='largest_country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='polls.Country', verbose_name='largest country'),
        ),
        migrations.AddField(
            model_name='continent',
            name='oceans',
            field=models.ManyToManyField(to='polls.Ocean', verbose_name='oceans'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='polls.Country', verbose_name='country'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'country')},
        ),
    ]
