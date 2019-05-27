import json
import requests


class SnapChat:

    def __init__ (self, username):
        self.username = username
        self.username_suggestions = ""


    def check_username(self):

        # This header is specific for checking the username
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

        return "Username available"

    
    def get_snapcode(self, bitmoji=False, size=None):

        url = "https://app.snapchat.com/web/deeplink/snapcode?username={}&type={}"
        
        if bitmoji == False:
            filetype = "PNG"
            snapcode_url = url.format(self.username, filetype)

            if size:
                if int(size) > 1000:
                    raise ValueError("size can not exceed 1000")
                
                url_with_size = url+"&size={}"
                snapcode_url = url_with_size.format(self.username, filetype, size)
                
                size = str(size)+"x"+str(size)

                r = requests.get(snapcode_url)
                snapcode = r.content

                return snapcode, filetype, size
            
            return snapcode, filetype

        else:
            # NOTICE: You cant resize the SVG because there is 
            #         no need to do that.

            # If filetype is SVG, you will get the 
            # SnapCode with the bitmoji
            filetype = "SVG"

            # Putting all the information into the url
            snapcode_url = url.format(self.username, filetype)

            r = requests.get(snapcode_url)

            # The SnapCode as raw
            snapcode = r.content

            return snapcode, filetype


