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

PATH = 'C:\\Users\\Administrator\\Desktop\\IEDriverServer.exe'
transaction_list = get_balance(PATH, '계좌번호', '계좌 비밀번호4자리', '생년월일6자리')

for t in transaction_list:
    print(t)
```

위에서 받은 `IEDriverServer.exe`의 위치(절대경로)를 첫 인자로 하고 계좌번호와 비밀번호, 생년월일 6자리를 입력하면 아래와 같은 dict로 이루어진 list가 나옵니다.

> 유의: 경로 입력시 `\`는 `\\`로 입력해주셔야 제대로 escaping이 됩니다.

```json
[{'date': datetime.datetime(2017, 9, 5, 18, 3, 52), 'amount': -1250, 'balance': 114645, 'transaction_by': 'KB카드출금'}, ...]
```

date는 datetime 객체, amount는 입금이면 +int, 출금이면 -int, balance는 현재 계좌 잔고 int, transaction_by는 은행에 찍히는 거래소(입금자명 등)입니다.

## 발전계획

이전 거래내역과 다른, 새로운 거래내역을 발견시 DB를 업데이트해주는 Django App으로 발전해나가는 것도 고려중입니다.
