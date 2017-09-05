# KB 국민은행 계좌 조회

## 왜 만들었나요?

KB국민은행에서 작년 '빠른조회'서비스 사이트가 변경되어 기존에 Github에 돌아다니던 조회 도구가 무용지물이 되어,
Selenium을 사용한 크롤링 도구를 간단하게 만들었습니다.

## 제약

현재 국민은행에서는 크롬등의 AX가 지원되지 않는 브라우저는 '가상키보드'를 사용합니다.
IE에서는 가상키보드를 사용하지 않고 Selenium의 `send_keys` 메소드를 사용해 입력을 받기 때문에 기존 코드 그대로 사용이 가능합니다.
하지만 IE의 제약으로 인해 프로그램이 Windows상에서 구동되어야한다는 문제점이 있습니다.

이 패키지는 파이썬 3.5 이상에서 사용가능합니다.

## 설치법

우선 pip로 받아주세요.

```
pip install kb-transaction
```

다음으로는 윈도에서 돌아갈 Selenium StandAlone Server가 필요합니다.

[http://docs.seleniumhq.org/download/](http://docs.seleniumhq.org/download/)에서 받아주세요. [바로받기](https://goo.gl/hWYjHR)

Selenium을 구동할 때 이 서버는 항상 켜져있어야 합니다.(IE라서...)

위 사이트에서 `Internet Explorer Driver`도 받아줘야 합니다. 32비트 버전을 받아주세요. [바로받기](https://goo.gl/BbeFgE)

> 64비트 버전을 사용해도 되지만 `send_keys()`가 무척 느려지는 이슈가 있어 사용을 권장하지 않습니다.

## 사용법

```python
from kb_transaction.crawler import get_balance

transaction_list = get_balance('계좌번호', '계좌 비밀번호4자리', '생년월일6자리')

for t in transaction_list:
    print(t)
```
