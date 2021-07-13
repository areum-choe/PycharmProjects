! pip install requests

import requests
res = requests.get("http://google.com")
res.raise_for_status()
print("응답코드:",res.status_code)
print(len(res.text))
