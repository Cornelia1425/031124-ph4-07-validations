from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# USER MODEL

class User(db.Model, SerializerMixin):
    
    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String)
    address = db.Column(db.String)
    phone_number = db.Column(db.String)
    age = db.Column(db.Integer)
    vip = db.Column(db.Boolean)
    year_joined = db.Column(db.Integer)

    # @validates('username')
    # def validate_username(self, key, value):
    #     # if len(value.strip()) >= 4:
    #     #     return value.strip()
    #     # if len(value.replace(' ', '')) >= 4:
    #     #     return value.replace(' ', '')
    #     # if len(value.strip().replace(' ', '_')) >= 4:
    #     #     return value.strip().replace(' ', '_')
    #     if len(value.replace(' ', '_').strip()) >= 4:
    #         return value.replace(' ', '_').strip()
    #     else:
    #         raise ValueError('Username must be greater than or equal to 4 characters')
        

    @validates('username')
    def validate_unique_username(self, key, value):
        user = User.query.where(User.username==value).first()
        if user:
            raise ValueError('User must be unique!')
        else:
            return value

        
    @validates('age')
    def validate_age(self, key, value):
        if value >=13:
            return value
        else:
            raise ValueError('Must be at least 13 years old!')
    
    @validates('email')
    def validate_email(self, key, value):
        if '$' in value:
            raise ValueError('Invalid characters for email!')
        else:
            return value

    
    
