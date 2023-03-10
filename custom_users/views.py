from django.db import IntegrityError
from django.http import HttpResponse
from django.template import loader
from rest_framework import views, response, status
from django.shortcuts import render
import bcrypt
import time

from custom_users.models import CustomUser
from custom_users.tasks import send_welcome_emails_to_new_users
from services.ses import SESService


def handler500(request, *args, **kwargs):
    template = loader.get_template('default_500.html')
    response.status_code = 500
    return HttpResponse(template.rener({"name": "Ines"}, request), status=500)

# def get_single_user():
#     return render()


class GetCreateUsers(views.APIView):
    def get(self, request):
        return response.Response({"message": "ok"})

    def post(self, request):
        user = CustomUser(**request.data)
        context = {"name": "Ines"}
        template = loader.get_template('index.html')
        # password = bcrypt.hashpw(request.data["password"], "123456")
        try:
            user.save()
        except IntegrityError as ex:
            template = loader.get_template('default_500.html')
            context = {}
        # TODO: send an email
        # send_welcome_emails_to_new_users.delay()
        SESService().send_email(user.email)
        return HttpResponse(template.rener(context, request))

        # except IntegrityError as ex:
        #     return response.Response({"message": "email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        # return response.Response({"message": "ok"})



class GetUpdateDeleteUser(views.APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass