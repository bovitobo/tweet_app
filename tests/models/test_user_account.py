import pytest

from tweet_app.models import UserAccount

@pytest.mark.django_db
class TestUserAccount:
    @pytest.fixture
    @staticmethod
    def follow_user_accounts():
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
        return [user_a, user_b]

    @staticmethod
    def test_follow(follow_user_accounts):
        user_account_a = follow_user_accounts[0]
        user_account_b = follow_user_accounts[1]
        assert user_account_a.username == 'John'
        assert user_account_b.username == 'Danny'
        assert UserAccount.objects.filter(username='Danny', followed_by=user_account_a).exists()
