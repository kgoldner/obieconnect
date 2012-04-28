from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

from bootstrap.forms import ExampleForm, AjaxAutoComplete, PopoverForm
from bootstrap.models import Course

def home(request):
    context = {}
    context.update(csrf(request))
    context["user"] = request.user
    context["hero_title"] = "Welcome to ObieConnect"
    return render_to_response("bootstrap/home.html", context)

def directory(request):
    context = {}
    context["user"]=request.user
    context["hero_title"]="Directory"
    courses = Course.objects.all()
    context["courses"]=courses;
    return render_to_response("bootstrap/directory.html", context)

def course_detail(request):
    context = {}
    context["course_id"]=request.course_id
    context["user"]=request.user
    context["hero_title"]=Course.objects.get(id=course_id)  


def ajax_form(request):
    context = {}
    context["form"] = ExampleForm()
    context["user"] = request.user
    context["hero_title"] = "Register"
    context.update(csrf(request))
    return render_to_response("bootstrap/example.html", context)


def ajax_example(request):
    context = {}
    if request.POST:
        form = ExampleForm(request.POST)
        if form.is_valid():
            #Do Something, e.g. save, send an email
            template = "bootstrap/example_form_success.html"
            success = True
        else:
            template = "bootstrap/example_form.html"
            context["form"] = form
            success = False
    else:
        template = "bootstrap/example_form.html"
        context["form"] = ExampleForm()
        success = False
    html = render_to_string(template, context)
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")    


def modal_dialog(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Modal Dialog"
    context.update(csrf(request))
    return render_to_response("bootstrap/modal/modal_dialog.html", context)


def text_modal_dialog(request):
    if request.POST.get('id', False):
        # String provided for ease of demonstration
        # Replace with model lookup, e.g. 
        # wording = User.objects.get(id=request.POST.get('id', False))
        wording = "ABC"
    else:
        wording = False
    template = "bootstrap/modal/modal_dialog_text.html"
    html = render_to_string(template, {"wording": wording})
    response = simplejson.dumps({"html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")
                                                    

def ajax_autocomplete(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Find a Class"
    context["form"] = AjaxAutoComplete()
    context.update(csrf(request))
    return render_to_response("bootstrap/autocomplete/autocomplete.html", context)


def ajax_autocomplete_lookup(request):
    results = []
    if request.GET.has_key("term"):
        value = request.GET[u'term']
        courses = Course.objects.filter(name__icontains=value)
        for course in courses:
            course_dict = {}
            course_dict["id"] = course.id
            course_dict["label"] = course.name
            results.append(course_dict)   
    response = simplejson.dumps(results)
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")


def ajax_autocomplete_get_selected_item(request):
    course_id = request.POST.get("course_id", False)
    if course_id:
        try:
            course = Course.objects.get(id=course_id)
        except Courses.DoesNotExist:
            course = None
    else:
        course = None
    template = "bootstrap/autocomplete/select_result.html"
    html = render_to_string(template, {"course": course})
    response = simplejson.dumps({"html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")
                            
                            
def popover(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Popovers"
    context["form"] = PopoverForm()
    context.update(csrf(request))
    return render_to_response("bootstrap/popover/popover.html", context)


def geolocation(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Geolocation"
    context.update(csrf(request))
    return render_to_response("bootstrap/geolocation/geolocation.html", context)
    
    
@login_required
def inside(request):
    context = {}
    context["user"] = request.user
    return render_to_response("bootstrap/inside.html", context)

