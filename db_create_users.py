from project import db
from project.sql import User

# insert data
# db.session.add(User("Michael", "zzz@qq.com", "you-will-never-know"))
# db.session.add(User("zhangzhihao", "erdos_zzh@163,com", "qweasdzxc"))
db.session.add(User("JackFram", "erdos_zzh@163,com", "qweasdzxc"))

# commit changes
db.session.commit()
