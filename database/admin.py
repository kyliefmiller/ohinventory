from django.contrib import admin

from . models import OHEntry

import data_wizard

admin.site.register(OHEntry)

data_wizard.register(OHEntry)
