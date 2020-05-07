# coding=utf-8
### API Tinder non-officially. Apr 2020
### Author: Filipe Rocha Silva
### https://github.com/filiperochs/api-tinder
### MIT License

import json
import requests

host = "https://api.gotinder.com"
app_v = "11.14.0"

get_headers = {
    "User-agent": "Tinder/11.14.0 (iPhone; iOS 13.4.1; Scale/2.00)",

}
headers = get_headers.copy()
headers['accept-encoding'] = "gzip"
headers['host'] = "api.gotinder.com"
headers['connection'] = "keep-alive"
headers['content-type'] = "application/json"

def get_auth_token(fb_token, fb_id):
    if "error" in fb_token:
        return {"error": "could not retrieve fb_token"}
    if "error" in fb_id:
        return {"error": "could not retrieve fb_id"}
    
    url = host + '/v2/auth/login/facebook'
    payload = json.dumps({
        'token': fb_token,
        'id': fb_id,
        'client-version': app_v
    })
    headers['content-length'] = str(len(payload))
    req = requests.post(url, headers=headers, data=payload)

    try:
        if req.json()['data']['is_new_user']:
            tinder_auth_token = req.json()['data']['onboarding_token']
        else:
            tinder_auth_token = req.json()['data']['api_token']
        
        headers.update({"X-Auth-Token": tinder_auth_token})
        get_headers.update({"X-Auth-Token": tinder_auth_token})
        print("You have been successfully authorized!")
        return tinder_auth_token
    except Exception as e:
        print(e)
        return {"error": "Something went wrong. Sorry, but we could not authorize you."}