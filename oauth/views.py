from django.shortcuts import render
from oauth.handlers.vk import VK
from oauth.utils.tokenizer import Token


def home(request):
    """
    :param request: django session request
    :return: vk auth window, if user is authenticated, it returns own name/last name, 5 random friends' names
    """
    if request.user.is_authenticated:
        vk = VK()
        token = Token(request, vk.get_provider_name())
        vk_method = VK(token.get_token())

        context = {'users': vk_method.get_friends, 'own_info': vk_method.get_own_info}

        return render(request, 'oauth/success.html', context)

    return render(request, 'oauth/home.html')
