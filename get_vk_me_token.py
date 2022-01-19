import requests

login = input('Введите логин:  ')
password= input('Введите пароль:  ')

session = requests.Session()

def auth(login:str, password:str, two_fa:bool = False, code:str=None):
    return session.get(f'https://oauth.vk.com/token', params={
        'grant_type': 'password',
        'client_id': '6146827',
        'client_secret': 'qVxWRF1CwHERuIrKBnqe',
        'username': login,
        'password': password,
        'v': '5.130',
        '2fa_supported': '1',
        'force_sms': '1' if two_fa else '0',
        'code': code if two_fa else None
    }).json()

response = auth(login, password)

if 'validation_sid' in response:
    session.get("https://api.vk.com/method/auth.validatePhone", params={'sid': response['validation_sid'],'v': '5.131'})
    response = auth(login, password)
    code = input('Введите код из смс:  ')
    response = auth(login, password, two_fa=True, code=code)   

if 'access_token' in response:
    token = response['access_token']
    try:
        requests.get('https://api.vk.com/method/messages.send?v=5.130', params={
            'access_token': token,
            'message': f'Ваш токен: {token}',
            'peer_id': response['user_id'],
            'random_id': 0
        })
        print('Токен отправлен в избранное.')
    except:
        print('Не удалось отправить токен в избранное.')
    print(f'Ваш токен: {token}')
else:
    print(response)


# Thanks,
# Vk: https://vk.com/id266287518, https://vk.com/id230192963.

# Written with love. By Alexey Kuznetsov.
# Bug reports write here -> https://vk.me/id194861150 
