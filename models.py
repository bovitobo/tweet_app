from django.db import models
from django.contrib.auth.models import User


class UserAccount(User):
    followed_by = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return f'{self.username}: {self.first_name} {self.last_name}'

    def follow(self, another_user):
        another_user.followed_by.add(self)
        another_user.save()


class Tweet(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.CharField(max_length=144)

    def __str__(self):
        return f'{self.user.username}: {self.message}'

    @staticmethod
    def list_following_tweets(user, limit=10):
        """
        Get a list of tweets written by the UserAccounts user follows
        :param user: user who follows other user's tweets
        :type user: UserAccount
        :param limit: Number of records to return, Default = 10
        :type limit: int
        :return: queryset
        :rtype:QuerySet
        """
        queryset = Tweet.objects.filter(user__followed_by=user).order_by('-id')[0:limit]
        return queryset
