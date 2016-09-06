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

def main(imdbID,min_rating):
    # get the basic series info such as title, nr of Seasons, etc.
    series_info = get_series_info(imdbID)
    total_found = 0
    if series_info["Type"] == "series":
        # get the info of all seasons
        totalSeasons = int(series_info["totalSeasons"])
        for i in range(1,totalSeasons+1):
            series_info["Season_" + str(i)] = get_series_info(series_info["imdbID"],i)
        # print all episodes that have a rating higher than min_ating
        for i in range(1,totalSeasons+1):
            print("Season",i)
            print("----------")
            for episode in series_info["Season_"+str(i)]["Episodes"]:
                if float(episode["imdbRating"]) >= min_rating:
                    total_found += 1
                    print(episode["imdbRating"],"\t",episode["Episode"],episode["Title"])
            print()
        print(series_info["Title"],"(" + series_info["Year"] + ")",
                "has",total_found,"episodes with rating >=",str(min_rating) + ".")
    else:
        print("Warning:",imdbID,"refers to",series_info["Title"],"(" + series_info["Year"] + ")")
        print("Error: Unable to display episodes for","'" + series_info["Type"] + "'","object.")
            
    #return series_info

if __name__ == "__main__":
    main()
