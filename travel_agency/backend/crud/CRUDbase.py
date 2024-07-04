from backend.db.db import session_scope
from backend.util import passutil
from backend.db.model import User, Base

class CRUDbase:
    def get_user_by_phone_number(self, phone_number) -> User:
        with session_scope() as db:
            user = db.query(User).filter(User.phone_number == phone_number).first()
            return user

    def get_user_password(self, phone_number) -> str:
        with session_scope() as db:
            user = db.query(User).filter(User.phone_number == phone_number).first()
            return user.password



crud_base = CRUDbase()
