import json
import requests
# import pandas
# def get_data():

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-FDA1EAB2-E1DE-4F0C-8E41-7026A551403E&locationName=%E8%87%BA%E5%8D%97%E5%B8%82"
params = { "Authorization": "CWB-FDA1EAB2-E1DE-4F0C-8E41-7026A551403E",
    "locationName": "%E8%87%BA%E5%8D%97%E5%B8%82"

}

response = requests.get(url, params=params)
print(response.status_code)

if response.status_code == 200:
    print(response.text)
    data = json.loads(response.text)

    location = data["records"]["location"][0]["locationName"]
    weather_elements = data["records"]["location"][0]["weatherElement"]
    weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
    rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
    min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
    max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

    print(location)
    print(weather_elements)
    print(weather_state)
    print(rain_prob)
    print(min_tem)
    print(max_tem)

else:
    print("Can't get data!")


######################line######################
def line_notify():

    token = "kkpN8FrEG1wfMoDVc2NbuETr30MlfSs1rLnRh0vX3jR"
    message = ""

    if len(data) == 0:
        message += "\n[Error] 無法取得天氣資訊"
    else:
        message += "今天"+location+"ㄟˊ天氣："+weather_state+"\n"
        message += "溫度："+min_tem+"°C~"+max_tem+"°C"+"\n"
        message += "降雨機率："+rain_prob+"%"+"\n"

        if int(rain_prob) > 70:
            message += "提醒您，今天很有可能會下雨，出門記得帶把傘哦!"
        elif int(max_tem) > 33:
            message += "提醒您，今天很熱，外出要小心中暑哦~"
        elif int(min_tem) < 10:
            message += "提醒您，今天很冷，記得穿暖一點再出門哦~"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)
# if __name__ == '__main__':
line_notify()

######################line######################
