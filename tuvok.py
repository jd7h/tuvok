#!/usr/bin/python3
import json
import urllib.request

def get_series_info(series,season=0):
    url = "http://www.omdbapi.com/?i="
    #print(url + series)
    apicall = ""
    if season > 0:
        apicall = url + series + "&Season=" + str(season)
    else:
        apicall = url + series
    try:
        conn = urllib.request.urlopen(apicall)
    except:
        print("Error fetching data")
        return ""
    data = conn.read().decode()
    series_info = json.loads(data)
    #print("Fetched data:")
    #print(series_info)
    return series_info

def main(min_rating):
    series_info = get_series_info("tt0060028")
    totalSeasons = int(series_info["totalSeasons"])
    for i in range(1,totalSeasons+1):
        series_info["Season_" + str(i)] = get_series_info(series_info["imdbID"],i)
    for i in range(1,totalSeasons+1):
        print("Season",i)
        print("----------")
        for episode in series_info["Season_"+str(i)]["Episodes"]:
            if float(episode["imdbRating"]) > min_rating:
                print(episode["imdbRating"],"\t",episode["Episode"],episode["Title"])
        print()
            
    #return series_info

if __name__ == "__main__":
    main()
