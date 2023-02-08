from flask import *
from models.models import *
from models.database import db_session


def ocr(p, s, r):
    with open(imFilePath, 'rb') as f:
        data= f.read()

    # https://{endpoint}/vision/v3.2/read/analyze[?language][&pages][&readingOrder][&model-version]


        subscription_key = "2d0fb6843c024fc680cf387aa7846dd7"
        endpoint = "https://preocr123456.cognitiveservices.azure.com/"
        text_recognition_url = endpoint + "vision/v3.2/read/analyze"
        headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
        params = {'language ': 'ja',
                'model-version': 'latest'}

        # 指定した画像の read メソッドを呼び出します。これによって operation ID が返され、画像の内容を読み取る非同期プロセスが開始されます
        response = requests.post(text_recognition_url,
                                headers=headers, params=params, json=None, data=data)
        response.raise_for_status()

        # レスポンスから operation location（末尾にIDが付いたURL）を取得する
        operation_url = response.headers["Operation-Location"]
        analysis = {}
        poll = True

        # read の呼び出しから返された operation location ID を取得し、操作の結果をサービスに照会します。
        # 次のコードは、結果が返されるまで 1 秒間隔で操作をチェックします
        while (poll):
            response_final = requests.get(
                response.headers["Operation-Location"], headers=headers)
            analysis = response_final.json()

            print(json.dumps(analysis, indent=4, ensure_ascii=False))

            time.sleep(1)
            if ("analyzeResult" in analysis):
                poll = False
            if ("status" in analysis and analysis['status'] == 'failed'):
                poll = False
