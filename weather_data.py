import requests

#add an api key from openweather
API_KEY=""


def get_data(place,forecast_day=None,kind=None):
    url="https://api.openweathermap.org/data/2.5/forecast?q={0}&appid={1}&units=metric".format(place,API_KEY)
    request=requests.get(url)
    data=request.json()
    filter_data=data["list"]
    nr_values=8*int(forecast_day)
    filter_data=filter_data[:nr_values]
    if kind=="Temperature":
        #just return list because we need temp and date
        return filter_data
    if kind=="Sky":
        filter_data=[dict["weather"][0]["main"] for dict in filter_data]
        return filter_data

if __name__ =="__main__":
    tempt=get_data(place="Taipei",forecast_day=1,kind="Sky")
    print(tempt)
   
        