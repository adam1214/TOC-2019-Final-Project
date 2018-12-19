import requests

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = ""
url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)

def send_text_message(id, text):
    #url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
    #url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment": {
                "type":"image", 
                "payload": {
                    "url":img_url, 
                    "is_reusable": True
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send image")
    return response

"""
def send_button_message(id, text, buttons):
    pass
"""
