from ..models import CustomUser, KarmaObjection


class UserController:
    def __check_user_karma(self, user):
        if user.karma <= -3:
            return False

        return True

    def __valididate_user(self, user):
        if user.api_key == '' or user.api_key is None:
            user.set_api_key()

    def login_user(self, request):
        if request.POST.get('email', '') != '' and request.POST.get('password', '') != '':
            try:
                user = CustomUser.objects.get(email=request.POST.get('email'))
            except:
                return {
                    'status': 'failed',
                    'reason': 'couldn\'t find a user with this email'
                }

            if user.check_password(request.POST.get('password')):
                if self.__check_user_karma(user):
                    self.__valididate_user(user)
                    return user.serialize()
                else:
                    return {
                        'status': 'suspended',
                        'reason': 'This user has been suspended due to low karma, ' +
                                  'contact a site administrator to undo this action'
                    }
            else:
                return {
                    'status': 'failed',
                    'reason': 'User password couldn\'t be verified'
                }

    def create_user(self, request):
        if request.method == 'POST':
            try:
                user = CustomUser()
                uname = request.POST.get('username', '')
                pword = request.POST.get('password', '')
                mail = request.POST.get('email', '')
                if uname != '' and pword != '' and mail != '':
                    user = user.create(username=uname, password=pword, email=mail)
                    self.__valididate_user(user)

                    status = {
                        'status': 'success'
                    }
                else:
                    status = {
                        'status': 'failed',
                        'reason': 'need username password and email'
                    }
            except:
                status = {
                    'status': 'failed',
                    'reason': 'user couldn\'t be created'
                }
        else:
            status = {
                'status': 'failed',
                'reason': 'only method POST is allowed'
            }

        return status

    def object_negitive_karma(self, request, user_id):
        try:
            objection = KarmaObjection()
            objection.user = CustomUser.objects.get(id=user_id)
            objection.reason = request.POST.get('reason', '')
            objection.save()
            return {
                'status': 'success'
            }
        except:
            return {
                'status': 'failed',
                'reason': 'couldn\'t create objection'
            }

