from django.db import models
from CustomUsers.models import CustomUser
from Services.models import Service


class Payment(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender_user')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver_user')
    post = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, default='processing')
    userFeedback = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.post.__str__() + ' | status: ' + self.status

    def setStatus(self, new_status):
        self.status = new_status
        self.save()
