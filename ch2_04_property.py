"""
프로퍼티는 명령-쿼리 분리 원칙(command and query separation - CC08)을 따르기 위한 좋은 방법이다
(https://en.wikipedia.org/wiki/Command%E2%80%93query_separation)
이 분리 원칙은 객체의 메서드가 무언가의 상태를 변경하는 커맨드이거나 무언가를 반환하는 쿼리이거나
둘 중에 하나만 수행해야지 둘 다 동시에 수행하면 안된다는 것이다

자바와 같은 프로그래밍 언어에서는 접근 메서드(getter, setter)를 만들지만
파이썬에서는 프로퍼티를 사용한다

프로퍼티를 사용하면 get_, set_ 접두어로 된 메서드를 만드는 것보다 훨씬 더 간단하다
단, 프로퍼티는 속성 값을 가져오거나 수정할 때 특별한 로직이 필요한 경우에만 사용하는게 좋다
사실, 대부분의 경우 일반 속성으로 처리가 가능하다
"""

import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")

def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None

class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    # 프로퍼티는 private속성인 email을 반환한다    
    @property
    def email(self):
        return self._email
    
    # <user>.email = <new_email> 이 실행될 때 호출되는 코드
    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"유효한 이메일이 아니므로 {new_email} 을 사용할 수 없음")
        self._email = new_email


u1  = User("jsmith")
u1.email = "jsmith@" # setter 프로퍼티 실행

u1.email = "jsmith@g.co" # setter 프로퍼티 실행
print(u1.email) # 프로퍼티 실행