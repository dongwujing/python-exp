import requests
import json

# 读取题目信息
url = 'http://yi.sunlands.com/portal-tiku/tiku/pcChapterExercise/getLastNodeQuestions'
headers = {'content-type': 'application/json',
           'cookie': 'Hm_lvt_042f1b4fd18a22ee217f0673c4c1b92f=1645755902; compatible3357615=1; fun3357615=reviewDivSub%3B5738712; userTicket=ST-3285113-kfUXIItmwwfj7qnMh2Ha-cas; Hm_lpvt_042f1b4fd18a22ee217f0673c4c1b92f=1647842734'
            }
data_json = {
    "resetFlag": 0,
    "start": -1,
    "studentId": 3357615,
    "lastLevelNodeId": 197702
}
res = requests.post(url=url, data=json.dumps(data_json), headers=headers)

simWords = res.json()

print(simWords)
