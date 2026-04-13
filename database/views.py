from django.shortcuts import render # type: ignore
from django.db.models import Q # type: ignore
import re

from .models import OHEntry

def entry_list(request):
    entries = OHEntry.objects.all()

    #def category_list(category):
        #category_choices = set()
        #for entry in entries:
            #category_choices.add(entry.__getattribute__(category).strip())
        #category_choices = sorted(list(category_choices))
        #return category_choices

    #institution_choices = category_list('institution')
    ##institution
    institution_choices = set()
    for entry in entries:
        institution_choices.add(entry.institution.strip())
    institution_choices = sorted(list(institution_choices))

    ##medium
    medium_choices = set()
    for entry in entries:
        for medium in entry.medium.split(","):
            medium_choices.add(medium.strip())
    medium_choices = sorted(list(medium_choices))

    ##access
    access_choices = set()
    for entry in entries:
        for access in entry.access.split(","):
            access_choices.add(access.strip())
    access_choices = sorted(list(access_choices))

    ##location
    location_choices = set()
    for entry in entries:
        if entry.location != None:
            for location in entry.location.split(","):
                location_choices.add(location.strip())
    location_choices = sorted(list(location_choices))
    location_choices = ['Archuleta County', 'Bayfield', 'Cortez', 'Dolores', 'Dolores County', 'Dove Creek',
                        'Durango', 'Hesperus', 'Hinsdale County', 'Ignacio', 'La Plata County',
                        'Lake City', 'Mancos', 'Montezuma County', 'Ophir', 'Ouray', 'Ouray County', 'Pagosa Springs',
                        'Pandora',' Placerville', 'Rico', 'Ridgway', 'San Juan County', 'San Miguel County',
                         'Silverton', 'Southern Ute Reservation', 'Telluride', 'Towaoc', 'Ute Mountain Ute Reservation' ]
    
    ##topic
    topic_choices = set()
    for entry in entries:
        if entry.topic != None:
            for topic in entry.topic.split(","):
                topic_choices.add(topic.strip())
    topic_choices = sorted(list(topic_choices)) 

    ##link 
    

    result_filter = Q()
    if "Institution" in request.GET and request.GET["Institution"] != "":
        institution_filter = Q()
        for institution in request.GET.getlist("Institution"):
            if "_" in institution:
                institution = institution.replace("_", " ")
            institution_filter = institution_filter | Q(institution__icontains=institution)
        result_filter = institution_filter

    if "Medium" in request.GET and request.GET["Medium"] != "":
        medium_filter = Q()
        for medium in request.GET.getlist("Medium"):
            medium_filter = medium_filter | Q(medium__icontains=medium)
        result_filter = medium_filter & result_filter

    if "Access" in request.GET and request.GET["Access"] != "":
        print(request.GET)
        access = request.GET["Access"]
        access_filter = Q()
        if "_" in access:
            access = access.replace("_", " ")
            print(access)
        if access=="exclude":
            access_filter= ~Q(access__icontains="Restricted") & ~Q(access__icontains="Low Quality")
            print(access_filter)
        else:
            access_filter = Q(access__icontains=access)
        result_filter = access_filter & result_filter
    
    if "Narrator" in request.GET and request.GET["Narrator"] != "":
        result_filter = Q(narrator__icontains=request.GET.get("Narrator")) & result_filter

    if "Start Year" in request.GET and "End Year" in request.GET:

        if request.GET["Start Year"] == "" and request.GET["End Year"] == "":
            result_filter = result_filter
    
        if request.GET["Start Year"] != "" or request.GET["End Year"] != "":
            if request.GET["Start Year"] == "":
                start_year = 0
            else:
                start_year = request.GET.get("Start Year") 
            if request.GET["End Year"] == "":
                end_year = 3000 
            else:
                end_year = request.GET.get("End Year")
            result_filter = Q(year__range=(start_year, end_year))

    if "Location" in request.GET and request.GET["Location"] != "":
        location_filter = Q()
        for location in request.GET.getlist("Location"):
            if "_" in location:
                location = location.replace("_", " ")

            location_filter = location_filter | Q(location__icontains=location)

        result_filter = location_filter & result_filter  
    
    if "Topic" in request.GET and request.GET["Topic"] != "":
        topic_filter = Q()
        for topic in request.GET.getlist("Topic"):
            if "_" in topic:
                topic = topic.replace("_", " ")

            topic_filter = topic_filter | Q(topic__icontains=topic)

        result_filter = topic_filter & result_filter 
    
    if "Description" in request.GET and request.GET["Description"] != "":
        result_filter = Q(description__icontains=request.GET.get("Description")) & result_filter
    
    result = entries.filter(result_filter)


    ##entry_filter = EntryFilter(request.GET, queryset=entries)

    return render(request, 'entries.html', {'institution_choices': institution_choices, 'medium_choices': medium_choices,
                                            'access_choices': access_choices, 
                                            'location_choices': location_choices, 'topic_choices': topic_choices, 
                                            'result': result})

def single_entry(request, id=None):
    single = OHEntry.objects.get(pk=id)
    updatedtext = ""
    if single.link != "" and single.link != None:
        updatedtext = single.link
        if ";" in single.link:
            updatedtext = updatedtext.replace(";", " - ")
        linktext = re.findall(r'(https?://[^\s]+)', updatedtext)
        for link in linktext:
            updatedtext = updatedtext.replace(link, f"<a href= \"{link}\" target=\"_blank\" style=\"color: blue;\"> {link} </a>")
            
            ##index = updatedtext.find(link)
            ##updatedtext = updatedtext[:index] + f"<a href= \"{link}\"> {link} </a>" + updatedtext[index:]
        ##linktext = re.search(r'(https?://[^\s]+)', single.link)
    print(updatedtext)
    return render(request, 'single-entry.html', {'entry': OHEntry.objects.get(pk=id), 'updatedtext' : updatedtext}) 

def home_page(request):
    return render(request, 'home-page.html')

def howto_page(request):
    return render(request, 'howto.html')

def about_page(request):
    return render(request, 'about.html')

def takepart_page(request):
    return render(request, 'take-part.html')