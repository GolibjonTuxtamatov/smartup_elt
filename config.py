import base64
import json

with open('auth.json','r',encoding='utf-8') as file:
    data = json.load(file)

_login = data['SMARTUP_LOGIN']
_password = data['SMARTUP_PASSWORD']
_project_code = data['SMARTUP_PROJECT_CODE']
_filial_id = data['SMARTUP_FILIAL_ID']

# endpoints
ENDPOINTS = {
    "inventory": "https://smartup.online/b/anor/mxsx/mr/inventory$export",
    "legal_person": "https://smartup.online/b/anor/mxsx/mr/legal_person$export",
    "natural_person": "https://smartup.online/b/anor/mxsx/mr/natural_person$export",
    "order": "https://smartup.online/b/trade/txs/tdeal/order$export",
    "cashin": "https://smartup.online/b/trade/txs/tcs/cashin$export",
    "cash_operation": "https://smartup.online/b/anor/mxsx/mkcs/cash_operation$export",
    "bank_operation": "https://smartup.online/b/anor/mxsx/mkcs/bank_operation$export"
}




def get_headers() -> dict:
    encode = base64.b64encode(f"{_login}:{_password}".encode()).decode()

    return {
        'Authorization': f"Basic {encode}",
        'project_code': _project_code,
        'filial_id': _filial_id
    }
