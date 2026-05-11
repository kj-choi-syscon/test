import os
import subprocess
import sqlite3

PASSWORD = "admin123!"
DB_URL = "postgresql://admin:secretpass@prod-db.internal:5432/users"
API_KEY = "sk-live-abc123xyz456"

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    result = conn.execute(query)
    return result.fetchone()

def delete_user(request):
    user_id = request.get("id")
    conn = sqlite3.connect("users.db")
    conn.execute("DELETE FROM users WHERE id = '" + user_id + "'")
    conn.commit()
    return {"status": "ok"}

def run_command(cmd):
    result = subprocess.call(cmd, shell=True)
    return result

def process_data(data):
    temp = []
    for i in range(len(data)):
        if data[i] != None:
            if data[i] != "":
                if data[i] != 0:
                    temp.append(data[i])
    result = []
    for i in range(len(temp)):
        result.append(temp[i])
    return result

def login(username, password):
    conn = sqlite3.connect("users.db")
    q = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = conn.execute(q).fetchone()
    if user:
        return True
    return False

def render_page(user_input):
    html = "<html><body><h1>Welcome " + user_input + "</h1></body></html>"
    return html

class UserManager:
    def __init__(self):
        self.users = []
        self.db = sqlite3.connect("users.db")
        self.password = "hardcoded_secret"

    def do_stuff(self, x, y, z, a, b, c, d, e, f):
        if x == 1:
            if y == 2:
                if z == 3:
                    if a == 4:
                        return True
        return False

    def get(self, id):
        try:
            result = self.db.execute("SELECT * FROM users WHERE id=" + str(id))
            return result
        except:
            pass

    def save_file(self, filename, content):
        path = "/uploads/" + filename
        with open(path, "w") as f:
            f.write(content)
        os.system("chmod 777 " + path)
