import pytest

from tweet_app.models import UserAccount, Tweet
@pytest.mark.django_db
class TestTweet:
    @pytest.fixture
    @staticmethod
    def follow_user_accounts():
        # Create users
        if not UserAccount.objects.filter(username='John').exists():
            user_a = UserAccount.objects.create_user('John', 'john@twitter.com', 'johnpassword')
        else:
            user_a = UserAccount.objects.get(username='John')

        if not UserAccount.objects.filter(username='Danny').exists():
            user_b = UserAccount.objects.create_user('Danny', 'danny@twitter.com', 'dannypassword')
        else:
            user_b = UserAccount.objects.get(username='Danny')

        # user_a to follow user_b
        user_a.follow(user_b)

        # create tweets for user_b
        for i in range(1, 13):
            Tweet.objects.get_or_create(user=user_b, message='Tweet %s' % i)

        return [user_a, user_b]

    @staticmethod
    def test_list_following_tweets(follow_user_accounts):
        user_account_a, user_account_b = follow_user_accounts

        assert user_account_a.username == 'John'
        assert user_account_b.username == 'Danny'
        assert UserAccount.objects.filter(username='Danny', followed_by=user_account_a).exists()
        assert len(Tweet.list_following_tweets(user_account_a, 20)) == 12


