# coding=utf-8
### API Tinder non-officially. Apr 2020
### Author: Filipe Rocha Silva
### https://github.com/filiperochs/api-tinder
### MIT License
### Used from https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py

import re
import requests
import robobrowser

MOBILE_USER_AGENT = "Tinder/11.14.0 (iPhone; iOS 13.4.1; Scale/2.00)"
url_auth = "https://www.facebook.com/v2.8/dialog/oauth?app_id=464891386855067&cbt=1588812042858&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D46%23cb%3Df341452d0bbc84%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff519b02b3e7a58%26relation%3Dopener&client_id=464891386855067&display=popup&domain=tinder.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Ftinder.com%2F&locale=en_US&logger_id=f1ec8e1ebc3b9f4&origin=1&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D46%23cb%3Dfaf96f1df020e%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff519b02b3e7a58%26relation%3Dopener%26frame%3Df1ac99c804cd72c&response_type=token%2Csigned_request%2Cgraph_domain&scope=user_birthday%2Cuser_photos%2Cemail%2Cuser_likes&sdk=joey&version=v2.8"


def get_fb_access_token(email, password):
    browser = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    browser.open(url_auth)
    form = browser.get_form()
    form["pass"] = password
    form["email"] = email
    browser.submit_form(form, submit=form['login'])

    try:
        if browser.get_form(id="platformDialogForm") != None:
            formPermissions = browser.get_form(id="platformDialogForm")
            browser.submit_form(formPermissions, submit=formPermissions['__CONFIRM__'])
        
        access_token = re.search(
            r"access_token=([\w\d]+)", browser.response.content.decode()).groups()[0]
        
        return access_token

    except Exception as e:
        print("Access Token could not be retrieved. Check your username and password.")
        print("Official error: %s" % e)
        return {"error": "Access Token could not be retrieved. Check your username and password."}


def get_fb_id(access_token):
    if "error" in access_token:
        return {"error": "access token could not be retrieved"}

    """Gets facebook ID from access token"""

    req = requests.get(
        'https://graph.facebook.com/me?access_token=' + access_token)
    return req.json()["id"]