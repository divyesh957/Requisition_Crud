import requests,json
api_key = 'b0aa032f-e8b8-43e9-aef4-1b127a8043cb'
account_id = 'f5b23aa83740/d87f391d-b63c-43a3-ad18-df9b107859ff'


def get_profile_idfy():
    """
    :return:
    """
    while True:
        try:

            url = "https://api.kyc.idfy.com/profiles/75ba0200-179a-4cec-b923-c28a8259cde7"
            payload = {}
            headers = {
                'api-key': api_key,
                'account-id': account_id
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            responce = json.loads(response.content.decode('utf-8'))

            if responce['reviewer_action'] == 'rejected':
                responce = {
                    "status": "rejected",
                }
                api = requests.post('http://127.0.0.1:8000/idfy/callback', json=responce)

                url = "https://api.kyc.idfy.com/:{}".format(api)

                payload = json.dumps({
                    "reference_id": responce['reference_id'],
                    "profile_id": "75ba0200-179a-4cec-b923-c28a8259cde7",
                    "status": "rejected",
                    "status_detail": "Signatures do not match."
                })

                headers = {
                    'Content-Type': 'application/json',
                    'api-key': api_key,
                    'account-id': account_id
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
            return {
                "code": 200,
                "message": "success",
                "data": responce
            }
        except Exception as e:
            return {
                "code": 500,
                "status": "error",
                "message": " Exception {} occurred while getting create_profile_idfy.".format(e)
            }

get_profile_idfy()