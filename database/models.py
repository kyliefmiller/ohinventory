from django.db import models
from django.utils.translation import gettext_lazy as _

class OHEntry(models.Model):
    class Institution(models.TextChoices):
        ANIMASMUSEUM = "Animas Museum", _("Animas Museum")
        CENTEROFSWSTUDIES = "Center of Southwest Studies", _("Center of Southwest Studies")
        COLORADOSTATEUNIVERSITY = "Colorado State University", _("Colorado State University")
        DENVERPUBLICLIBRARY = "Denver Public Library", _("Denver Public Library")
        DOLORESPUBLICLIBRARY = "Dolores Public Library", _("Dolores Public Library")
        DURANGONATIVESTORIES = "Durango Native Stories", _("Durango Native Stories")
        DURANGOPUBLICLIBRARY = "Durango Public Library", _("Durango Public Library")
        FORTLEWISMESALIBRARY = "Fort Lewis Mesa Library", _("Fort Lewis Mesa Library")
        HINSDALECOUNTYHISTORICALSOCIETY = "Hinsdale County Historical Society", _("Hinsdale County Historical Society")
        HISTORYCOLORADO = "History Colorado", _("History Colorado")
        IGNACIOLIBRARY = "Ignacio Library", _("Ignacio Library")
        KVNF = "KVNF", _("KVNF")
        MANCOSPUBLICLIBRARY = "Mancos Public Library", _("Mancos Public Library")
        OURAYCOUNTYRANCHHISTORYMUSEUM = "Ouray County Ranch History Museum", _("Ouray County Ranch History Museum")
        PINERIVERPUBLICLIBRARY = "Pine River Public Library", _("Pine River Public Library")
        RIDGWAYPUBLICLIBRARY = "Ridgway Public Library", _("Ridgway Public Library")
        SANJUANCOUNTYHISTORICALSOCIETY = "San Juan County Historical Society", _("San Juan County Historical Society")
        TELLURIDEHISTORICALMUSEUM = "Telluride Historical Museum", _("Telluride Historical Museum")
        WILKINSONPUBLICLIBRARY = "Wilkinson Public Library", _("Wilkinson Public Library")
        
        
    institution = models.CharField(max_length=100, choices=Institution)  
    medium = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    month = models.CharField(max_length=1000, null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    narrator = models.CharField(max_length=100, null=True, blank=True)
    creator = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    topic = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000000, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)

