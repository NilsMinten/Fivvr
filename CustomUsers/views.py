from .Controllers.UserController import UserController
from .Controllers.KarmaObjectionController import KarmaObjectionController
from django.http import JsonResponse

user_controller = UserController()
karma_objections_controller = KarmaObjectionController()


def create_user(request):
    status = user_controller.create_user(request)
    return JsonResponse(status)


def login_user(request):
    status = user_controller.login_user(request)
    return JsonResponse(status)


def object_karma(request, user_id):
    status = user_controller.object_negitive_karma(request, user_id)
    return JsonResponse(status)


def admin_view_karma_objections(request, user_id):
    status = karma_objections_controller.view_karma_objections(user_id, request)
    return JsonResponse(status)


def admin_approve_karma_objection(request, objection_id):
    status = karma_objections_controller.accept_karma_objection(objection_id, request)
    return JsonResponse(status)


def admin_deny_karma_objection(request, objection_id):
    status = karma_objections_controller.deny_karma_objection(objection_id, request)
    return JsonResponse(status)
