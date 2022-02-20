from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from school_app import models

import json

def hello_world(request):
    return HttpResponse("Hello Jirkha 2")

@csrf_exempt
def list_subjects(request):
    if request.method == "GET":
        subjects = list(models.Subject.objects.values())
        return JsonResponse(subjects, safe=False, status=200)
    elif request.method == "POST":
        subject = request.body
        subject_dict = json.loads(subject)
        new_subject = models.Subject(**subject_dict)
        new_subject.save()
        return JsonResponse(subject_dict, status=200)
    else:
        return HttpResponseNotFound("No")

@csrf_exempt
def subject_detail(request, pk):
    global subjects
    subject=False
    try:
        subject = models.Subject.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"No subject id {pk}"}, status=404)

    if subject:       
        if request.method == "GET":
            return JsonResponse(model_to_dict(subject))
        elif request.method == "POST":
            new_subject_body = request.body
            new_subject = json.loads(new_subject_body)
            new_subject_index = subjects.index(subject)
            subjects[new_subject_index] = new_subject
            return JsonResponse(new_subject, status=201)
        elif request.method == "PUT":
            new_subject_body = request.body
            new_subject = json.loads(new_subject_body)
            subject.__dict__.update(new_subject)
            subject.save()
            #new_subject_index = subjects.index(subject)
            #if new_subject_index != pk:
            #    return HttpResponse(status=404)
            return JsonResponse(new_subject, status=201)
        elif request.method == "DELETE":
            subject.delete()
            return HttpResponse(status=204)