import requests
import json
import win32com.client as wincom
city=input("Enter the name of city\n")
url="your api"
r= requests.get(url)
wdict=json.loads(r.text)
b = wdict['current']['temp_c']
print(b)
speak=wincom.Dispatch("SAPI.SpVoice")
speak.Speak(f"Whether of {city} city is" + str(b))


