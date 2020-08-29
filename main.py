import json
from urllib.parse import quote, quote_plus

data = {'detail_v': '3.3.2', "exParams": {"item_id": 601664142715, "from": "search"}}

json_data = json.dumps(data)
print(json_data)
print(quote(json_data))
