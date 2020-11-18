"""
컨텍스트 관리자는 사전조건과 사후조건을 가지고 있어
파일이나 커넥션 등의 리소스 관리에 자주 사용된다
이외에도 사실상 모든 패턴에 적용하기 쉽다

메서드는 아래 두가지를 가지고 있다
__enter__ : with 구문에 진입할 때 실행한다
__exit__ : with 구무을 종료할 때 실행한다

"""
import contextlib
########################
# 1번
########################
def stop_database():
    print("systemctl stop postgresql.service")

def start_database():
    print("systemctl start postgresql.service")

class DBHandler:
    # 데이터베이스를 백업을 시작 할 때 데이터베이스를 종료한다
    def _enter__(self):
        stop_database()
        return self
    
    # 데이터베이스를 백업이 종료될 때 데이터베이스를 재시작한다
    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()
    
def db_backup():
    print("pg_dump database")


########################
# 2번
########################
@contextlib.contextmanager
def db_handler():
    # yield 문 앞에 있는 모든 것은 __enter__ 메서드의 일부처럼 취급된다
    stop_database()
    yield
    start_database()


########################
# 3번
########################
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()

@dbhandler_decorator()
def db_backup3():
    print("pg_dump database")

# 1번
def ex1():
    """
    일반적인 컨텍스트 관리자 사용 방법
    """
    with DBHandler():
        db_backup()

# 2번
def ex2():
    """
    데코레이터를 사용하여
    클래스와 독립적인 컨텍스트 관리자 함수를 만드는 방법
    """
    with db_handler():
        db_backup()

# 3번
def ex3():
    """
    데코레이터 래퍼 클래스를 사용하여
    완전히 독립적인 컨텍스트 관리자 함수 만드는 방법

    with db_backup3() as db 와 같은 as 리턴 객체를 사용할 수 없다
    (사용하려면 2번 예시를 따라야한다)
    """
    db_backup3()