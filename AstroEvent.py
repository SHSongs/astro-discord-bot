import urllib.request as ul
import json
import xmltodict
from urllib.parse import quote
from env import AstroEventKey


year = 20210826

location=quote("광주")

url = f"http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getAreaRiseSetInfo?location={location}&locdate={year}&ServiceKey={AstroEventKey}"

print(type(url))
# 데이터를 받을 url

request = ul.Request(url)
# url의 데이터를 요청함

response = ul.urlopen(request)
# 요청받은 데이터를 열어줌

rescode = response.getcode()
# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음
    rD = xmltodict.parse(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    # dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    # json형식의 데이터를 dict 형식으로 변환

    print(rDD)
    # 정상적으로 데이터가 출력되는지 확인

    print(type(rDD))

    astroEvents = rDD['response']['body']['items']['item']


    for i in astroEvents:
        print(i)