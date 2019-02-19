import datetime
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Ticket
from .forms import TicketForms
def helpindex(request):
    return render(request,'helpme.html')


def new_help_request(request):
    #ticket_instance = get_object_or_404(Ticket, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        ticket_form = TicketForms(request.POST)

        # Check if the form is valid:
        if ticket_form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_instance.due_back = book_renewal_form.cleaned_data['renewal_date']
            topic = ticket_form.save(commit=False)	
            topic.save()
			# redirect to a new URL:
            return redirect('help_index')

    # If this is a GET (or any other method) create the default form.
    else:
        ticket_form = TicketForms()

    context = {
        'form': ticket_form,
        #'book_instance': ticket_instance,
    }

    return render(request, 'newrequest.html', context)