import requests



class City:
    def __init__(self, name, lat, lon, units="mertic"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()


    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=2d83dc6006cddeea3d2828bafdfcba61")

        except:
            print("OOopsie! something did not clicked")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"] 


    def temp_print(self):
        print(f"In {self.name} it is currently {self.temp}° C")
        print(f"Today's High: {self.temp_max}° C")
        print(f"Today's Low: {self.temp_min}° C")


        


my_city = City("London", 35.6762, 139.6503)  
my_city.temp_print()

