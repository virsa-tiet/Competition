
from django.http import HttpResponse
from django.shortcuts import redirect , render
from .models import Participant
from .forms import ParticipantForm
from django.contrib import messages
import csv
# Create your views here.
all_participants= Participant.objects.all
def home(request):
    return render(request , 'home.html' , {'all':all_participants})

# with open('meggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam','roll','phone','subit'])
#     m_feilds=all_participants.values_list('name','branch','email','roll','phone','subit')
#     for Participant in m_feilds:
#         spamwriter.writerow(Participant)
   
# with open('eggs.csv', 'w', newline='') as csvfile:
#     all_participants= Participant.objects.all
#     response=HttpResponse(content_type='text/csv')
    

#     writer=csv.writer(response)
#     writer.writerow(['Name','Branch','email','roll','phone','subit'])
#     # m_feilds=all_participants.value_list('name','branch','email','roll','phone','subit')
#     # for Participant in m_feilds:
#     writer.writerow('name')
    
    
def come(request):
    # all_participants= Participant.objects.all
    if request.method == "POST" :
        form= ParticipantForm(request.POST)
        
        if form.is_valid():
            form.save()
            # for Participant in all_participants:
            with open('participants.csv', 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                       
                    spamwriter.writerow(['name','branch','email','roll','phone','subit'])
                    m_feilds=all_participants.values_list('name','branch','email','roll','phone','subit')
                    for Participant in m_feilds:
                        spamwriter.writerow(Participant)      
        else :
            name = request.POST['name']
            branch = request.POST['branch']
            phone = request.POST['phone']
            roll = request.POST['roll']
            email = request.POST['email']
            subit = request.POST['subit']
            messages.success(request,('error'))
            # return redirect('come')
            return render(request , 'come.html' , { 'name':name,
             'branch':branch,
             'email' :email,
             'roll': roll,
              'phone':phone,
              'subit':subit
             
             })
        messages.success(request, ('submitted'))
        return render(request,'thankyou.html')
        # return redirect('thankyou.html')
    else :
         
        return render(request , 'come.html' , {})
