import json
import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


MY_TOKEN = os.getenv('MY_TOKEN')
CODENATION_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + MY_TOKEN

def requisicao_post:
    multipart_data = MultipartEncoder(
        fields={
            # a file upload field
            'answer': ('answer', open('answer.json', 'rb'))
            # plain text fields
        }
    )
    
    response = requests.post(CODENATION_URL, data=multipart_data,
                        headers={'Content-Type': multipart_data.content_type})
    
    print(response.text)
    print(response.status_code)


resultado_final = requisicao_post()

if __name__ == '__main__':
    requisicao_post()