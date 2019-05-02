from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.shortcuts import render
from .models import Message
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def Home(request):
    context = locals()
    template = 'index.html'
    return render(request, template, context)


def About(request):
    context = locals()
    template = 'app/about.html'
    return render(request, template, context)


def Contact(request):
    context = locals()
    template = 'app/contact.html'
    return render(request, template, context)


@login_required
def user(request):
    form_1 = forms.LocationForm(request.POST or None)

    if form_1.is_valid():
        instance = form_1.save(commit=False)
        instance.user = request.user
        instance.save()
        form_1 = None

    context = {'form_1': form_1}
    template = 'app/user.html'
    return render(request, template, context)


@login_required
def feedback(request):
    title = 'Message'
    form = forms.CreateForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        title = "Thanks!!"
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'app/feedback.html'
    return render(request, template, context)





def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


# # Simple API  JSON Responce
# def Location_list(request):
#     MAX_OBJECTS = 20
#     polls = Location.objects.all()[:MAX_OBJECTS]
#     data = {"results": list(polls.values("location", "user", "date"))}
#     return JsonResponse(data)
#
#
# def Message_list(request):
#     MAX_OBJECTS = 20
#     polls = Message.objects.all()[:MAX_OBJECTS]
#     data = {"results": list(polls.values("username", "email", "message", "date"))}
#     return JsonResponse(data)
