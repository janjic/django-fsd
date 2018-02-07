from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


@python_2_unicode_compatible
class Department(models.Model):
    dept_no = models.CharField(_('code'), primary_key=True, max_length=4)
    dept_name = models.CharField(_('name'), unique=True, max_length=40)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        db_table = 'departments'
        ordering = ['dept_no']

    def __str__(self):
        return self.dept_name


@python_2_unicode_compatible
class Employee(models.Model):
    emp_no = models.IntegerField(_('employee number'), primary_key=True)
    birth_date = models.DateField(_('birthday'))
    first_name = models.CharField(_('first name'), max_length=14)
    last_name = models.CharField(_('last name'), max_length=16)
    gender = models.CharField(_('gender'), max_length=1)
    hire_date = models.DateField(_('hire date'))

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employees'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


@python_2_unicode_compatible
class Ocean(models.Model):
    name = models.CharField(_('name'), max_length=250, primary_key=True)
    area = models.BigIntegerField(_('area'))
    slug = models.SlugField(_('slug'))
    description = models.TextField(_('description'))
    map_url = models.URLField(_('map url'))

    class Meta:
        verbose_name = _('ocean')
        verbose_name_plural = _('oceans')
        ordering = ['name']

    def __str__(self):
        return self.name if self.name is not None else 'Ocean'


@python_2_unicode_compatible
class Sea(models.Model):
    name = models.CharField(_('name'), max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'))
    ocean = models.ForeignKey(Ocean, on_delete=models.CASCADE, verbose_name=_('ocean'))

    area = models.BigIntegerField(_('area'), help_text=mark_safe(_('km&#178;')))
    avg_depth = models.IntegerField(_('average depth'), help_text=_('meters'), null=True, blank=True)
    max_depth = models.IntegerField(_('maximum depth'), help_text=_('meters'), null=True, blank=True)

    basin_countries = models.ManyToManyField(
        'Country', related_name='seas', blank=True)

    def get_parent_id_display(self):
        return self.parent

    class Meta:
        verbose_name = _('sea')
        verbose_name_plural = _('seas')
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Continent(models.Model):
    name = models.CharField(_('name'), max_length=250, primary_key=True)
    area = models.BigIntegerField(_('area'), help_text=mark_safe('km&#178;'))
    population = models.BigIntegerField(_('population'))
    population_density = models.DecimalField(_('population density'), decimal_places=2, max_digits=8)

    largest_country = models.OneToOneField(
        'Country', on_delete=models.CASCADE, related_name='+', blank=True, null=True, verbose_name=_('largest country'))
    biggest_city = models.OneToOneField(
        'City', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('biggest city'))
    longest_river = models.CharField(_('longest river'), max_length=250, blank=True, null=True)
    biggest_mountain = models.CharField(_('biggest mountain'), max_length=250, blank=True, null=True)

    oceans = models.ManyToManyField(Ocean, verbose_name=_('oceans'))
    hemisphere = models.CharField(
        max_length=5, choices=(
            ('NORTH', 'North'),
            ('SOUTH', 'South'),
            ('BOTH', 'Both')))

    def __str__(self):
        return self.name if self.name is not None else 'Continent'

    class Meta:
        verbose_name = _('continent')
        verbose_name_plural = _('continents')
        ordering = ['name']

    def countries_count(self):
        return self.countries.count()
    countries_count.short_description = _('countries count')


@python_2_unicode_compatible
class Country(models.Model):
    code = models.CharField(_('code'), max_length=3, unique=True)
    name = models.CharField(_('name'), max_length=250)
    independence_day = models.DateField(_('independence day'), null=True, blank=True)
    gay_friendly = models.NullBooleanField(_('gay friendly'))
    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, null=True, related_name='countries', verbose_name=_('continent'))

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(_('name'), max_length=250)
    is_capital = models.BooleanField(_('is capital city'), default=False)
    population = models.BigIntegerField(_('population'))
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='cities', verbose_name=_('country'))

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        unique_together = ('name', 'country')
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=50, unique=True)
    nav_cust_name = models.CharField(_('nav_cust_name'), max_length=250)
    nav_cust_search_name = models.CharField(_('nav_cust_search_name'), max_length=250)
    mds_cust_id = models.CharField(_('mds_cust_id'), max_length=250)
    nav_vat = models.CharField(_('nav_vat'), max_length=250, null=True, blank=True)
    source = models.CharField(_('source'), max_length=3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        ordering = ['nav_cust_name']

    def __str__(self):
        return self.nav_cust_name

    @staticmethod
    def autocomplete_search_fields():
        return 'nav_cust_name', 'nav_cust_search_name'

