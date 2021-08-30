import urllib.request as ul
import json
import xmltodict
from urllib.parse import quote
from env import RiseKey


def get_rise_set(year, month, day):
    date = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)

    location = quote("광주")

    url = f"http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getAreaRiseSetInfo?location={location}&locdate={date}&ServiceKey={RiseKey}"

    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        responsedata = response.read()
        rd = xmltodict.parse(responsedata)

        rdj = json.dumps(rd)

        rdd = json.loads(rdj)

        astroevents = rdd['response']['body']['items']['item']

        rise_set = {}

        def get_info(key, name):
            time = astroevents[key]
            rise_set[name] = time[:2] + ':' + time[2:]

        get_info('sunrise', '일출')
        get_info('sunset', '일몰')
        get_info('moonrise', '월출')
        get_info('moonset', '월몰')

        return rise_set


if __name__ == "__main__":
    # execute only if run as a script
    data = get_rise_set(2021, 8, 26)
    print(data)
