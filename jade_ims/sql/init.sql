CREATE TABLE Supplier  /*供应商表*/
(
  Supplier_ID    INT IDENTITY(1, 1) NOT NULL, /* 供应商编号 ,主键 */
  Name           VARCHAR(250)       NOT NULL, /* 供应商名称 */
  Address        VARCHAR(250)       NOT NULL, /* 地址 */
  Phone          VARCHAR(25), /* 电话 */
  ConstactPerson VARCHAR(20), /* 联系人 */
  Remark         VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE Customer   /* 客户表*/
(
  Customer_ID INT IDENTITY(1, 1) NOT NULL, /* 客户编号,主键*/
  Name        VARCHAR(250)       NOT NULL, /* 客户名称 */
  Address     VARCHAR(250)       NOT NULL, /* 地址 */
  Phone       VARCHAR(25), /* 电话 */
  Remark      VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE Product    /* 商品信息表 */
(
  Product_ID  INT IDENTITY(1, 1) NOT NULL, /* 商品编号, 主键 */
  Name        VARCHAR(30)        NOT NULL, /* 商品名称 */
  Price       REAL, /* 参考价格 */
  Supplier_ID INT                NOT NULL, /* 供应商编号 , 主键,  外键( 参照 SUPPLIER 表) */
  CreateDate  DATETIME, /* 创建时间 */
  Remark      VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE ImportBill    /* 进货单 */
(
  ImportBill_ID INT IDENTITY(1, 1) NOT NULL, /* 进货单编号 , 主键 */
  Supplier_ID   INT                NOT NULL, /* 供应商,   外键 ( 参照 SUPPLIER 表 ) */
  Product_ID    INT                NOT NULL, /* 所进商品编号,主键, 外键 (参照 PRODUCT 表 ) */
  Quantity      INT                NOT NULL, /* 商品数量 */
  Price         REAL               NOT NULL, /* 商品进价 */
  Sum           REAL               NOT NULL, /* 商品总价 */
  DATE          DATETIME           NOT NULL, /* 日期  */
  Remark        VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE EnterStock    /* 入库单表 */
(
  EnterStock_ID INT IDENTITY(1, 1) NOT NULL, /* 入库单编号 , 主键 */
  EnterDate     DATETIME           NOT NULL, /* 入库时间 */
  Product_ID    INT                NOT NULL, /* 此种商品编号,主键, 外键 (参照 PRODUCT 表 ) */
  Quantity      INT                NOT NULL, /* 此种商品数量 */
  Price         REAL, /* 此种商品参考价格  */
  Remark        VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE Sale   /* 销售表 */
(
  Sale_ID    INT IDENTITY(1, 1) NOT NULL, /* 销售单编号  */
  SaleDate   DATETIME           NOT NULL, /* 销售 日期 */
  Product_ID INT                NOT NULL, /* 商品编号,主键, 外键 ( 参照 PRODUCT 表 ) */
  Quantity   INT                NOT NULL, /* 数量 */
  Price      REAL               NOT NULL, /* 价格 */
  Discount   INT, /* 折扣 */
  Remark     VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE LeaveStock  /* 出库单表 */
(
  LeaveStock_ID INT IDENTITY(1, 1) NOT NULL, /* 出库单编号 , 主键*/
  LeaveDate     DATETIME           NOT NULL, /* 出库时间 */
  Product_ID    INT                NOT NULL, /* 所出商品编号,主键, 外键 (参照 PRODUCT 表 ) */
  Quantity      INT                NOT NULL, /* 出库数量 */
  Price         REAL, /* 出库价格 */
  Remark        VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE SaleBill    /* 发货单 */
(
  SaleBill_ID INT IDENTITY(1, 1) NOT NULL, /* 发货单编号 , 主键 */
  Sale_ID     INT IDENTITY(1, 1) NOT NULL, /* 销售单编号 ，外键（参照销售表） */
  Customer_ID INT IDENTITY(1, 1) NOT NULL, /* 客户,   外键 ( 参照 CUSTOMER表 ) */
  Product_ID  INT                NOT NULL, /* 销售商品编号,主键, 外键 (参照 PRODUCT 表 ) */
  Quantity    INT                NOT NULL, /* 商品数量 */
  Price       REAL               NOT NULL, /* 商品单价 */
  Sum         REAL               NOT NULL, /* 商品总价 */
  DATE        DATETIME           NOT NULL, /* 日期  */
  Remark      VARCHAR(250)      /* 描述,备注 */
);
CREATE TABLE StockPile  /* 库存表 */
(
  Product_ID     INT      NOT NULL, /* 商品编号,     外键 ( 参照 PRODUCT 表 ) */
  FirstEnterDate DATETIME NOT NULL, /* 此种商品第一次入库时间 */
  LastLeaveDate  DATETIME, /* 此种商品最后一次出库时间 */
  Quantity       INT      NOT NULL, /* 所存数量 */
  Price          REAL     NOT NULL, /* 加权价 */
  Remark         VARCHAR(250)     /* 描述,备注 */
);