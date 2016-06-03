from jade_ims import db


class User(db.Model):
    """用户表

    Attributes:
        ID: 用户ID
        Name: 用户名字
        Password: 用户密码
    """
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, Name, Password):
        self.Name = Name
        self.Password = Password

    def __repr__(self):
        return '<User %r>' % self.Name


class Supplier(db.Model):
    """供应商表

    """
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Address = db.Column(db.String(250))
    Phone = db.Column(db.String(20), nullable=False)
    Constact = db.Column(db.String(20), nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Name, Address, Phone, Constact, Remark):
        self.Name = Name
        self.Address = Address
        self.Phone = Phone
        self.Constact = Constact
        self.Remark = Remark

    def __repr__(self):
        return '<Supplier %r>' % self.Name


class Customer(db.Model):
    """顾客表

    """
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Name, Phone, Remark):
        self.Name = Name
        self.Phone = Phone
        self.Remark = Remark

    def __repr__(self):
        return '<Customer %r>' % self.Name


class Product(db.Model):
    """商品表

    """
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Supplier_ID = db.Column(db.Integer, db.ForeignKey(Supplier.ID), nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Name, Price, Supplier_ID, Remark):
        self.Name = Name
        self.Price = Price
        self.Supplier_ID = Supplier_ID
        self.Remark = Remark

    def __repr__(self):
        return '<Product %r>' % self.Name


class InputBill(db.Model):
    """进货单

    """
    ID = db.Column(db.Integer, primary_key=True)
    Supplier_ID = db.Column(db.Integer, db.ForeignKey(Supplier.ID), nullable=False)
    Product_ID = db.Column(db.Integer, db.ForeignKey(Product.ID), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Supplier_ID, Product_ID, Quantity, Price, Date, Remark):
        self.Supplier_ID = Supplier_ID
        self.Product_ID = Product_ID
        self.Quantity = Quantity
        self.Price = Price
        self.Date = Date
        self.Remark = Remark

    def __repr__(self):
        return '<InputBill ID %d>' % self.ID


class EnterStockBill(db.Model):
    """入库单

    """
    ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey(Product.ID), nullable=False)
    InputBill_ID = db.Column(db.Integer, db.ForeignKey(InputBill.ID), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Remark = db.Column(db.String)

    def __init__(self, Product_ID, InputBill_ID, Quantity, Remark):
        self.Product_ID = Product_ID
        self.InputBill_ID = InputBill_ID
        self.Quantity = Quantity
        self.Remark = Remark

    def __repr__(self):
        return '<EnterStockBill ID %d>' % self.ID


class SaleBill(db.Model):
    """销货单

    """
    ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey(Product.ID), nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Discount = db.Column(db.Float, nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Prodcut_ID, Date, Quantity, Price, Discount, Remark):
        self.Product_ID = Prodcut_ID
        self.Date = Date
        self.Quantity = Quantity
        self.Price = Price
        self.Discount = Discount
        self.Remark = Remark

    def __repr__(self):
        return '<SaleBill ID %d>' % self.ID


class LeaveStockBill(db.Model):
    """出库单

    """
    ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey(Product.ID), nullable=False)
    SaleBill_ID = db.Column(db.Integer, db.ForeignKey(SaleBill.ID), nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Product_ID, SaleBill_ID, Date, Quantity, Remark):
        self.Product_ID = Product_ID
        self.SaleBill_ID = SaleBill_ID
        self.Date = Date
        self.Quantity = Quantity
        self.Remark = Remark

    def __repr__(self):
        return '<LeaveStockBill ID %d>' % self.ID


class Stock(db.Model):
    """库存表

    """
    Product_ID = db.Column(db.Integer, db.ForeignKey(Product.ID), primary_key=True)
    Quantity = db.Column(db.Integer, nullable=False)
    Remark = db.Column(db.String(1000))

    def __init__(self, Product_ID, Quantity, Remark):
        self.Product_ID = Product_ID
        self.Quantity = Quantity
        self.Remark = Remark

    def __repr__(self):
        return '<Stock %d>' % self.Product_ID
