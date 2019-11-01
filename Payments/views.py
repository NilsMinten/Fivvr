from django.shortcuts import render
from .Controllers.PaymentController import PaymentController
from django.http import JsonResponse
paymentController = PaymentController()


def create_payment_for_service(request, service_id):
    result = paymentController.create_payement_for_service(request, service_id)
    return JsonResponse(result)


def service_cancel(request, payment_id):
    result = paymentController.service_cancel(request, payment_id)
    return JsonResponse(result)


def check_service_payed(request, payment_id):
    result = paymentController.check_service_payed(payment_id)
    return JsonResponse(result)
