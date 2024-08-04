from .models import User


def seed_user():
    users = [
        User(first_name="Shashi", last_name="Bhagat", middle_name="Bhushan", age=30,
             email='test@mail.com', gender='M', username='shashidev091', password='******'),
        User(first_name="Rabita", last_name="Bhagat", age=27,
             email='testR@mail.com', gender='F', username='rabit', password='********')
    ]

    User.objects.bulk_create(users)


def get_users():
    return User.objects.all()
