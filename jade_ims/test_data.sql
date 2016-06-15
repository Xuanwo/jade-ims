-- data for Supplier

INSERT INTO Supplier VALUES (
  1,
  "Apple",
  "库克",
  "13000000000",
  "美国",
  "爱买不买！"
);

INSERT INTO Supplier VALUES (
  2,
  "Google ",
  "Larry Page",
  "13000000000",
  "美国",
  "谷歌大法好！"
);

-- data for Product
INSERT INTO product VALUES (
  1,
  "iPhone6s",
  "7000",
  1,
  "身份的象征"
);

-- data for Stock
INSERT INTO stock VALUES (
  1,
  100,
  ""
);

-- data for Customer
INSERT INTO customer VALUES (
  1,
  "阮哥",
  "13000000000",
  "中国地质大学（北京）",
  "对的呀，就是这样的呀"
);

--data for InputBill
INSERT INTO input_bill VALUES (
  1,
  1,
  100,
  7000,
  "2016-06-09 06:00:00.000000",
  "iPhone采购"
);

--data for SaleBill
INSERT INTO sale_bill VALUES (
  1,
  1,
  1,
  "2016-06-09 06:00:00.000000",
  1,
  7000,
  "强行购买"
);

