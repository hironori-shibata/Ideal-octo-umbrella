from flask import *
from models.models import *
from models.database import db_session
import requests
import time
import difflib

def ocr(s, r):
    r="images/"+r
    with open(r, 'rb') as f:
        data= f.read()

    # https://{endpoint}/vision/v3.2/read/analyze[?language][&pages][&readingOrder][&model-version]


        subscription_key = "2d0fb6843c024fc680cf387aa7846dd7"
        endpoint = "https://preocr123456.cognitiveservices.azure.com/"
        text_recognition_url = endpoint + "vision/v3.2/read/analyze"
        headers = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type': 'application/octet-stream'}
        params = {'language ': 'ja','model-version': 'latest'}

        # 指定した画像の read メソッドを呼び出します。これによって operation ID が返され、画像の内容を読み取る非同期プロセスが開始されます
        response = requests.post(text_recognition_url,headers=headers, params=params, json=None, data=data)
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

            #print(json.dumps(analysis, indent=4, ensure_ascii=False))

            time.sleep(1)
            if ("analyzeResult" in analysis):
                poll = False
            if ("status" in analysis and analysis['status'] == 'failed'):
                poll = False
        return analysis


def classfy(analysis):
    text=analysis["analyzeResult"]["readResults"][0]["lines"]
    books=[]
    count_f=0
    for li in text:

        words=li["words"]
        fxy=words[0]["boundingBox"]
        leng=len(words)-1
        lxy=words[leng]["boundingBox"]
        la=10**10 if fxy[0]==lxy[6] else (fxy[1]-lxy[7])/(fxy[0]-lxy[6])
        
        lb=lxy[7]-la*lxy[6]
        ra=10**10 if fxy[2]==lxy[4] else (fxy[3]-lxy[5])/(fxy[2]-lxy[4])
            
        rb=lxy[5]-ra*lxy[4]
        count_r=0
        boo=[]
        if ra<3 and ra>-3:
            
            la=10**10 if fxy[0]==fxy[6] else (fxy[1]-fxy[7])/(fxy[0]-fxy[6])
            lb=fxy[7]-la*fxy[6]
            ra=10**10 if lxy[2]==lxy[4] else (lxy[3]-lxy[5])/(lxy[2]-lxy[4])
            rb=lxy[5]-ra*lxy[4]
        if -0.5<ra<0.5 or -0.5<la<0.5:
            books.append([count_f])
            count_f+=1
            continue

            
        
        for s in text:
            ran=s["words"][0]["boundingBox"]
            y=(ran[1]+ran[3])/2
            x=(ran[0]+ran[2])/2

            leftrange=(y-lb)/la
            rightrange=(y-rb)/ra
            if leftrange<=x<=rightrange:
              boo.append(count_r)
            count_r+=1
        books.append(boo) 
        count_f+=1 
    return books
def classfy_arg(books,analysis):
    text=analysis["analyzeResult"]["readResults"][0]["lines"]
    data=[]
    length=len(text)

    m=[x for x in range(length)]
    for i in m:
        n=[f for f in books if i in f]
        temp=[]
        for g in n:
            temp.append(len(g))
        d=temp.index(max(temp))
        data.append(n[d])
    
    
    
    data=list(map(list, set(map(tuple, data))))
    #print(data)
    te=[]
    for az,t in enumerate(data):
        for d in t:
            #print(text[d]["text"])
            if d in te:
               data[az].clear()     
            te.append(d)
    label=[]
    
    for gh in data:
        raw=""
        for ew in gh:
            raw=raw+text[ew]["text"]




    
  
  

