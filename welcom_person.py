import win32com.client as wincom

speak=wincom.Dispatch("SAPI.sPvoice")
speak.rate=0
speak.volume=40
lis=['saurabh','alok','dheeraj','harry bhai','jhon milton']
for name in lis:
    speak.Speak(f"welcome to this magical world {name} . kepp try keep learning ")
    