import requests


def get_json(owner_id, token, offset):
    request_params = {
        'owner_id': owner_id,
        'count': 100,
        'offset': offset,
        'access_token': token,
        'v': '5.85'
    }

    return requests.get('https://api.vk.com/method/wall.get', request_params).json()


def get_likes(r):
    return r['response']['items'][0]['likes']['count']


def get_owner_id():
    return input('owner id: ')


def get_token():
    return input('token: ')


def main():
    owner_id = get_owner_id()
    token = get_token()
    offset = 0

    max_likes_post_id = -1
    max_num_of_likes = 0

    try:
        while True:
            response = get_json(owner_id, token, offset)['response']
            for post in response['items']:
                if post['likes']['count'] > max_num_of_likes:
                    max_num_of_likes = post['likes']['count']
                    max_likes_post_id = post['id']
            if len(response['items']) < 100:
                break
            offset += 100
    except KeyError:
        print('Wrong input')

    if max_likes_post_id != -1:
        print('id: ', max_likes_post_id, 'number of likes: ', max_num_of_likes)


if __name__ == '__main__':
    main()
