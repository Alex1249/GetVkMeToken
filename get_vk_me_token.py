import requests

login = input('Введите логин (номер телефона +7):  ')
password= input('Введите пароль:  ')

session = requests.Session()

def auth(login:str, password:str, tow_fa:bool = False, code:str=None):
    return session.get(f'https://oauth.vk.com/token?grant_type=password&client_id=6146827&client_secret=qVxWRF1CwHERuIrKBnqe&username={login}&password={password}&v=5.131&2fa_supported=1{f"&force_sms=1&code={code}" if tow_fa else ""}').json()

response = auth(login, password)

if 'validation_sid' in response:
    session.get("https://api.vk.com/method/auth.validatePhone", params=[('sid', response['validation_sid']),('v', '5.131')])
    response = auth(login, password)
    code = input('Введите код из смс:  ')
    response = auth(login, password, tow_fa=True, code=code)   

print(response)

# Thanks,
# Vk: https://vk.com/id266287518, https://vk.com/id230192963.

# Written with love. By Alexey Kuznetsov.
# Bug reports write here -> https://vk.me/id194861150 