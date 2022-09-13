from database.manage import db_session
from database.models import Admin


class AdminRepository:
    def get_admin_by_id(self, admin_id):
        return db_session.query(Admin).get(admin_id)
        # users = self.session.query(User).all()

    def get_admin_by_email(self, admin_email):
        return db_session.query(Admin).filter(Admin.email == admin_email).first()

    def save_admin(self, user_obj, password):
        user_obj.set_password(password)
        db_session.add(user_obj)
        db_session.commit()


admins_rep = AdminRepository()
