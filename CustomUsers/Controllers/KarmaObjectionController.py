from ..models import KarmaObjection, CustomUser


class KarmaObjectionController:
    def view_karma_objections(self, user_id, request):
        if not CustomUser.objects.get(api_key=request.POST.get('api')).is_admin():
            return {
                'status': 'failed',
                'reason': 'user is not admin'
            }

        objections = KarmaObjection.objects.filter(user=CustomUser.objects.get(id=user_id))

        serialized_objections = []
        try:
            for objection in objections:
                serialized_objections.append(objection.serialize())
        except:
            serialized_objections = []

        return serialized_objections

    def accept_karma_objection(self, objection_id, request):
        if not CustomUser.objects.get(api_key=request.POST.get('api')).is_admin():
            return {
                'status': 'failed',
                'reason': 'user is not admin'
            }

        objection = KarmaObjection.objects.get(id=objection_id)
        objection.user.substract_karma()
        objection.accept_objection()

        return {
            'status': 'success'
        }

    def deny_karma_objection(self, objection_id, request):
        if not CustomUser.objects.get(api_key=request.POST.get('api')).is_admin():
            return {
                'status': 'failed',
                'reason': 'user is not admin'
            }

        objection = KarmaObjection.objects.get(id=objection_id)
        objection.user.add_karma()
        objection.deny_objection()
