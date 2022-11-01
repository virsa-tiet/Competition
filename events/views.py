
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
    
    if request.method == "POST" :
        # form= ParticipantForm(request.POST)
        name = request.POST['name']
        branch = request.POST['branch']
        phone = request.POST['phone']
        roll = request.POST['roll']
        email = request.POST['email']
        subit = request.POST['subit']
        data=Participant.objects.create(
        name=name,
        branch=branch,
        email =email,
        roll= roll,
        phone=phone,
        subit=subit
        )
        data.save()
        with open('participants1.csv', 'a', newline='') as csvfile:
                    # spamwriter = csv.writer(csvfile, delimiter=' ',
                    #         quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    # spamwriter.writerow(['name','branch','email','roll','phone','subit'])  
                    spamwriter= csv.writer(csvfile)
                    data1=[name,branch,email,roll,phone,subit]
                    spamwriter.writerow(data1) 
        
        return render(request,'thankyou.html')     
    return render(request , 'come.html')



















# data=Participant.objects.create(
        # name=name,
        # branch=branch,
        # email =email,
        # roll= roll,
        # phone=phone,
        # subit=subit
        # )
        # data.save()
        # form.save()



# context={ 'name':name,
        #      'branch':branch,
        #      'email' :email,
        #      'roll': roll,
        #       'phone':phone,
        #       'subit':subit
        #      }




  
        # if form.is_valid():
        #     form.save()
            
        #     with open('participants.csv', 'w', newline='') as csvfile:
        #             spamwriter = csv.writer(csvfile, delimiter=' ',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
                       
        #             spamwriter.writerow(['name','branch','email','roll','phone','subit'])
        #             m_feilds=all_participants.values_list('name','branch','email','roll','phone','subit')
        #             for Participant in m_feilds:
        #                 spamwriter.writerow(Participant)      
        