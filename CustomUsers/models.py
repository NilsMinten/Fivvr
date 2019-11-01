from django.contrib.auth.models import AbstractUser
from django.db import models
import string
import random


class CustomUser(AbstractUser):
    karma = models.IntegerField(null=True)
    api_key = models.TextField(null=True)
    pass

    def __str__(self):
        return self.email

    def set_api_key(self):
        letters = string.hexdigits
        self.api_key = ''.join(random.choice(letters) for i in range(25))

    def is_admin(self):
        return self.groups.filter(name__in=['Admin']).exists()

    def create(self, username, password, email):
        self.set_api_key()
        self.username = username
        self.email = email
        self.set_password(password)
        self.karma = 0
        self.save()
        self.groups.set([2])
        self.save()

    def serialize(self):
        if self.is_admin():
            group = 'admin'
        else:
            group = 'member'

        return {
            'username': self.username,
            'email': self.email,
            'api': self.api_key,
            'karma': self.karma,
            'group': group
        }

    def add_karma(self):
        self.karma += 1
        self.save()

    def substract_karma(self):
        self.karma -= 1
        self.save()


class KarmaObjection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    reason = models.TextField()
    accepted = models.NullBooleanField(default=None)

    def __str__(self):
        return self.reason

    def accept_objection(self):
        self.accepted = True
        self.save()

    def deny_objection(self):
        self.accepted = False
        self.save()

    def serialize(self):
        return {
            'objection_id': self.id,
            'user_id': self.user.id,
            'reason': self.reason,
            'accepted': self.accepted
        }
