# Generated by Django 2.0.2 on 2018-02-06 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=10, verbose_name='customer_id')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('search_name', models.CharField(max_length=250, verbose_name='search_name')),
                ('mds_customer_id', models.CharField(max_length=250, verbose_name='mds_customer_id')),
                ('nav_vat', models.CharField(max_length=250, verbose_name='nav_vat')),
                ('source', models.CharField(max_length=3, verbose_name='source')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'ordering': ['name'],
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
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]