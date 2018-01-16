from project.sql import User
from project import admin_page
from flask_admin.contrib.sqla import ModelView
from project import db
from flask import redirect, url_for, request
from flask_login import current_user


class RealUModelView(ModelView):
    #但是还是不许再每一个函数前加上这么判定的  ，不然还是可以直接通过地址访问
    def is_accessible(self):
        return current_user.admin

    #跳转
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login', next=request.url))


admin_page.add_view(RealUModelView(User, db.session))

