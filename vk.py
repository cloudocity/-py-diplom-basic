import requests


class vkGet:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def photos_get(self, owner_id, album_id='profile'):
        get_photos_url = self.url + 'photos.get'
        get_photos_params =  {
            'owner_id': owner_id,
            'album_id': album_id,
            'rev': 0,
            'extended': 1
        }
        req = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        return req['response']['items']

    def big_size(self, sizes):
        dict_size = {
            's': 1, 'm': 2,'x': 3, 'o':4, 'p': 5, 'q': 6, 'r':7, 'y': 8, 'z':9, 'w': 10
                     }
        url_size ={}
        big_size = 0
        max_size = {}
        for photo in sizes:
            url_size[photo['type']] = photo['url']
        for type_size in url_size:
            if big_size < dict_size[type_size]:
                big_size = dict_size[type_size]
                max_size = url_size[type_size]
                size_t = type_size
        url_size = {'url': max_size, 'type': size_t}
        return url_size





