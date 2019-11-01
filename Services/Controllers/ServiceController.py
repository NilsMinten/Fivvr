from ..models import Service
from CustomUsers.models import CustomUser
from Payments.Controllers.PaymentController import PaymentController


class ServiceController:
    def __verify_service(self, service):
        if service.title == '':
            return False
        if service.description == '':
            return False
        if service.cost == 0:
            return False

        return True

    def __update_service(self, service, request):
        service.title = request.POST.get('title', '')
        service.description = request.POST.get('description', '')
        service.cost = int(request.POST.get('cost', ''))

        return service

    def load_all_services(self, request):
        services = Service.objects.all().order_by('-created')
        services_serialized = []
        try:
            if CustomUser.objects.get(api_key=request.POST.get('api', '')).is_admin():
                paymentController = PaymentController()
                for service in services:
                    services_serialized.append(service.serialize_admin(paymentController.get_payments_for_service(service.id)))
            else:
                for service in services:
                    services_serialized.append(service.serialize_user())
        except:
            for service in services:
                services_serialized.append(service.serialize_user())

        return services_serialized

    def create_service(self, request):
        service = Service()
        service.author = CustomUser.objects.get(api_key=request.POST.get('api', ''))
        self.__update_service(service, request)

        if self.__verify_service(service):
            service.save()
            result = {
                'status': 'success',
            }
        else:
            result = {
                'status': 'failed',
                'reason': 'not all data filled in'
            }

        return result

    def delete_service(self, request, service_id):
        service = Service.objects.get(id=service_id)
        requesting_user = CustomUser.objects.get(api_key=request.POST.get('api', ''))

        if service.author == requesting_user or requesting_user.is_admin():
            service.delete()
            result = {
                'status':  'success'
            }
        else:
            result = {
                'status': 'failed',
                'reason': 'user not allowed delete this post'
            }

        return result

    def edit_service(self, request, service_id):
        service = Service.objects.get(id=service_id)
        requesting_user = CustomUser.objects.get(api_key=request.POST.get('api', ''))

        if service.author == requesting_user or requesting_user.is_admin():
            self.__update_service(service, request)

            if self.__verify_service(service):
                service.save()
                result = {
                    'status': 'success',
                }
            else:
                result = {
                    'status': 'failed',
                    'reason': 'not all data filled in'
                }
        else:
            result = {
                'status': 'failed',
                'reason': 'user not allowed to edit service'
            }

        return result

    def view_service(self, request, service_id):
        service = Service.objects.get(id=service_id)
        service.views += 1
        service.save()
        try:
            requesting_user = CustomUser.objects.get(api_key=request.POST.get('api', ''))
            paymentController = PaymentController()

            if service.author == requesting_user or requesting_user.is_admin():
                return service.serialize_admin(paymentController.get_payments_for_service(service.id), requesting_user)
        except:
            return service.serialize_user()

        return service.serialize_user()

    def like_service(self, service_id):
        service = Service.objects.get(id=service_id)
        service.upvotes += 1
        service.save()

        return service.serialize_user()

    def buy_service(self, request, service_id):
        return {
            'status': 'failed',
            'reason': 'method not yet implemented'
        }

    def cancel_service(self, request, service_id):
        return {
            'status': 'failed',
            'reason': 'method not yet implemented'
        }
