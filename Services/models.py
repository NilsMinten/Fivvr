from django.db import models
from django.utils import timezone
from CustomUsers.models import CustomUser


class Service(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(max_length=10000)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cost = models.IntegerField(default="0")
    upvotes = models.IntegerField(default="0")
    views = models.IntegerField(default="0")

    def getService(self):
        return self

    def __str__(self):
        return 'ID:' + str(self.id) + ' | Title: ' + self.title + ' | Author: ' + self.getAuthor()

    def getAuthor(self):
        author = self.author.first_name + ' ' + self.author.last_name

        if author == ' ':
            author = self.author.email

        return author

    def serialize_admin(self, payments='', user=None):
        is_author = False

        if user is not None:
            if user == self.author:
                is_author = True

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S'),
            'cost': self.cost / 100,
            'upvotes': self.upvotes,
            'views': self.views,
            'author': self.getAuthor(),
            'author_role': is_author,
            'author_karma': self.author.karma,
            'user_id': self.author.id,
            'payments': payments
        }

    def serialize_user(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S'),
            'cost': self.cost / 100,
            'upvotes': self.upvotes,
            'author': self.getAuthor(),
        }
