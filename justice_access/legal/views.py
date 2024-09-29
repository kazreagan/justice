import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import LegalInformation, LegalAid, CourtCase, LegalTopic, LegalAidRequest
from .forms import LegalAidRequestForm

#view for home page
def home(request):
    return render(request, 'home.html')

#view for list of topics
def legal_info_list(request):
    topics = LegalTopic.objects.all()
    return render(request, 'legal/legal_info_list.html', {'topics': topics})

#view for legal information portal
def legal_information(request):
    info = LegalInformation.objects.all()
    return render(request, 'legal/legal_information.html', {'info': info})

#view for legal aid organizations
def legal_aid(request):
    aid_orgs = LegalAid.objects.all()
    return render(request, 'legal/legal_aid.html', {'aid_orgs': aid_orgs})

#view for case tracking
def track_case(request):
    cases = CourtCase.objects.filter(user=request.user)
    return render(request, 'legal/track_case.html', {'cases': cases})

#view for content of a single topic
def legal_info_detail(request, topic_id):
    topic = get_object_or_404(LegalTopic, id=topic_id)
    return render(request, 'legal/legal_info_detail.html', {'topic': topic})

#set up logging
logger = logging.getLogger(__name__)

#view to handle form submission
def request_legal_aid(request):
    if request.method == 'POST':
        form = LegalAidRequestForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Legal aid request submmitted: %s', form.cleaned_data) #log the data
            return redirect('legal_aid_thanks')
        else:
            logger.error('Invalid form submission: %s', form.errors) #log errors    
    else:
        form = LegalAidRequestForm()
    
    return render(request, 'legal/request_legal_aid.html', {'form': form})
    
def legal_aid_thanks(request):
    return render(request, 'legal/legal_aid_thanks.html')

#view to display court case progress
def case_tracking(request):
    cases = CourtCase.objects.all()
    return render(request, 'legal/case_tracking.html', {'case': cases})

#view to display all submitted forms on a separate page
def view_requests(request):
    requests = LegalAidRequest.objects.all() #to fetch all requests
    return render(request, 'legal/view_requests.html', {'requests': requests})