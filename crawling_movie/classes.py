class MOVIE:
    def __init__(self,code,title,score, n_reopen,c_count, img):
        self.code = code
        self.title = title
        self.score = score
        self.n_reopen = n_reopen
        self.c_count = c_count
        self.img = img

    def show(self,count):
        print('{2}. {0}/ {1}'.format(self.code,self.title, count))


class STAFF:
    def __init__(self,code,k_name,e_name,birth,nation, img):
        self.code = code
        self.k_name = k_name
        self.e_name = e_name
        self.birth = birth
        self.nation = nation
        self.img = img

    def show(self,count):
        print('{2}. {0}/ {1}'.format(self.code,self.k_name,count))


class CAST:
    def __init__(self,m_code,s_code,act_name,role_info):
        self.m_code = m_code
        self.s_code = s_code
        self.act_name = act_name
        self.role_info = role_info

    def show(self,count):
        print('{2}. {0}/ {1}'.format(self.m_code,self.s_code, count))