import requests


try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=51.5085&lon=-0.1257&appid=2d83dc6006cddeea3d2828bafdfcba61")

except:
    print("OOopsie! something did not clicked")


response_json = response.json()

temp = response_json["main"]["temp"]
temp_min = response_json["main"]["temp_min"]
temp_max = response_json["main"]["temp_max"] 