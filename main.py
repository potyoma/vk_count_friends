
import requests # to work with https requests
from datetime import date # to count age
import operator # for sorting

# data for request 
token = '243ceda5243ceda5243ceda501244cf4c32243c243ceda57a5c553a5c8ac03c9b8eb1b8'
domain = 'https://api.vk.com/method'
fields = 'bdate'

def calc_age(user_id):
    query = '{}/friends.get?access_token={}&user_id={}&fields={}&v=5.53'.format(domain, token, user_id, fields)
    today = date.today()
    number_age = []
    ages = []
    response = requests.get(query)
    response = response.json()
    have_bdays = []
    for elem in response['response']['items']:
        if 'bdate' in elem.keys() and len(elem['bdate']) > 7:
            have_bdays.append(elem)
    for item in have_bdays:
        ages.append(item['bdate'])   
    for i in range(len(ages)):
        ages[i] = date(int(ages[i][ages[i].rfind('.')+1:]), int(ages[i][ages[i].find('.')+1:ages[i].rfind('.')]), int(ages[i][:ages[i].find('.')]))
        ages[i] = (today - ages[i]).days//365
    for elem in set(ages):
        number_age.append((elem, ages.count(elem)))
    number_age.sort(key = operator.itemgetter(1), reverse = True)
    return number_age

print(calc_age('444830045'))

