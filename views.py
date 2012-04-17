from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import datetime, random, sha
from django.core.mail import send_mail
from obieconnect.models import UserProfile
from obieconnect.forms import RegistrationForm

from obieconnect.models import ObieConnectProfile, Course, Department, Professor

# If user is logged in, take to personal profile
# Else display login form AND link to registration form

# registration form

def register(request):
    if request.user.is_authenticated():
        # They already have an account; don't let them register again
        return render_to_response('register.html', {'has_account': True})
    manipulator = RegistrationForm()
    if request.POST:
        new_data = request.POST.copy()
        errors = manipulator.get_validation_errors(new_data)
        if not errors:
            # Save the user                                                                                                                                                 
            manipulator.do_html2python(new_data)
            new_user = manipulator.save(new_data)
            
            # Build the activation key for their account                                                                                                                    
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+new_user.username).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            # Create and save their profile                                                                                                                                 
            new_profile = UserProfile(user=new_user,
                                      activation_key=activation_key,
                                      key_expires=key_expires)
            new_profile.save()
            
            # Send an email with the confirmation link                                                                                                                      
            email_subject = 'Your new example.com account confirmation'
            email_body = "Hello, %s, and thanks for signing up for an ObieConnect account!\n\nTo activate your account, click this link within 48 \hours:\n\nhttp://obieconnect.com/accounts/confirm/%s" % (
                new_user.username,
                new_profile.activation_key)
            send_mail(email_subject,
                      email_body,
                      'accounts@example.com',
                      [new_user.email])
            
            return render_to_response('register.html', {'created': True})
    else:
        errors = new_data = {}
    form = forms.FormWrapper(manipulator, new_data, errors)
    return render_to_response('register.html', {'form': form})

# Department view 

# Professor view

# Course page view
    # Comments
    # Include list of users?

