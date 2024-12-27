from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app import db, app
from enum import Enum as RoleEnum
from flask_login import UserMixin
from datetime import datetime


class UserRole(RoleEnum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dyoffqmct/image/upload/​v1734370860/mẫu/phong cảnh/thuyền-bãi-biển.jpg')
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    receipts = relationship('Receipt', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)

    def __str__(self):
        return self.name

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    details = relationship('ReceiptDetails', backref='product', lazy=True)
    comments = relationship('Comment', backref='product', lazy=True)

    def __str__(self):
        return self.name


class Receipt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    created_date = Column(DateTime, default=datetime.now())
    details = relationship('ReceiptDetails', backref='receipt', lazy=True)

    def __str__(self):
        return self.id

class ReceiptDetails(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)


class Comment(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    created_date = Column(DateTime, default=datetime.now())




if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        u = User(name='admin', username='admin',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()
        c1 = Category(name='Thái Lan')
        c2 = Category(name='Nhật Bản')
        c3 = Category(name='Anh')
        c4 = Category(name='Cambodia')
        c5 = Category(name='Canada')
        c6 = Category(name='Ý')
        c7 = Category(name='Pháp')
        c8 = Category(name='Mỹ')
        c9 = Category(name='Úc')
        c10 = Category(name='Trung Quốc')


        db.session.add_all([c1, c2, c3,c4,c5,c6,c7,c8,c9,c10])
        db.session.commit()

        products = [{
            "name": "Thái Lan",
            "description": "Hạng 1,ghế 01,sân bay từ BangKok đến MaCao Trung Quốc, Ngày 20-10-2024 giờ khởi hành 10:30, thời gian bay 5 tiếng",
            "price": 1500000,
            "category_id": 1
        }, {
            "name": "Nhật Bản",
            "description": "Hạng 2,ghế 02,sân bay từ Tokyo đến Thượng Hải Trung Quốc, Ngày 22-5-2024 giờ khởi hành 12:30, thời gian bay 4 tiếng",
            "price": 1600000,
            "category_id": 2
        }, {
            "name": "Anh",
            "description": "Hạng 1,ghế 04,sân bay từ Anh đến MaCao Trung Quốc, Ngày 23-11-2024 giờ khởi hành 10:30, thời gian bay 3 tiếng",
            "price":1700000,
            "category_id": 3
        }, {
            "name": "Cambodia",
            "description": "Hạng 2,ghế 01,sân bay từ Phnôm Pênh đến Vũ Hán Trung Quốc, Ngày 20-10-2024 giờ khởi hành 10:30, thời gian bay 5 tiếng",
            "price": 1800000,
            "category_id": 4
        }, {
            "name": "Canada",
            "description": "Hạng 1,ghế 01,sân bay từ Ottawa đến Tứ Xuyên Trung Quốc, Ngày 20-1-2024 giờ khởi hành 10:30, thời gian bay 7 tiếng",
            "price": 1900000,
            "category_id": 5
        }, {
            "name": "Ý",
            "description": "Hạng 2,ghế 11,sân bay từ Roma đến BangKok Thái Lan, Ngày 20-2-2024 giờ khởi hành 5:30, thời gian bay 5 tiếng",
            "price": 200000,
            "category_id": 6
        }, {
            "name": "Pháp",
            "description": "Hạng 1,ghế 08,sân bay từ Pari đến Roma Ý, Ngày 20-10-2024 giờ khởi hành 10:30, thời gian bay 5 tiếng",
            "price": 2100000,
            "category_id": 7
        }, {
            "name": "Mỹ",
            "description": "Hạng 1,ghế 01,sân bay từ Washington đến MaCao Trung Quốc, Ngày 20-10-2024 giờ khởi hành 10:30, thời gian bay 5 tiếng",
            "price": 2200000,
            "category_id": 8
        }, {
            "name": "Úc",
            "description": "Hạng 2,ghế 01,sân bay từ Canberra đến Tokyo Nhật Bản, Ngày 20-6-2024 giờ khởi hành 10:30, thời gian bay 4 tiếng",
            "price": 5000000,

            "category_id": 9
        }, {
            "name": "Trung Quốc",
            "description": "Hạng 1,ghế 01,sân bay từ Bắc Kinh đến Hồng Kông, Ngày 11-10-2024 giờ khởi hành 9:30, thời gian bay 3 tiếng",
            "price": 400000,
            "category_id": 10
        }]

        for p in products:
            prod = Product(**p)
            db.session.add(prod)

        db.session.commit()

        c1 = Comment(content='Chuyến bay an toàn', user_id=1, product_id=1)
        c2 = Comment(content='Nhân viên chu đáo', user_id=1, product_id=1)
        c3 = Comment(content='Đồ ăn ngon', user_id=1, product_id=1)

        db.session.add_all([c1, c2, c3])
        db.session.commit()


