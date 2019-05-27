import json
import requests


class SnapChat:

    def __init__ (self, username):
        self.username = username
        self.username_suggestions = ""


    def check_username(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://accounts.snapchat.com/",
            "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            }

        check_username_url= "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg"

        r = requests.post(check_username_url.format(self.username), headers=headers)
        data = r.json()

        status = data.get("reference").get("status_code")
        suggestions = data.get("reference").get("suggestions")

        if len(suggestions):
            self.username_suggestions = suggestions
        

        if status == "TAKEN" or "TOO_LONG" or "INVALID_CHAR":
            error_message = data.get("reference").get("error_message")

            return error_message

        return "username available"





