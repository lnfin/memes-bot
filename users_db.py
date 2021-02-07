import sqlite3
import os



class UsersDB:
    def __init__(self):
        self.db_name = 'data/database.db'

    def is_user_in_db(self, sn_type=None, u_id=None):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()  
        cmd = "SELECT * FROM users WHERE {} = {}".format(sn_type, u_id, )
        r = cur.execute(cmd).fetchall()
        conn.close()
        return bool(r)

    def add_user(self, sn_type=None, u_id=None):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()    
        if not self.is_user_in_db(sn_type=sn_type, u_id=u_id):
            cmd = "INSERT INTO users({}) VALUES ({})".format(sn_type, u_id)
            cur.execute(cmd)
            conn.commit()
        conn.close()

    def get_matches(self, sn_type=None, u_id=None, test_r = None):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()    
        users_test = test_r
        print(users_test)
        
        cmd="SELECT * FROM users".format()
        matches = cur.execute(cmd).fetchall()
        counter = []
        for m in matches:
            if not m[-1]:
                continue
            ids = m[1:3]
            if u_id in ids:
                continue
            test = [int(n) for n in m[-1].split()]
            c = 0
            print("test ",test)
            for i in range(len(users_test)):
                if users_test[i] == test[i]:
                    c += 1
            counter.append((ids, c))
        counter.sort(key=lambda x: x[1], reverse=True)
        conn.close()
        print(counter, counter[5:])
        return counter

    def add_test_results(self, sn_type=None, u_id=None, test_r=None):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()    
        test_r = " ".join([str(i) for i in test_r])
        cur.execute("""UPDATE users SET test_result = \"{}\" WHERE {} = {}""".
                         format(test_r, sn_type, u_id))
        conn.commit()
        conn.close()

    def get_table(self, table):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()    
        return cur.execute("SELECT * FROM {}".format(table)).fetchall()

    def print_table(self, table):
        print(*self.get_table(table), sep="\n")

    def get_subscribe_match(self, subscribes):
        """Возвращает list с 5 (tg_id, совпадений) с наибольшими совпадениями"""
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()  
        matches = {}
        for subscribe in subscribes:
            users = set()
            results = self.cur.execute(f'''SELECT tg_id FROM subs WHERE sup = {subscribe}''').fetchall()
            for result in results:
                other_id = result[0]
                users.add(other_id)
                if other_id not in users:
                    try:
                        matches[other_id] += 1
                    except Exception:
                        matches[other_id] = 1


if __name__ == "__main__":
    db = UsersDB()
    db.add_user(sn_type="tg_id",u_id=545921945)
    db.add_user(sn_type="tg_id",u_id=667624384)
    db.add_user(sn_type="tg_id",u_id=461038836)
    db.add_user(sn_type="tg_id",u_id=1351593274)
    db.add_user(sn_type="tg_id",u_id=510449525)
    db.add_test_results(sn_type="tg_id", u_id=545921945,test_r=[1,1,1,1,1,1,1,1,0,1])
    db.add_test_results(sn_type="tg_id", u_id=667624384,test_r=[1,0,1,1,1,1,1,0,1,0])
    db.add_test_results(sn_type="tg_id", u_id=461038836,test_r=[1,1,0,1,1,1,0,1,0,1])
    db.add_test_results(sn_type="tg_id", u_id=1351593274,test_r=[1,1,1,0,1,0,1,0,1,1])
    db.add_test_results(sn_type="tg_id", u_id=510449525,test_r=[1,1,1,1,0,1,0,1,1,1])
    db.print_table('users')
    




