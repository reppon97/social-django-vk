
class Token:
    """Gets your provider's access_key

    Args:
        django-request, provider name (google-oauth2, facebook-oauth2, etc)
        you can find the full list of providers here: https://github.com/omab/django-social-auth

    Returns:
        Oauth2 access key
    """
    def __init__(self, request, provider):
        user = request.user
        self.provider = provider
        self.social = user.social_auth.get(provider=provider)
        self.access_key = None

    def get_token(self):
        self.access_key = self.social.extra_data['access_token']

        return self.access_key

    def get_provider(self):
        return self.provider
