from .helper import User, UsernameError,PlatformError
from django.http import JsonResponse

def UserDetails(request):
    username = request.GET.get('username')
    platform = request.GET.get('platform')
    user = User(username,platform)
    data = dict()
    try:
        data = user.get_info()
    except UsernameError:
        data = {'status':'FAILED','comment':'User not found'}
    except PlatformError:
        data = {'status':'FAILED','comment':'Platform not found'}
    except ConnectionError:
        data = {'status':'FAILED','comment':'Connection error'}
    except :
        data = {'status':'FAILED','comment':'Unknown Error'}
    return JsonResponse(data)
