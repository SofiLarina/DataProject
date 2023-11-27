from db import User, db
from werkzeug.security import generate_password_hash, check_password_hash

def registration(name, email, password):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        new_user = User(email=email, name=name, password=generate_password_hash(password))
        db.add(new_user)
        db.commit()
        print("Registration suceed")
        return True
    else:
        print("User with such login is already exist.")
        return False

def autorization(email, password):
    try:
        user = db.query(User).filter(User.email == email).first()

        if check_password_hash(user.password, password):
            print("Autorization suceed.")
            return user.name
        else:
            print("Wrong password.")
            return False

    except:
        print("User with such name doesn't exist.")
        return False
