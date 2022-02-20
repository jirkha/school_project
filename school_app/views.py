from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from school_app import models

import json

def hello_world(request):
    return HttpResponse("Hello Jirkha 2")

# Subject
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
    subject=False
    try:
        subject = models.Subject.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"No subject id {pk}"}, status=404)

    if subject:       
        if request.method == "GET":
            return JsonResponse(model_to_dict(subject))
        elif request.method == "PUT":
            new_subject_body = request.body
            new_subject = json.loads(new_subject_body)
            subject.__dict__.update(new_subject)
            subject.save()
            return JsonResponse(new_subject, status=201)
        elif request.method == "DELETE":
            subject.delete()
            return HttpResponse(status=204)

# Teacher
@csrf_exempt
def list_teachers(request):
    if request.method == "GET":
        teachers = list(models.Teacher.objects.values())
        return JsonResponse(teachers, safe=False, status=200)
    elif request.method == "POST":
        teacher = request.body
        teacher_dict = json.loads(teacher)
        new_teacher = models.Teacher(**teacher_dict)
        new_teacher.save()
        return JsonResponse(teacher_dict, status=200)
    else:
        return HttpResponseNotFound("No")


@csrf_exempt
def teacher_detail(request, pk):
    teacher = False
    try:
        teacher = models.Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"No teacher id {pk}"}, status=404)

    if teacher:
        if request.method == "GET":
            return JsonResponse(model_to_dict(teacher))
        elif request.method == "PUT":
            new_teacher_body = request.body
            new_teacher = json.loads(new_teacher_body)
            teacher.__dict__.update(new_teacher)
            teacher.save()
            return JsonResponse(new_teacher, status=201)
        elif request.method == "DELETE":
            teacher.delete()
            return HttpResponse(status=204)
