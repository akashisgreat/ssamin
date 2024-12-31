import requests
from bs4 import BeautifulSoup

mauja_id = [
1154,
1156,
1163,
1155,
1190,
1138,
1139,
1140,
1162,
1191,
1192,
1143,
1145,
1157,
1171,
1173,
1175,
1178,
1181,
1148,
1176,
1186,
1147,
1150,
1159,
1174,
1182,
1188,
1151,
1152,
1177,
1180,
1183,
1158,
1167,
1172,
1179,
1142,
1153,
1165,
1137,
1144,
1149,
1160,
1164,
1184,
1185,
1187,
1189,
1141,
1146,
1169,
1170,
1166,
1168,
1161
]

all_p2 = []

print("P2 Report (public portal)\n==================")

for x in mauja_id:
    cookies = {
        'AspxAutoDetectCookieSupport': '1',
        'ASP.NET_SessionId': 'iqgo13ezz5nbsi4cuvoyj21o',
        '__AntiXsrfToken': 'c3620c86809a477d801b4e4b9b0a189e',
        'user_info': 'USER_NAME=AEN07007&Role=AMN',
        '.ASPXAUTH': '06D673434AD2C76803B90126D1EC8A457FCB406FD759893F6CB156212EB2DA9F3B8675A6AB0C29D86F852D5AEBDAC280A56264DECB1BE91CE882EA35B8BB724B61528881C6E23C0C4061A46023148623DD60CAD4FFBCEE34C13A44D7F55126E92B20DF7AA1F85A67CCE2D3B72AACF2CA6A8C6F1ABF4FA1D40645426958A6285B',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://dlrs.bihar.gov.in',
        'Connection': 'keep-alive',
        'Referer': 'https://dlrs.bihar.gov.in/SurveyStatus.aspx',
        # 'Cookie': 'AspxAutoDetectCookieSupport=1; ASP.NET_SessionId=iqgo13ezz5nbsi4cuvoyj21o; __AntiXsrfToken=c3620c86809a477d801b4e4b9b0a189e; user_info=USER_NAME=AEN07007&Role=AMN; .ASPXAUTH=06D673434AD2C76803B90126D1EC8A457FCB406FD759893F6CB156212EB2DA9F3B8675A6AB0C29D86F852D5AEBDAC280A56264DECB1BE91CE882EA35B8BB724B61528881C6E23C0C4061A46023148623DD60CAD4FFBCEE34C13A44D7F55126E92B20DF7AA1F85A67CCE2D3B72AACF2CA6A8C6F1ABF4FA1D40645426958A6285B',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '/wEPDwUKLTg0NzM1MDU3Mw9kFgJmDw8WBB4PX19BbnRpWHNyZlRva2VuBSBjMzYyMGM4NjgwOWE0NzdkODAxYjRlNGI5YjBhMTg5ZR4SX19BbnRpWHNyZlVzZXJOYW1lZWQWAgIDD2QWAgIBD2QWBgIBDxAPFgYeDkRhdGFWYWx1ZUZpZWxkBQRDT0RFHg1EYXRhVGV4dEZpZWxkBQhkaXN0cmljdB4LXyFEYXRhQm91bmRnZBAVKBMtLVNlbGVjdCBEaXN0cmljdC0tBkFSQVJJQQVBUldBTApBVVJBTkdBQkFEBUJBTktBCUJFR1VTQVJBSQlCSEFHQUxQVVIHQkhPSlBVUgVCVVhBUglEQVJCSEFOR0EER0FZQQlHT1BBTEdBTkoFSkFNVUkJSkVIQU5BQkFED0tBSU1VUiAoQkhBQlVBKQdLQVRJSEFSCEtIQUdBUklBCktJU0hBTkdBTkoKTEFLSElTQVJBSQlNQURIRVBVUkEJTUFESFVCQU5JBk1VTkdFUgtNVVpBRkZBUlBVUgdOQUxBTkRBBk5BV0FEQQZPdGhlcnMSUEFTSENISU0gQ0hBTVBBUkFOBVBBVE5BD1BVUkJJIENIQU1QQVJBTgZQVVJOSUEGUk9IVEFTB1NBSEFSU0EKU0FNQVNUSVBVUgVTQVJBTgpTSEVJS0hQVVJBB1NIRU9IQVIJU0lUQU1BUkhJBVNJV0FOBlNVUEFVTAhWQUlTSEFMSRUoATABNwIzOAIzNAIyMwIyMAIyMgIyOQIzMAIxMwIzNQIxNQIzNwIzMwIzMQIxMAIyMQE4AjI1AjExATUCMjQCMTQBMQIzNgQ5OTk5AjI3AjI4ATIBOQIzMgIxMgIxOQIxNwIyNgEzATQCMTYBNgIxOBQrAyhnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnFgECHmQCAw8QDxYGHwIFBmNpcl9pZB8DBQhjaXJfbmFtZR8EZ2QQFRQKLS1TZWxlY3QtLQtBa29yaGkgR29sYQpCaWtyYW1nYW5qB0NoZW5hcmkGRGF3YXRoBURlaHJpBkRpbmFyYQdLYXJha2F0CEthcmdhaGFyBktvY2hhcwlOYXNyaWdhbmoITmF1aGF0dGEFTm9raGEGUmFqcHVyBlJvaHRhcwlTYW5qaGF1bGkHU2FzYXJhbQlTaGVvc2FnYXIJU3VyeWFwdXJhCFRpbG91dGh1FRQBMAE4AjEyATICMTMBNwIxNAIxNgEzATQCMTcCMTABNgIxOQIxMQIxOAExATUCMTUBORQrAxRnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgUPEA8WBh8EZx8CBQhtYXVqYV9pZB8DBQptYXVqYV9uYW1lZBAVOQotLVNlbGVjdC0tC0Frb3JoaSgxMzEpCkJhZ2VuKDEzOSkOQmFnaGEgS2hvaCg5NCkPQmFob3JhbnB1cigxNDEpC0JhbmRocGEoOTYpCUJhbmsoMTM2KQtCYXJ1bmEoMTMyKQ5CYXNhbnRwdXIoMTA2KQxCaXJvZGloKDEzNCkQQmlzZW5pIEthbGFuKDg4KQtCdWRodWEoMTAwKQtDaGFuZGEoMTA3KQtDaGFuZGkoMTM4KQlDaGFucCg5OSkMQ2hoYXByYSgxMDUpDUNoaGVtdWFuKDEyOSkQQ2hpdCBCaXNhd2FuKDkyKQ5EaGFyYWhhcmEoMTI4KQ1HYW1oYXJpYSgxMDgpC0dob3JhaGkoODYpEUdvYmFyZGhhbnB1cigxNDApC0hhYmJ1cHVyKDgpDUhhbWlyYWRpaCgzMSkLSGF1bmRpaCgzMCkISXNyYSg5NykJSmFkd2EoOTUpCkthaXRoaSg4NykKS2FwYXNpYSg5KQ5LYXJrYXRwdXIoMTMzKQtLYXJtYWhpKDg1KQpLYXVwYSgxMTMpC0toYXByYSgxMDQpDEt1c21oYXJhKDkxKQxNYWh1YXJpKDEwMSkPTWF0aHVyYXB1cigxNDMpDE5hd2FkaWgoMTA5KQlOaW1hbig5MCkMUGFrYXJpYSgxMDIpDFBpYXJlcHVyKDk4KQpTYWhqaSgxMjcpClNhbGVhKDEwMykMU2hlcnB1cigxMzApDlRlbmR1YmFoYXIoMTEpEVRlbnVhICBLaHVyZCgxMTIpC1RldHJhcmgoOTMpEFRld2FyaSAgRGloKDExNCkJVWdyYSgxNDIpD1pvcmF3YXJwdXIoMTM3KSTgpKTgpYfgpKjgpY3gpKbgpYHgpIbgpJXgpLLgpL4gKDExMSkZ4KSs4KSy4KS/4KSX4KS+4KS14KSBKDEwKRngpKzgpL/gpLDgpYvgpKHgpYDgpLkoODMpJeCkrOCkv+CkuOCliOCkqOCkv+CkluClgeCksOCljeCkpig4NCkZ4KSt4KS/4KSu4KSV4KSw4KWC4KSqKDg5KSDgpK7gpKfgpYHgpLDgpL7gpK7gpKrgpYHgpLAoMTM1KRrgpK7gpYHgpKHgpL/gpK/gpL7gpLAoMTEwKRPgpLjgpLDgpL7gpLXgpIEoMzIpFTkBMAQxMTU4BDExNjYEMTE4NwQxMTY4BDExODkEMTE2MwQxMTU5BDExNDQEMTE2MQQxMTgwBDExMzgEMTE0NQQxMTY1BDExOTIEMTE0MwQxMTU2BDExODUEMTE1NQQxMTQ2BDExNzgEMTE2NwQxMTc0BDExNzIEMTE3MQQxMTkwBDExODgEMTE3OQQxMTgyBDExNjAEMTE3NwQxMTUyBDExNDIEMTE4NAQxMTM5BDExNzAEMTE0NwQxMTgzBDExNDAEMTE5MQQxMTU0BDExNDEEMTE1NwQxMTQ4BDExNTEEMTE4NgQxMTUzBDExNjkEMTE2NAQxMTUwBDExMzcEMTE3NQQxMTc2BDExODEEMTE2MgQxMTQ5BDExNzMUKwM5Z2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZGRkcIkf3u5cae5+huA/6/v4ykB3zq59QHJZGTmUH+KpXSM=',
        '__VIEWSTATEGENERATOR': '037084C7',
        '__EVENTVALIDATION': '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',
        'ctl00$ContentPlaceHolder1$DropDownListdist': '32',
        'ctl00$ContentPlaceHolder1$DropDownListcircle': '8',
        'ctl00$ContentPlaceHolder1$DropDownListmauza': x,
        'ctl00$ContentPlaceHolder1$Button1': 'Click Here',
    }

    response = requests.post('https://dlrs.bihar.gov.in/SurveyStatus.aspx', cookies=cookies, headers=headers, data=data)


    if response.status_code == 200:
        # print("Response received:")
        # print(response.text)  # Or response.json() if the response is JSON
        resp = response.text
        soup = BeautifulSoup(resp, 'html.parser')
        
        mauja_name = soup.select_one("#ContentPlaceHolder1_lbl_mauja").text
        p2_no = soup.select_one("#ContentPlaceHolder1_lbl_p231_Count")
        
        mauja_name = mauja_name.replace(" मौजा/ग्राम (थाना न०/RT Num):-", "")
        
        print(mauja_name, "\t\t", p2_no.text)

        all_p2.append(int(p2_no.text))

    else:
        print(f"Request failed with status code: {response.status_code}")

print("---- Mauja Count: ", len(all_p2), " ---")
print("Total P2: ", sum(all_p2))
