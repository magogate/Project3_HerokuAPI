# Created By: 
#     Grettel Canepari
#     Katherine Lee
#     Mandar Gogate
#     Petra Alex
#     Preet Puri
#     Sweta Shekhar
# Created On: 01/01/2020
# Updated On: 01/10/2020


from pymongo import MongoClient
import pandas as pd

def getConnection():
    # conn = MongoClient('localhost', 27017)
    connString = "mongodb+srv://mandargogate:Password123@cluster0-x4wnf.mongodb.net/test?retryWrites=true&w=majority"    
    conn = MongoClient(connString, 27017)    
    conn.population
    return conn.population

def getConnectionForAccidents():
    # conn = MongoClient('localhost', 27017)
    connString = "mongodb+srv://mandargogate:Password123@cluster0-x4wnf.mongodb.net/test?retryWrites=true&w=majority"    
    conn = MongoClient(connString, 27017)
    conn.US_Accidents
    return conn.US_Accidents

def insertUSCityPopulation(cities_list):
    # print(cities_list)
    db = getConnection()

    cityPopulation = list(db.all_us_city_population.find())
    if len(cityPopulation) < 1:
        db.all_us_city_population.insert(cities_list)
    else:
        # https://www.w3schools.com/python/python_mongodb_delete.asp
        db.all_us_city_population.delete_many({})
        db.all_us_city_population.insert(cities_list)

def insertGACityPopulation(cities_list):
    db = getConnection()
    cityPopulation = list(db.ga_city_population.find())

    if len(cityPopulation) < 1:
        db.ga_city_population.insert(cities_list)
    else:
        # https://www.w3schools.com/python/python_mongodb_delete.asp
        db.ga_city_population.delete_many({})
        db.ga_city_population.insert(cities_list)
    

def getUSCityPopulation():
    db = getConnection()    
    cityPopulation = list(db.all_us_city_population.find({},{"population": 1, "_id":0, "city": 1, "accidents":1, "state":1, "transportation":1}))
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    df = pd.DataFrame(cityPopulation)
    cityPopJson = df.to_json(orient='records')
    # print(cityPopJson)
    return cityPopJson

def getGACityPopulation():
    db = getConnection()    
    cityPopulation = list(db.ga_city_population.find({},{"population": 1, "_id":0, "city": 1, "accidents":1, "state":1, "transportation":1}))
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    df = pd.DataFrame(cityPopulation)
    cityPopJson = df.to_json(orient='records')
    # print(cityPopJson)
    return cityPopJson

def getUSaccidents2018():
    db = getConnectionForAccidents()    
    us_accidents_2018 = list(db.us_accidents_2018.find({},{"ID": 1, "_id":0, "Severity": 1, "Start_Time":1, "Start_Lat":1, "Start_Lng":1, "Street":1, "City":1, "State":1, "Temperature(F)":1, "Humidity(%)":1, "Weather_Condition":1, "Visibility(mi)":1, "Precipitation(in)":1, "Traffic_Signal":1, "Sunrise_Sunset":1}))
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    df = pd.DataFrame(us_accidents_2018)
    accidentsJson = df.to_json(orient='records')
    # print(cityPopJson)
    return accidentsJson

# getUSaccidents2018()