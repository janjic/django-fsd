from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from material.frontend.apps import ModuleMixin


class PollsConfig(ModuleMixin, AppConfig):
    name = 'polls'
    icon = '<i class="material-icons">extension</i>'
    verbose_name = _("CRUD sample")

    def has_perm(self, user):
        return user.is_superuser



