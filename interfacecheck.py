#!/usr/local/python/bin/python3


import requests


if __name__=="__main__":
    response=requests.post("http://127.0.0.1:8080/shibor/report",
        {'term':'oneNight',fromDate='2017-04-01','toDate':'2018-01-01'}
    )