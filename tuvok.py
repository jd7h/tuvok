#!/usr/bin/python3
import json
import urllib.request

def get_series_info(series):
    url = "http://www.omdbapi.com/?i="
    print(url + series)
    try:
        conn = urllib.request.urlopen(url + series)
    except:
        print("Error:",series,"not found in OMDB")
        return ""
    data = conn.read().decode()
    print(data)
    series_info = json.loads(data)
    print(series_info)
    return series_info

def main():
    get_series_info("tt0060028")

if __name__ == "__main__":
    main()
