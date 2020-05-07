# coding=utf-8
### API Tinder non-officially. Apr 2020
### Author: Filipe Rocha Silva
### https://github.com/filiperochs/api-tinder
### MIT License

import config
import requests
import json

get_headers = config.get_headers
headers = get_headers.copy()

def get_updates(last_activity_date=""):

    '''
    Returns all updates since the given activity date.
    The last activity date is defaulted at the beginning of time.
    Format for last_activity_date: "2020-04-26T10:28:00.000Z"
    '''

    try:
        url = config.host + '/updates'
        req = requests.post(url, headers=headers, data=json.dumps(
            {"last_activity_date": last_activity_date}
        ))
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong with getting updates:", e)

def get_profile():
    
    '''
    Returns your own profile data
    '''
    
    try:
        url = config.host + '/profile'
        req = requests.get(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your data:", e)

def change_preferences(**kwargs):

    '''
    ex: change_preferences(age_filter_min=30, gender=0)
    kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments
    age_filter_min: 18..46
    age_filter_max: 22..55
    age_filter_min <= age_filter_max - 4
    gender: 0 == seeking males, 1 == seeking females
    distance_filter: 1..100
    discoverable: true | false
    {"photo_optimizer_enabled":false}
    '''

    try:
        url = config.host + '/profile'
        req = requests.post(url, headers=headers, data=kwargs)
        print("Change applied in your Profile!")
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not change your preferences:", e)

def get_meta():
    
    ''' 
    get the meta data on yourself. Includes:
    [data][account, boost, superboost, fastmatch, readreceipts, top_picks, free_daily, paywall] and more.
    '''
    
    try:
        url = config.host + '/v2/meta'
        req = requests.get(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your meta:", e)

def get_recs():

    '''
    Get a list of users that you can swipe on.
    '''

    try:
        url = config.host + '/v2/recs/core?locale=pt-BR'
        req = requests.get(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your meta:", e)

def change_webusername(username=""):

    '''
    Change your username following ex: change_username(username="newuser")
    '''

    try:
        headers['content-type'] = "application/json"
        url = config.host + '/profile/username'
        req = requests.put(url, headers=headers, data=json.dumps(
            {"username": username}
        ))
        print("Your username has been successfully changed.")
        del headers['content-type']
        return req
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not change your username:", e)

def like(person_id):

    try:
        url = config.host + f"/like/{person_id}"
        req = requests.get(url, headers=headers)
        print("Match:", req.json()['match'])
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Someting went wrong. Could not give like:", e)

def dislike(person_id):

    try:
        url = config.host + f"/pass/{person_id}"
        req = requests.get(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Someting went wrong. Could not give dislike:", e)

def superlike(person_id):

    try:
        url = config.host + f"/like/{person_id}/super"
        req = requests.post(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not give superlike:", e)

def send_msg(match_id, msg):

    try:
        headers['content-type'] = "application/json"
        url = config.host + f"/user/matches/{match_id}"
        req = requests.post(url, headers=headers, data=json.dumps(
            {"message": msg}
        ))
        del headers['content-type']
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not send your message:", e)

def get_person(id):

    '''
    Gets a user's profile via their id
    '''
    
    try:
        url = config.host + f"/user/{id}"
        req = requests.get(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get that person:", e)

def unmatch(match_id):
    
    try:
        url = config.host + f"/matches/{match_id}"
        req = requests.delete(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not unmatch person:", e)

def report(person_id, cause, explanation=''):

    '''
    There are three options for cause:
        0 : Other and requires an explanation
        1 : Feels like spam and no explanation
        4 : Inappropriate Photos and no explanation
    '''

    try:
        url = config.host + f"/report/user/{person_id}?locale=pt-BR"
        req = requests.post(url, headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}, data=json.dumps({"cause": cause, "text": explanation}))
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not report:", e)

def get_all_matches(limit=20):

    try:
        url = config.host + f"/v2/matches?count={limit}"
        req = requests.get(url, headers=headers)
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your matches:", e)

def update_location(lat, lon):

    '''
    Updates your location to the given float inputs
    Note: Requires a passport / Tinder Plus (Except in the COVID-19 pandemic period)
    '''

    try:
        url = config.host + '/passport/user/travel'
        req = requests.post(url, headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}, data=json.dumps({"lat": lat, "lon": lon}))
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not update your location:", e)

def reset_real_location():
    try:
        url = config.host + '/passport/user/reset'
        req = requests.post(url, headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"})
        return req.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not update your location:", e)
        
