
from datetime import timedelta
from datetime import date

"""
객체를 반복하려고 하면 파이썬은 해당 객체의 iter() 함수를 호출한다.
즉, 해당 객체에 __iter__ 메서드가 있는지를 확인한다.
iter()함수는 초기 루프 시작할 때 실행되고, 그 뒤로는 next() 함수가 실행된다

- for 루프가 앞서 만든 객체를  사용해 새로운 반복을 시작한다
- 파이썬은 iter() 함수를 호출한다
- iter() 함수는 __iter__ 매직 메서드를 호출한다
- __iter__ 함수는 self(자기 자신)를 반환한다
- for 루프는 이터러블 객체의 next() 함수를 호출한다
- next() 함수는 다시 __next__ 메서드를 호출한다(위임한다)
- StopIteration 예외가 발생할 때까지 next()를 호출한다
"""

class DateRangeIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

print("이터러블")
r1 = DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5))
for day in r1:
    print(day)

print("2번째 호출")
for day in r1:
    print(day)

class DateRangeIterable_container:
    """컨테이너 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

print("")
print("컨테이너 이터러블")
r2 =  DateRangeIterable_container(date(2019, 1, 1), date(2019, 1, 5))
for day in r2:
    print(day)

print("2번째 호출")
for day in r2:
    print(day)