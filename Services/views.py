from django.http import JsonResponse
from .Controllers.ServiceController import ServiceController

service_controller = ServiceController()


def load_services(request):
    services = service_controller.load_all_services(request)
    return JsonResponse(services, safe=False)


def create_service(request):
    status = service_controller.create_service(request)
    return JsonResponse(status)


def delete_service(request, service_id):
    status = service_controller.delete_service(request, service_id)
    return JsonResponse(status)


def edit_service(request, service_id):
    status = service_controller.edit_service(request, service_id)
    return JsonResponse(status)


def load_service(request, service_id):
    service = service_controller.view_service(request, service_id)
    return JsonResponse(service)


def upvote_service(request, service_id):
    status = service_controller.like_service(service_id)
    return JsonResponse(status)


def buy_service(request, service_id):
    status = service_controller.buy_service(request, service_id)
    return JsonResponse(status)


def cancel_service(request, service_id):
    status = service_controller.cancel_service(request, service_id)
    return JsonResponse(status)
