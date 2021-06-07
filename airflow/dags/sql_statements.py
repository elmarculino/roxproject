# DROP TABLES

DROP_TABLES_SQL = """
    DROP TABLE IF EXISTS SalesOrderDetail,
        SpecialOfferProduct,
        SalesOrderHeader,
        Customer,
        Product,
        Person;
"""

# CREATE TABLES

CREATE_PERSON_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS Person
    (
        BusinessEntityID INTEGER NOT NULL,
        PersonType VARCHAR(10),
        NameStyle INTEGER,
        Title VARCHAR(10),
        FirstName VARCHAR(50),
        MiddleName VARCHAR(50),
        LastName VARCHAR(50),
        Suffix VARCHAR(10),
        EmailPromotion INTEGER,
        AdditionalContactInfo VARCHAR(2000),
        Demographics VARCHAR(1000),
        rowguid VARCHAR(36),
        ModifiedDate TIMESTAMP,
        PRIMARY KEY(BusinessEntityID)
    )
"""

CREATE_PRODUCT_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS Product
    (
        ProductID INTEGER NOT NULL,
        Name VARCHAR(50),
        ProductNumber VARCHAR(10),
        MakeFlag INTEGER,
        FinishedGoodsFlag INTEGER,
        Color VARCHAR(20),
        SafetyStockLevel INTEGER,
        ReorderPoint INTEGER,
        StandardCost FLOAT,
        ListPrice FLOAT,
        Size VARCHAR(10),
        SizeUnitMeasureCode VARCHAR(10),
        WeightUnitMeasureCode VARCHAR(10),
        Weight FLOAT,
        DaysToManufacture INTEGER,
        ProductLine VARCHAR(10),
        Class VARCHAR(10),
        Style VARCHAR(10),
        ProductSubcategoryID INTEGER,
        ProductModelID INTEGER,
        SellStartDate TIMESTAMP,
        SellEndDate TIMESTAMP,
        DiscontinuedDate TIMESTAMP,
        rowguid VARCHAR(36),
        ModifiedDate TIMESTAMP,
        PRIMARY KEY (ProductID)
    )
"""

CREATE_CUSTOMER_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS Customer
    (
        CustomerID INTEGER NOT NULL,
        PersonID INTEGER,
        StoreID INTEGER,
        TerritoryID INTEGER,
        AccountNumber VARCHAR(10),
        rowguid VARCHAR(36),
        ModifiedDate TIMESTAMP,
        PRIMARY KEY (CustomerID),
        FOREIGN KEY (PersonID) REFERENCES Person(BusinessEntityID)
    )
"""

CREATE_SALESORDERHEADER_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS SalesOrderHeader
    (
        SalesOrderID INTEGER NOT NULL,
        RevisionNumber INTEGER,
        OrderDate TIMESTAMP,
        DueDate TIMESTAMP,
        ShipDate TIMESTAMP,
        Status INTEGER,
        OnlineOrderFlag INTEGER,
        SalesOrderNumber VARCHAR(10),
        PurchaseOrderNumber VARCHAR(20),
        AccountNumber VARCHAR(20),
        CustomerID INTEGER,
        SalesPersonID INTEGER,
        TerritoryID INTEGER,
        BillToAddressID INTEGER,
        ShipToAddressID INTEGER,
        ShipMethodID INTEGER,
        CreditCardID INTEGER,
        CreditCardApprovalCode VARCHAR(20),
        CurrencyRateID INTEGER,
        SubTotal FLOAT,
        TaxAmt FLOAT,
        Freight FLOAT,
        TotalDue FLOAT,
        Comment VARCHAR(10),
        rowguid VARCHAR(36),
        ModifiedDate TIMESTAMP,
        PRIMARY KEY (SalesOrderID),
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    )
"""

CREATE_SPECIALOFFERPRODUCT_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS SpecialOfferProduct
    (
        SpecialOfferID INTEGER NOT NULL,
        ProductID INTEGER NOT NULL,
        rowguid VARCHAR(36),
        ModifiedDate TIMESTAMP,
        PRIMARY KEY (SpecialOfferID, ProductID),
        FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
    )
"""

CREATE_SALESORDERDETAIL_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS SalesOrderDetail
    (
        SalesOrderID INTEGER NOT NULL,
        SalesOrderDetailID INTEGER NOT NULL,
        CarrierTrackingNumber VARCHAR(20),
        OrderQty INTEGER,
        ProductID INTEGER,
        SpecialOfferID INTEGER,
        UnitPrice FLOAT,
        UnitPriceDiscount FLOAT,
        LineTotal FLOAT,
        rowguid VARCHAR(36),
        ModifiedDate TIMESTAMP,
        PRIMARY KEY (SalesOrderID, SalesOrderDetailID),
        FOREIGN KEY (SalesOrderID)
            REFERENCES SalesOrderHeader(SalesOrderID),
        FOREIGN KEY (SpecialOfferID, ProductID)
            REFERENCES SpecialOfferProduct(SpecialOfferID, ProductID),
        FOREIGN KEY (ProductID)
            REFERENCES Product(ProductID)
    )
"""

COPY_SQL = """
COPY {}
FROM '{}'
IAM_ROLE 'arn:aws:iam::029258854698:role/doxRole'
IGNOREHEADER 1
DELIMITER ';'
"""


COPY_PERSON_SQL = COPY_SQL.format(
    "Person",
    "s3://roxproject/data/Person.Person.csv"
)

COPY_PRODUCT_SQL = COPY_SQL.format(
    "Product",
    "s3://roxproject/data/Production.Product.csv"
)

COPY_CUSTOMER_SQL = COPY_SQL.format(
    "Customer",
    "s3://roxproject/data/Sales.Customer.csv"
)

COPY_SALESORDERHEADER_SQL = COPY_SQL.format(
    "SalesOrderHeader",
    "s3://roxproject/data/Sales.SalesOrderHeader.csv"
)

COPY_SPECIALOFFERPRODUCT_SQL = COPY_SQL.format(
    "SpecialOfferProduct",
    "s3://roxproject/data/Sales.SpecialOfferProduct.csv"
)

COPY_SALESORDERDETAIL_SQL = COPY_SQL.format(
    "SalesOrderDetail",
    "s3://roxproject/data/Sales.SalesOrderDetail.csv"
)

# QUERY LISTS

create_table_queries = [
    CREATE_PERSON_TABLE_SQL,
    CREATE_PRODUCT_TABLE_SQL,
    CREATE_CUSTOMER_TABLE_SQL,
    CREATE_SALESORDERHEADER_TABLE_SQL,
    CREATE_SPECIALOFFERPRODUCT_TABLE_SQL,
    CREATE_SALESORDERDETAIL_TABLE_SQL,
]
