import requests


url = "https://jsonfakery.com/jobs"
response = requests.get(url)
Jobs= response.json()