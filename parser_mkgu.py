import fake_user_agent
import requests
from bs4 import BeautifulSoup
import fake_user_agent

session = requests.Session()
link = 'https://vashkontrol.ru/users/sign_in'
user = fake_user_agent.UserAgent().random
header = {
    'user-agent' : user
}
data = {
    'authenticity_token': "",
    'user[login]': 'login',
    'user[password]': 'password',
    'commit': 'Войти'
}

response = session.post(link, data=data, headers=header).text

profile_info = 'https://vashkontrol.ru/hershel/analytics/9792/summary'
profile_resposnse = session.get(profile_info, headers=header).text

print(profile_resposnse)


cookies_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info, headers=header)
print(resp.text)




'''data1 = {    'user[login]' :	'login',
        'user[password]' : 'password',
        'commit' : "Войти"
         }


s = requests.Session()
loging = s.post(link, data=data1)
f = open('resul.txt', 'w+')
f.write(loging.text)
f.close()'''




'''def loginbot(login, password):
    s = requests.Session()
    s = requests.get('https://vashkontrol.ru/hershel')

    data = {
        'authenticity_token':"",
        'user[login]':'login',
        'user[password]':'password',
        'commit':'Войти'
    }

    r = s.get('https://vashkontrol.ru/users/sign_in', data=data)
    return r.text


loginbot()

'''