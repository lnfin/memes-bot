def correct_sn(method):
    sns = ("vk", "tg")

    def check_condition(self, sn_type=None, u_id=None, **kwargs):
        if sn_type in sns: sn_type += "_id"
        if sn_type in [sn + "_id" for sn in sns]:
            return method(self, sn_type=sn_type, u_id=u_id, **kwargs)
        else:
            raise Exception

    return check_condition


class DB:
    def __init__(self):
        self.db = None
        self.cur = None

    def get_table(self, table):
        return self.cur.execute("SELECT * FROM {}".format(table)).fetchall()

    def print_table(self, table):
        print(*self.get_table(table), sep="\n")
