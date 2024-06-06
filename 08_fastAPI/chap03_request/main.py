
# 요청 응답

# POST, PUT, PATCH 등의 메소드를 사용하는 경우 HTTP 본문(body)사용

# 단순 텍스트나 json을 이용한다.

# pydantic 으로 요청 본문 받기
# 데이터 유효성 검사 및 설정 관리를 위한 라이브러리

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class UserInfo(BaseModel):
    name : str
    password : str
            # url 은 선택사항이며, URL 형식으로 받아야 한다. 기본값은
    url : Optional[HttpUrl] = None
# UserInfo 클래스 (BaseModel 을 상속 받음)
# BaseModel 을 상속 받아야 request body 부분을 받을 클래스로 이용할 수 있음

@app.post("/users")
def createUser(user:UserInfo):
    return user