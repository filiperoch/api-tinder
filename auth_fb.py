# coding=utf-8
### API Tinder non-officially. v0.1 Apr 2020
### Author: Filipe Rocha Silva
### https://github.com/filiperochs
### MIT License
### Used from https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py

import re
import requests
import robobrowser

MOBILE_USER_AGENT = "Tinder/11.14.0 (iPhone; iOS 13.4.1; Scale/2.00)"
url_auth = "https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1588016031099%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fconnect%252Fxd_arbiter.php%253Fversion%253D46%2523cb%253Df175f24fae866b4%2526domain%253Dtinder.com%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff1a94e0f0525c54%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Df30f4c360ee4808%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fconnect%252Fxd_arbiter.php%253Fversion%253D46%2523cb%253Df3fd82d04dc71%2526domain%253Dtinder.com%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff1a94e0f0525c54%2526relation%253Dopener%2526frame%253Dfd42c833f84bc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26logged_out_behavior%3D6&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter.php%3Fversion%3D46%23cb%3Df3fd82d04dc71%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff1a94e0f0525c54%26relation%3Dopener%26frame%3Dfd42c833f84bc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0"


def get_fb_access_token(email, password):
    browser = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    browser.open(url_auth)
    form = browser.get_form()
    form["pass"] = password
    form["email"] = email
    browser.submit_form(form, submit=form['login'])

    # VERIFICAR CONFIRMAÇÃO POR "OK" QUANDO É NOVO USUÁRIO PELO FACEBOOK

    try:
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