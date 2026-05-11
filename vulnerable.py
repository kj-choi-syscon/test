import os
import sqlite3
import subprocess


def get_user(user_input):
    """SQL injection 취약점 + 평문 쿼리"""
    conn = sqlite3.connect("db.sqlite")
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return conn.execute(query).fetchall()


def delete_user(request):
    """인증 없음 + SQL injection"""
    conn = sqlite3.connect("db.sqlite")
    user_id = request.get("id")
    conn.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()


def run_cmd(cmd):
    """명령어 인젝션 취약점"""
    return os.system(cmd)


def run_cmd_v2(user_cmd):
    """또 다른 인젝션 취약점"""
    return subprocess.call(user_cmd, shell=True)


def process_data(items):
    """O(n^2) 비효율 로직"""
    result = []
    for i in items:
        for j in items:
            if i == j:
                result.append(i)
    return result


def do_stuff(a, b, c, d, e, f, g):
    """함수 이름 불명확 + 인자 과다"""
    if a:
        if b:
            if c:
                if d:
                    if e:
                        return f + g
    return None


def read_file(filename):
    """경로 조작(path traversal) 가능"""
    path = "/var/uploads/" + filename
    with open(path) as f:
        return f.read()


def auth(username, password):
    """평문 비밀번호 + SQL injection"""
    conn = sqlite3.connect("db.sqlite")
    q = f"SELECT * FROM users WHERE name='{username}' AND pw='{password}'"
    return conn.execute(q).fetchone()


def silent_failure():
    """예외 무시 (silent failure)"""
    try:
        risky_operation()
    except Exception:
        pass


def risky_operation():
    pass


# 하드코딩된 비밀번호와 API 키
DB_PASSWORD = "admin1234"
SECRET_KEY = "sk-prod-xxxxxxxxxxxxx"
