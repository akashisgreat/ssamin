import requests
from bs4 import BeautifulSoup

cookies = {
    'AspxAutoDetectCookieSupport': '1',
    'ASP.NET_SessionId': 'vz5kx2z5njj3o1n2b4mdauad',
    '__AntiXsrfToken': '8580051330ac41e6b0f540d6d57fe242',
    'user_info': 'USER_NAME=AEN07007&Role=AMN',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'AspxAutoDetectCookieSupport=1; ASP.NET_SessionId=vz5kx2z5njj3o1n2b4mdauad; __AntiXsrfToken=8580051330ac41e6b0f540d6d57fe242; user_info=USER_NAME=AEN07007&Role=AMN',
    'origin': 'https://dlrs.bihar.gov.in',
    'priority': 'u=0, i',
    'referer': 'https://dlrs.bihar.gov.in/bsap/bs/PrapatraEntry/amin_dairy.aspx',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

data = {
    'ContentPlaceHolder1_ToolkitScriptManager1_HiddenField': '',
    '__LASTFOCUS': '',
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUKMTA4NTYyODk3Mw9kFgJmD2QWAgIDD2QWCAIBDzwrAA0BDBQrAAkFHzA6MCwwOjEsMDoyLDA6MywwOjQsMDo1LDA6NiwwOjcUKwACFgQeBFRleHQFAXweClNlbGVjdGFibGVoZBQrAAIWBh4FVmFsdWUFATEfAAUESG9tZR4LTmF2aWdhdGVVcmwFGlByYXBhdHJhRW50cnkvZGVmYXVsdC5hc3B4ZBQrAAIWBB8ABQF8HwFoZBQrAAIWBh8CBQEyHwAFBUVudHJ5HwFoFCsADQUxMDowLDA6MSwwOjIsMDozLDA6NCwwOjUsMDo2LDA6NywwOjgsMDo5LDA6MTAsMDoxMRQrAAIWBh8CBQIyMR8ABQlQcmFwYXRyLTEfAwUcUHJhcGF0cmFFbnRyeS9QcmFwYXRyYTEuYXNweGQUKwACFgYfAgUCMjIfAAUJUHJhcGF0ci0yHwMFG1ByYXBhdHJhRW50cnkvcHJhcHRyYTIuYXNweGQUKwACFgYfAgUCMjMfAAUJUHJhcGF0ci0zHwMFIlByYXBhdHJhRW50cnkvcHJhcGF0cmEzYWZ0ZXIyLmFzcHhkFCsAAhYGHwIFAjI1HwAFDFByYXBhdHItMygyKR8DBR5QcmFwYXRyYUVudHJ5L3ByYXBhdHJhM18yLmFzcHhkFCsAAhYGHwIFAjI2HwAFCVByYXBhdHItNB8DBRxQcmFwYXRyYUVudHJ5L1ByYXBhdHJhNC5hc3B4ZBQrAAIWBh8CBQIyOB8ABQlQcmFwYXRyLTYfAwUcUHJhcGF0cmFFbnRyeS9QcmFwYXRyYTYuYXNweGQUKwACFgYfAgUDMTM5HwAFCVA2IERlbGV0ZR8DBSdQcmFwYXRyYUVudHJ5L2RlbGV0ZXByYXB0cmE2aG9sZGVyLmFzcHhkFCsAAhYGHwIFAzE1NR8ABRtQcmFwYXJhLTYgRGVsZXRlIEFmdGVyIExvY2sfAwUsUHJhcGF0cmFFbnRyeS9kZWxldGVwcmFwdHJhNmhvbGRlcl9yZXNzLmFzcHhkFCsAAhYGHwIFAzE1Nx8ABQpBbWluIERpYXJ5HwMFHVByYXBhdHJhRW50cnkvYW1pbl9kYWlyeS5hc3B4ZBQrAAIWBh8CBQMyMjAfAAUKR3JhbSBTYWJoYR8DBSJQcmFwYXRyYUVudHJ5L2dyYW1hYmhpbGVraG5ldy5hc3B4ZBQrAAIWBh8CBQMyMjIfAAUYUHJhcGF0ci01IEVudHJ5IE5ldyBGb3JtHwMFKlByYXBhdHJhRW50cnkvcHJhcGF0cmE1X25ld2VudHJ5XzIwMjQuYXNweGQUKwACFgYfAgUDMjI2HwAFGEJodWtoYW4gU2FtYmFuZGhpdCBFbnRyeR8DBSFQcmFwYXRyYUVudHJ5L2NzX3JzX3RlbXBsZXQxLmFzcHhkFCsAAhYEHwAFAXwfAWhkFCsAAhYGHwIFATMfAAUGVXBkYXRlHwFoFCsABAULMDowLDA6MSwwOjIUKwACFgYfAgUDMTQ5HwAFEVByYXBhdHJhLTYgVXBkYXRlHwMFJVByYXBhdHJhRW50cnkvcDZ1cGRhdGlvbl9kZXRhaWxzLmFzcHhkFCsAAhYGHwIFAzE1Nh8ABSJQcmFwYXRyYS02IFVwZGF0ZSBBZnRlciBQcmFwYXRhLTE0HwMFLlByYXBhdHJhRW50cnkvcDZ1cGRhdGlvbl9kZXRhaWxzX2FmdGVyXzE0LmFzcHhkFCsAAhYGHwIFAzE5NR8ABSVQcmFwYXRyYS02IFVwZGF0aW9uIEFmdGVyIFByYXBhdHJhLTIxHwMFLlByYXBhdHJhRW50cnkvcDZ1cGRhdGlvbl9kZXRhaWxzX2FmdGVyXzIwLmFzcHhkFCsAAhYEHwAFAXwfAWhkFCsAAhYGHwIFATUfAAUGUmVwb3J0HwFoFCsABwUXMDowLDA6MSwwOjIsMDozLDA6NCwwOjUUKwACFgYfAgUCNTYfAAUJUHJhcGF0ci00HwMFGFBQUmVwb3J0L3ByYXBhdHJhLTQuYXNweGQUKwACFgYfAgUCNTcfAAUJUHJhcGF0ci01HwMFIVBQUmVwb3J0L01hdXphU2VsZWN0LmFzcHg/cmVwTm89NWQUKwACFgYfAgUDMTM4HwAFLFByYXBhdHJhLTYgT2xkIGtoYXRhIEtoZXNyYSBVcGRhdGUgaW4gUmVwb3J0HwMFJ1ByYXBhdHJhRW50cnkvcDZvbGRraGF0YWtoZXNyYV9kdGwuYXNweGQUKwACFgYfAgUDMTQwHwAFFlA2IE1pc3NpbmcgUGxvdCBEZXRhaWwfAwUmUFBSZXBvcnQvUHJhcGF0cmEtNi1NaXNzaW5nUmVwb3J0LmFzcHhkFCsAAhYGHwIFAzE0Nh8ABR9QcmFwYXRyYS02IHBoeXNpY2FsIGxheWVyIENoZWNrHwMFLFBQUmVwb3J0L1ByYXBhdHJhLTYtTWlzc2luZ1BoeXNpY2FsbHllci5hc3B4ZBQrAAIWBh8CBQMyMDMfAAUbUDYgUmVwb3J0IFByaW50IEtoZXNyYSBXaXNlHwMFIFBQUmVwb3J0L3A2cmVwb3J0d2l0aF9yYW5nZS5hc3B4ZGQCAw8PFgIfAAULQUtBU0ggS1VNQVJkZAIFDw8WAh8ABQZSb2h0YXNkZAIJD2QWAgIDD2QWHgIBD2QWGAIBDxAPFgYeDkRhdGFWYWx1ZUZpZWxkBQRjb2RlHg1EYXRhVGV4dEZpZWxkBQhkaXN0cmljdB4LXyFEYXRhQm91bmRnZBAVAgotLVNlbGVjdC0tBlJPSFRBUxUCATACMzIUKwMCZ2cWAQIBZAIFDxAPFgYfBAUGY2lyX2lkHwUFBmNpcmNsZR8GZ2QQFQIKLS1TZWxlY3QtLQtBa29yaGkgR29sYRUCATABOBQrAwJnZxYBAgFkAgkPEA8WBh8EBQhzaGl2aXJpZB8FBQZzaGl2aXIfBmdkEBUCCi0tU2VsZWN0LS0OQUtPUkhJIEdPTEEgMDEVAgEwAzczNhQrAwJnZxYBAgFkAg0PEA8WBh8EBQhtYXVqYV9pZB8FBQptYXVqYV9uYW1lHwZnZBAVBgotLVNlbGVjdC0tBkFrb3JoaQxCaXNlbmkgS2FsYW4MR29iYXJkaGFucHVyB0thcm1haGkFTmltYW4VBgEwBDExNTgEMTE4MAQxMTY3BDExNzcEMTE4MxQrAwZnZ2dnZ2cWAQICZAIRDw8WAh8AZWRkAhcPDxYYHg1Gb250X092ZXJsaW5laB4ORm9udF9VbmRlcmxpbmVoHgJUUgUBUh4ORm9udF9TdHJpa2VvdXRoHgJUVGUeBF8hU0ICgPwDHgtGb250X0l0YWxpY2geCUZvbnRfQm9sZGgeCkZvbnRfTmFtZXNkHglGb250X1NpemUoKiJTeXN0ZW0uV2ViLlVJLldlYkNvbnRyb2xzLkZvbnRVbml0AB4CVEUFAUUeAlRWBQFWZGQCGQ8QZGQWAWZkAhsPDxYCHwAFBDIwMjVkZAIdDw8WAh8ABQExZGQCHw8PFgIfAAUFZGF5XzlkZAIhDxAPFgIeB0NoZWNrZWRoZGRkZAIlDxAPFgIfE2hkZGRkAgMPZBYGAgEPDxYCHwBlZGQCAw8PFgIfAGVkZAIFDw8WAh8AZWRkAgUPZBYEAgMPDxYCHwBlZGQCBQ8PFgIfAGVkZAIHD2QWBAIBDw8WAh8AZWRkAgMPDxYCHwBlZGQCCQ9kFgQCAQ8PFgIfAGVkZAIDDw8WAh8AZWRkAgsPZBYEAgEPDxYCHwBlZGQCAw8PFgIfAGVkZAIND2QWBAIBDw8WAh8AZWRkAgMPDxYCHwBlZGQCDw9kFgQCAQ8PFgIfAGVkZAIDDw8WAh8AZWRkAhEPZBYEAgEPDxYCHwBlZGQCAw8PFgIfAGVkZAITD2QWBAIBDw8WAh8AZWRkAgMPDxYCHwBlZGQCFQ9kFgQCAQ8PFgIfAGVkZAIDDw8WAh8AZWRkAhkPZBYGAgEPDxYCHwBlZGQCAw8PFgIfAGVkZAIFDxBkZBYBZmQCGw9kFgQCAQ8PFgIfAGVkZAIDDw8WAh8AZWRkAiEPZBYIAgEPDxYCHwBlZGQCAw8PFgIfAGVkZAIFDw8WAh8AZWRkAgcPDxYCHwBlZGQCIw9kFgQCAQ8PFgIfAGVkZAIDDw8WAh8AZWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBSNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJENoZWNrQm94MQUjY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRDaGVja0JveDJymokwgXoK03QFn4+B1Tr73cuyMy1CXXMnlKKoxZ2Wcg==',
    '__VIEWSTATEGENERATOR': '49F317A1',
    '__EVENTVALIDATION': '/wEdACzHQ7tUKU7sv6bPOTx+YI2TkD3JDx7FXCo1/JSNBxNejPA3qyS6lKtIIyMIlR8QkCtXZS8Sw6kfSptOdJlwOi8syxcXQ6ZHDBiaDrQ5+avuOO8/DyL8NluixW4fHDrgGT8Z6IIG1mv3it+sfhvyGU2eZUsDKJnJrto4G0cOXHOpVxpInPBGJCUrCKJs2LlsPD0VCD5uvNoQFW5/jnbHm2lRkEQC7wRhVrDuzWwCxK9kJFfgYkdbGzBa6M0fWeKHRjeMh0jJ/UkenfgytzMLS4q8/6w0fBWWBbtj0vBBEVt0QBRhEEsQmvrj/Qva8mqP69crtIZ26v6yuivdf5F+aGsw/biJJwpvruzKau3+L7prfSItO3lFMM/WYWK4gMNUxNb/eG47B3PvBDl3JGSjDhRp1r/jBs+JMlCvF7E1zcO24aQLqlTNKdoCZy1ScQlySyFLb4DFRpERzhw/O/hKyb5+naZjtqRgDTmPyMY/nWM9ogF/dNjb90PQ498GrYj9afOeVeolRbieDLC30s60IpP6fb/T2DMv8PYSnc+vJYVXD/hGqTL4S+PZW61qSzF6GU+ONvxiSi4M5bezTpd8EbZhl27SsMP+d4uKTJikzp08PoX87SKHqYya3lGtpXJzX3R4zAMarka8v0LtGsx6+jQhErQEtD8VLAoUcsqt3QTRNkwK7NjiRgFiYwRtHwQJb3QrBd5kBYY+8vEaWPEMD+YCFIC7K7DbCMhzGDWZ2HqfqKTEyeSZiZrkHTTPTjGqQblXfE3f12EUyfcPBqDvCsLwuGeuwDlP5M4cy1el9z/ag4kHj7KsGQZ9KI/q0cgR79ct2bZ0SCx1IenWuWq+e7bvkXMiQv+1Ib/KVLk8EXJ2SgY9OC2yZrn5wyC0AJT5W0QCAU5IxSxlwFLVkmISOJhoVxO7ONN2L+tqN9f8f+J/zYMt7FuPFnJERKIqEm8NZ13qfQeVfPD0br+kdbYpX9k9',
    'ctl00$ContentPlaceHolder1$DropDownListdist': '32',
    'ctl00$ContentPlaceHolder1$DropDownListcircle': '8',
    'ctl00$ContentPlaceHolder1$DropDownListshivir': '736',
    'ctl00$ContentPlaceHolder1$DropDownListmauza': '1180',
    'ctl00$ContentPlaceHolder1$txtthana': '',
    'ctl00$ContentPlaceHolder1$txtDate': '16-01-2025',
    'ctl00$ContentPlaceHolder1$DropDownList1': '0',
    'ctl00$ContentPlaceHolder1$txtyear': '2025',
    'ctl00$ContentPlaceHolder1$txtmonth': '1',
    'ctl00$ContentPlaceHolder1$txtday': 'day_9',
    'ctl00$ContentPlaceHolder1$TextBox1': '09-06-2022',
    'ctl00$ContentPlaceHolder1$TextBox2': '11-06-2022',
    'ctl00$ContentPlaceHolder1$txtdabaaapti': '_। आज दिनांक 16/01/2025 को शिविर कार्यालय मे उपस्थित हो कर बिसेनीकला, गोवर्धनपुर, करमाही, नीमा मौजा का प्रपत्र 3 और प्रपत्र 4 का सत्यापन किया एवं वांसवाली की सूची बनाई \r\nकुल खेसरो की संख्या: 219\r\n\r\nबिसेनीकला ग्राम का प्रपत्र 5 की एंट्री की \r\nप्रपत्र 5 की एंट्री की गई खेसरो की संख्या: 4',
    'ctl00$ContentPlaceHolder1$txtdabaaaptitotal': '219',
    'ctl00$ContentPlaceHolder1$btnsave': 'Save',
}

response = requests.post(
    'https://dlrs.bihar.gov.in/bsap/bs/PrapatraEntry/amin_dairy.aspx',
    cookies=cookies,
    headers=headers,
    data=data,
)




if response.status_code == 200:
    resp = response.text
    soup = BeautifulSoup(resp, 'html.parser')
  
    # if "Amin dairy save successfully" in soup.text:
    if "Amin Dairy Save Successfully." in soup.text:
        print("Text 'Amin dairy save successfully' found in the response.")
    else:
        print("Text 'Amin dairy save successfully' not found in the response.")


else:
    print(f"Request failed with status code: {response.status_code}")
