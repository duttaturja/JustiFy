from django.core import signing

def generate_verification_token(user):
    data = {'user_id': user.pk}
    token = signing.dumps(data, salt='email-verification')
    return token

def verify_verification_token(token, max_age=60*60*24):  # Token valid for 1 day
    try:
        data = signing.loads(token, salt='email-verification', max_age=max_age)
        return data['user_id']
    except signing.BadSignature:
        return None
