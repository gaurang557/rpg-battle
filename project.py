import requests
r=requests.get("http://www.google.com")
print(r.url)
f=open("google.txt", "w")
f.write(r.text)
f.close()
