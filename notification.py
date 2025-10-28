import requests
import json
from MySecrets import secrets
from datetime import datetime

def notif(title,message):
    try:
        apiurl="https://www.pushsafer.com/api"
        notif_title=title
        notif_msg=message
        notif_icon="1"
        notif_priority = "2"
        notif_device=secrets.get('PUSHSAFER_DEVICE_ID') # from pushsafer account >> device ID nbr
        notif_key=secrets.get('PUSHSAFER_PRIVATE_KEY') # from pushsafer account >> your key
        mydata = {'t':notif_title,
              'i':notif_icon,
              'm':notif_msg,
              'pr':notif_priority,
              'd':notif_device,
              'k':notif_key}  
        # uncomment if sending a new notification is wanted
        x=requests.post(apiurl,data=mydata)
        # example binary response: b'{"status":1,"success":"message transmitted","available":921,"message_ids":"59693451:57813"}'

        # uncomment following 2 lines if only historical messages info for this device are needed :
        #mymessages = "-m?k=" + notif_key + "&d=" + notif_device
        #x=requests.get("https://www.pushsafer.com/api" + mymessages)


        # uncomment following 2 lines if only available notifications/calls is requested without sending a new notification
        #myavailablecalls = "-k?k=" + notif_key + "&u=" + secrets.get('MY_EMAIL') 
        #x=requests.get("https://www.pushsafer.com/api" + myavailablecalls)
        # example binary response:  b'{"status":1,"success":"valid key","available-api-calls":500}' 

        # x : bytes variable
        #print(type(x)) # variable <class 'requests.models.Response'>
        ResponseContent = x.content
        #print(type(ResponseContent)) # variable = bytes
        print(str(datetime.now().time())+ "\t" +"pushsafer bytes response : " + str(ResponseContent))
        ResponseDictionary = json.loads(ResponseContent.decode()) # extract dictionary inside x : bytes
        NbrMessagesLeft = ResponseDictionary['available']  # get value from key:'available'
        #print()
        print("Messages Left : " + str(NbrMessagesLeft))

    except Exception as error:
        # in case your Python code has no internet access or other issues
        print(error)
    return

notif("TEST","my message")
