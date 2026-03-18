from django.contrib import admin # type: ignore

from . models import OHEntry

import data_wizard # type: ignore

admin.site.register(OHEntry)

data_wizard.register(OHEntry)
