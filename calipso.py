from colorama import Fore, Back, Style
from dechiffrement import fromage_de_bite, couille,couillevide
from random import random
import sys, time, threading, requests, os ,base64, json,websocket
os.system("cls")
def printlent(text):
    for c in text:
        sys.stdout.write(c)
        # sys.stdout.flush()
        time.sleep(0.00001)
    sys.stdout.write("\n")
banner = """
 ▄████▄   ▄▄▄       ██▓     ██▓ ██▓███    ██████  ▒█████  
▒██▀ ▀█  ▒████▄    ▓██▒    ▓██▒▓██░  ██▒▒██    ▒ ▒██▒  ██▒
▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒██▒▓██░ ██▓▒░ ▓██▄   ▒██░  ██▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ░██░▒██▄█▓▒ ▒  ▒   ██▒▒██   ██░
▒ ▓███▀ ░ ▓█   ▓██▒░██████▒░██░▒██▒ ░  ░▒██████▒▒░ ████▓▒░
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░▓  ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ 
  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░░▒ ░     ░ ░▒  ░ ░  ░ ▒ ▒░ 
░          ░   ▒     ░ ░    ▒ ░░░       ░  ░  ░  ░ ░ ░ ▒  
░ ░            ░  ░    ░  ░ ░                 ░      ░ ░  
░  
calipso crypt in discord by Opale 
"""
printlent(Fore.GREEN+banner)

sauvegarde = ""
question_de_import = str(input('import your backup token? y/n :'))
if question_de_import == "y" :
    
    with open("data.json", "r") as f:
        data = json.load(f)
        token = data["token"]
        

else :

    token =str(input("token :"))
    sauvegarde = str(input("save settings?  y/n :"))




if sauvegarde == "y" :
    Sauvegardejson = {"token" : token }


    with open("data.json", "w") as json_file:
        json.dump(Sauvegardejson, json_file)
    print("backup successful")
print("")
idchannel = int(input("channel id:")) 
print("")
def listen(token):
    def send_json_request(ws,request):
        ws.send(json.dumps(request))

    def recieve_json_reponse(ws):
        reponse = ws.recv()
        if reponse:
            return json.loads(reponse)

    def heartbeat(interval, ws):
        print("calipso work")
        print("")
        while True:
            time.sleep(interval)
            heartbeatJSON= {
                "op":1,
                "d":"null"
            }
            send_json_request(ws, heartbeatJSON)

    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=10&encording=json")
    event = recieve_json_reponse(ws)

    heartbeat_interval = event ["d"]["heartbeat_interval"]/1000
    threading._start_new_thread(heartbeat,(heartbeat_interval,ws))

    payload={
        "op" : 2,
        "d":{
            "token":token,
            "properties":{
                "$os":"windows",
                "$browser": "chrome",
                "$device" : "pc"
            }
        }
    }
    send_json_request(ws,payload)

    while True:
        event = recieve_json_reponse(ws)

        try:
            print(f"{event['d']['author']['username']}: {couillevide(event['d']['content'])}")
            op_code = event("op")
            if op_code == 11:
                print("heartbeat received")
        except:
            pass
        
def send(idchannel, token):
    while True:
        msg = str(input())
        msg =couille(msg, int(25*random()))
        payload = {
            'content' : msg
        }

        header = {
            'authorization' : token
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{idchannel}/messages",data=payload, headers=header)

threading.Thread(target=send, args=(idchannel, token)).start()
threading.Thread(target=listen, args=(token,)).start()


