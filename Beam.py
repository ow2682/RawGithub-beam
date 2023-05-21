import urllib.request

url = "RAW GITHUB HERE"

response = urllib.request.urlopen(url)
script_content = response.read().decode("utf-8")

exec(script_content)
