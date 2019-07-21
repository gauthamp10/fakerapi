from faker import Faker
import sqlite3 as lite
from flask import Flask, jsonify, request
import json
import gunicorn

fake = Faker()
app = Flask('app')


@app.route("/api/v1/<func>/<int:num>")
def mulit(func,num):
    ccno=fake.credit_card_number(card_type=None)
    profile=fake.profile(fields=None, sex=None)
    keys=list()
    for key in profile.keys():
        keys.append(key)
    s=list()
    if str(func) in keys:
        for i in range(num):
            s.append(str(fake.profile(fields=None, sex=None)[str(func)]))
        return json.dumps(s)
    elif str(func) == 'profile':
        s=list()
        for i in range(num):
            s.append(str(fake.profile(fields=None, sex=None)))
        return json.dumps(s)
    elif str(func) == 'credit_card':
        s=list()
        for i in range(num):
            s.append(str(fake.credit_card_number(card_type=None)))
        return json.dumps(s)
    elif str(func) == 'sentence':
        s=list()
        for i in range(num):
            s.append(str(fake.paragraphs( ext_word_list=None)))
        return json.dumps(s)
    elif str(func) == 'license':
        s=list()
        for i in range(num):
            s.append(str(fake.license_plate()))
        return json.dumps(s)
    elif str(func) == 'color':
        s=list()
        for i in range(num):
            s.append(str(fake.color_name()))
        return json.dumps(s)
    elif str(func) == 'hex_color':
        s=list()
        for i in range(num):
            s.append(str(fake.hex_color()))
        return json.dumps(s)
    elif str(func) == 'rgb':
        s=list()
        for i in range(num):
            s.append(str(fake.rgb_color()))
        return json.dumps(s)
    elif str(func) == 'rgb_css':
        s=list()
        for i in range(num):
            s.append(str(fake.rgb_css_color()))
        return json.dumps(s)
    elif str(func) == 'currency':
        s=list()
        for i in range(num):
            s.append(str(fake.currency_name()))
        return json.dumps(s)
    elif str(func) == 'date':
        s=list()
        for i in range(num):
            s.append(str(fake.date(pattern="%Y-%m-%d", end_datetime=None)))
        return json.dumps(s)
    elif str(func) == 'year':
        s=list()
        for i in range(num):
            s.append(str(fake.year()))
        return json.dumps(s)
    elif str(func) == 'timezone':
        s=list()
        for i in range(num):
            s.append(str(fake.timezone()))
        return json.dumps(s)
    elif str(func) == 'random_url':
        s=list()
        for i in range(num):
            s.append(str(fake.image_url(width=None, height=None)))
        return json.dumps(s)
    elif str(func) == 'ipv4':
        s=list()
        for i in range(num):
            s.append(str(fake.ipv4(network=False, address_class=None, private=None)))
        return json.dumps(s)
    elif str(func) == 'ipv6':
        s=list()
        for i in range(num):
            s.append(str(fake.ipv6(network=False)))
        return json.dumps(s)
    elif str(func) == 'mac':
        s=list()
        for i in range(num):
            s.append(str(fake.mac_address()))
        return json.dumps(s)
    elif str(func) == 'uri':
        s=list()
        for i in range(num):
            s.append(str(fake.uri()))
        return json.dumps(s)
    elif str(func) == 'isbn10':
        s=list()
        for i in range(num):
            s.append(str(fake.uri()))
        return json.dumps(s)
    elif str(func) == 'isbn13':
        s=list()
        for i in range(num):
            s.append(str(fake.uri()))
        return json.dumps(s)
    elif str(func) == 'job':
        s=list()
        for i in range(num):
            s.append(str(fake.job()))
        return json.dumps(s)
    elif str(func) == 'boolean':
        s=list()
        for i in range(num):
            s.append(str(fake.boolean(chance_of_getting_true=50)))
        return json.dumps(s)
    elif str(func) == 'useragent':
        s=list()
        for i in range(num):
            s.append(str(fake.user_agent()))
        return json.dumps(s)
    elif str(func) == 'phone':
        s=list()
        for i in range(num):
            s.append(str(fake.phone_number()))
        return json.dumps(s)
    elif str(func) == 'md5':
        s=list()
        for i in range(num):
            s.append(str(fake.md5(raw_output=False)))
        return json.dumps(s)
    elif str(func) == 'password':
        s=list()
        for i in range(num):
            s.append(str(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)))
        return json.dumps(s)
    elif str(func) == 'sha1':
        s=list()
        for i in range(num):
            s.append(fake.sha1(raw_output=False))
        return json.dumps(s)
    elif str(func) == 'sha256':
        s=list()
        for i in range(num):
            s.append(fake.sha256(raw_output=False))
        return json.dumps(s)
    elif str(func) == 'iban':
        s=list()
        for i in range(num):
            s.append(fake.iban())
        return json.dumps(s)
    elif str(func) == 'credit_card_full':
        s=list()
        for i in range(num):
            s.append(fake.credit_card_full(card_type=None))
        return json.dumps(s)
    elif str(func) == 'country':
        s=list()
        for i in range(num):
            s.append(fake.country())
        return json.dumps(s)
    elif str(func) == 'random_number':
        s=list()
        for i in range(num):
            s.append(fake.random_number(digits=None, fix_len=False))
        return json.dumps(s)
    else:
        return 'Not Found. Check endpoints'