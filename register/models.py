from django.db import models


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=100, unique=True, null=False)


class Wrong(models.Model):
    pr_id = models.IntegerField(null=False)
    email = models.ForeignKey(User, on_delete='CASCADE', related_name='user_wrong')


class Bookmark(models.Model):
    pr_id = models.IntegerField(null=False)
    email = models.ForeignKey(User, on_delete='CASCADE', related_name='user_bookmark')
