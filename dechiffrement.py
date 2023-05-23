from random import random
import base64
def fromage_de_bite(c, n):
    if 'a' <= c <= 'z':
        return chr((ord(c) + n - ord('a')) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) + n - ord('A')) % 26 + ord('A'))
    else:
        return c
def couille(s, n):
    roquefort = ""
    roquefort += fromage_de_bite("a", n) 
    roquefort += fromage_de_bite("H", n) 
    roquefort += fromage_de_bite("o", n) 
    i=0
    while i< len(s):
        roquefort += fromage_de_bite(s[i], n) 
        i+=1
    message = roquefort
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_bytes = base64.a85encode(base64_bytes)
    base64_bytes = base64.b32hexencode(base64_bytes)
    base64_bytes = base64.a85encode(base64_bytes)
    base64_message = base64_bytes.decode('ascii')
    roquefort = base64_message
    return roquefort
def couillevide(s):
    base64_message = s
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.a85decode(base64_bytes)
    message_bytes = base64.b32hexdecode(message_bytes)
    message_bytes = base64.a85decode(message_bytes)
    message_bytes = base64.b64decode(message_bytes)
    message = message_bytes.decode('ascii')
    for x in range(26):
        roquefort = ""
        i=0
        while i< len(message):
            roquefort += fromage_de_bite(message[i], x) 
            i+=1
        if roquefort[0] == "a" and roquefort[1] == "H" and roquefort[2] == "o":
            return "".join(roquefort[t] for t in range(3, len(message)))        
    
    
    
