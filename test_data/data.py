import random
import string

adding_products = [
    {
        'product_name': 'Seimens',
        'meta_tag_title': 'mobile',
        'description': 'test111',
        'model': 'A35'
    },
    {
        'product_name': 'Nokia',
        'meta_tag_title': 'smartphone',
        'description': 'test222',
        'model': 'N-Gage QD'
    },
    {
        'product_name': 'HTC',
        'meta_tag_title': 'communicator',
        'description': 'test333',
        'model': '7 Pro'
    }

]


def add_product():
    return random.choice(adding_products)


admin_user = {
    'name': 'user',
    'password': 'bitnami'
}


def random_word(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def random_phone():
    letters = string.digits
    return ''.join(random.choice(letters) for _ in range(10))


def random_email(length=5):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length)) + \
        random.choice(['@gmail.com', '@mail.ru', '@yandex.ru'])


random_user = {
    'first_name': random_word(random.randint(5, 15)),
    'last_name': random_word(random.randint(5, 10)),
    'email': random_email(random.randint(7, 15)),
    'telephone': random_phone(),
    'password': random_word(random.randint(10, 15)),
}
