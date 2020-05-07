# coding=utf-8
### Author: Filipe Rocha Silva https://github.com/filiperochs
### MIT License

import config, requests, json
headers = config.get_headers.copy()
host = config.host

def get_updates(last_activity_date=""):
        return requests.post(host + '/updates', headers=headers, data=json.dumps({"last_activity_date": last_activity_date})).json()

def get_profile():
        return requests.get(host + '/profile', headers=headers).json()

def change_preferences(**kwargs):
        return requests.post(host + '/profile', headers=headers, data=kwargs).json()

def get_meta():
        return requests.get(host + '/v2/meta', headers=headers).json()

def get_recs():
        return requests.get(host + '/v2/recs/core?locale=pt-BR', headers=headers).json()

def change_webusername(username=""):
        return requests.put(host + '/profile/username', headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}, data=json.dumps({"username": username})).json()

def like(person_id):
        return print("Match:", requests.get(host + f"/like/{person_id}", headers=headers).json()['match'])

def dislike(person_id):
        return requests.get(host + f"/pass/{person_id}", headers=headers).json()

def superlike(person_id):
        return requests.post(host + f"/like/{person_id}/super", headers=headers).json()

def send_msg(match_id, msg):
        return requests.post(host + f"/user/matches/{match_id}", headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}, data=json.dumps({"message": msg})).json()

def get_person(id):
        return requests.get(host + f"/user/{id}", headers=headers).json()

def unmatch(match_id):
        return requests.delete(host + f"/matches/{match_id}", headers=headers).json()

def report(person_id, cause, explanation=''):
        return requests.post(host + f"/report/user/{person_id}?locale=pt-BR", headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}, data=json.dumps({"cause": cause, "text": explanation})).json()

def get_all_matches(limit=20):
        return requests.get(host + f"/v2/matches?count={limit}", headers=headers).json()

def update_location(lat, lon):
        return requests.post(host + '/passport/user/travel', headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}, data=json.dumps({"lat": lat, "lon": lon})).json()

def reset_real_location():
        return requests.post(host + '/passport/user/reset', headers={"X-Auth-Token": headers['X-Auth-Token'], "User-agent": headers['User-agent'], "content-type": "application/json"}).json()