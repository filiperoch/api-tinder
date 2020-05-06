# coding=utf-8
### API Tinder non-officially. v0.1 Apr 2020
### Author: Filipe Rocha Silva
### https://github.com/filiperochs
### MIT License

import auth_fb
import auth_tinder

email = "" ### Email or Phone     << CHANGE
password = "" ### << CHANGE
fb_access_token = auth_fb.get_fb_access_token(email, password)
fb_id = auth_fb.get_fb_id(fb_access_token)

tinder_access_token = auth_tinder.get_auth_token(fb_access_token, fb_id)

get_headers = auth_tinder.get_headers
host = "https://api.gotinder.com"

'''
Config Example File
Rename for: config.py
'''