import hashlib
import requests


def api_search(text):
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

    payload = {
        'q': text,
        'from': 'en',
        'to': 'zh',
        'appid': '20220427001193361',
        'salt': '1',
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
    }

    key = 'IHAVydIsj32EFKqlzTdG'

    key = hashlib.md5(
        (payload['appid'] + str(payload['q']) + payload['salt'] + key).encode(encoding='UTF-8')).hexdigest()
    payload['sign'] = key
    # print(key)

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.json())
    return response.json()['trans_result'][0]['dst']


'''
def api_search(text):
    t = time.time()

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "q=" + text + "&target=zh-CN&source=en"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X-RapidAPI-Key": "7c44ea8b16msh1c1d6d3a879d693p1b69bbjsnb15b94ddbf6d"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()

    out = data['data']['translations'][0]['translatedText']
    t = time.time() - t
    print(t)
    return out
'''
