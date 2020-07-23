import vk_api


class VK:
    """Gets your VK own info and 5 random friends' name/last name

    Args:
        VK oauth2 access key

    Returns:
        Own first/last name, 5 friends' first/last_name
    """
    def __init__(self, token=None):
        self.vk = vk_api.VkApi(token=token)

    def get_own_info(self):
        get_own_account_info = self.vk.method('users.get', {'fields': ('first_name', 'last_name')})

        return get_own_account_info

    def get_friends(self):
        friends = self.vk.method('friends.get', {'fields': 'last_name', 'count': 5})['items']

        return friends

    @staticmethod
    def get_provider_name():
        return "vk-oauth2"
