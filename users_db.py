import sqlite3
import os

from db import DB, correct_sn


class UsersDB(DB):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect(os.path.join("data", "database.db"))
        self.cur = self.db.cursor()

    @correct_sn
    def is_user_in_db(self, sn_type=None, u_id=None):
        r = self.cur.execute("SELECT * FROM users WHERE {} = {}".format(sn_type, u_id, )).fetchall()
        return bool(r)

    @correct_sn
    def add_user(self, sn_type=None, u_id=None):
        if not self.is_user_in_db(sn_type=sn_type, u_id=u_id):
            self.cur.execute("INSERT INTO users({}) VALUES ({})".format(sn_type, u_id))
            self.db.commit()
        self.print_table("users")

    @correct_sn
    def add_tiktok_to_user(self, sn_type=None, u_id=None, tt_nm=None):
        self.cur.execute(
            """UPDATE users SET tt_nm = \"{}\" WHERE {} = {}""".format(tt_nm, sn_type, u_id))
        self.db.commit()
        self.print_table("users")

    @correct_sn
    def is_tiktok(self, sn_type=None, u_id=None):
        return bool(self.cur.execute("""SELECT * FROM users WHERE {} = {} AND tt_nm != NULL""".
                                     format(sn_type, u_id)).fetchall())


if __name__ == "__main__":
    db = UsersDB()
    db.print_table("users")
