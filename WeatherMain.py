# weather_data 3 hours 5 days for the listed cities 
# -------------------------------------------------------------------------------------------------------
# import the  following libraries
# -------------------------------------------------------------------------------------------------------

import requests
from datetime import date
import pandas as pd
import json

#--------------------------------------------------------------------------------------------------------
# ADD the names of cities here
#=========================================================================================================
cities = ["sydney","newcastle", "Central Coast", "Wollongong","Albury" ]
#==========================================================================================================
country_code = "AU"  # Country Code 
#---------------------------------------------------------------------------------------------------------

#set API Key
APIKEY = 'YOUR API KEY' #api key from Harmeet's openweathermap.org

#---------------------------------------------------------------------------------------------------
# Get 5 day forecast
#-----------------------------------------------------------------------------------------------------

for i, v in enumerate(cities):    #Loopthru the cities listed above
    newlocation = v+','+country_code
   #  Call the API for forecast of each city
    url = "http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s&units=metric" %(newlocation,APIKEY)
    response = requests.get(url)
    response_dict = json.loads(response.text)
    
    # Get the individual values response_dict['list']
    date_time = []
    temp_deg_c = []
    date=[]
    temp_min=[]
    temp_max=[]
    for index, item in enumerate(response_dict['list']):
        date_time.append (response_dict['list'][index]['dt_txt'])
        temp_deg_c.append (response_dict['list'][index]['main']['temp'])
        temp_min.append (response_dict['list'][index]['main']['temp_min'])
        temp_max.append (response_dict['list'][index]['main']['temp_max'])
  
    time=list(map(lambda x : str(x).split(" ")[1], (response_dict['list'][index]['dt_txt'] for index, item in enumerate(response_dict['list']))))
    date=list(map(lambda x : str(x).split(" ")[0], (response_dict['list'][index]['dt_txt'] for index, item in enumerate(response_dict['list']))))

    #s_date_time = pd.Series(data = date_time)
    #s_temp_deg_c = pd.Series(data =  temp_deg_c)
    forecast = pd.DataFrame(data ={"Date": date, 'Time':time, "Temp":temp_deg_c, 'Minimum Temp':temp_min,'Max Temp':temp_max})
    forecast = forecast[['Date', 'Time', 'Temp', 'Minimum Temp', 'Max Temp']]

    # print ('forecast for every 3 hours for the next 5 days in %s', forecast_5d %location)
    print('********************************************************************************************************************')
    print('Forecast for every 3 hours for the next 5 days in %s' %newlocation.replace(',',', '))
    print('********************************************************************************************************************')
    print(forecast)





