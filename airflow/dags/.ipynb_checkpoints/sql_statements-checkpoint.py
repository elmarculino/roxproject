# DROP TABLES

DROP_PERSON_TABLE_SQL = "DROP TABLE IF EXISTS Person;"
DROP_PRODUCT_TABLE_SQL = "DROP TABLE IF EXISTS Product;"
DROP_CUSTOMER_TABLE_SQL = "DROP TABLE IF EXISTS Customer;"
DROP_SALESORDERHEADER_TABLE_SQL = "DROP TABLE IF EXISTS SalesOrderHeader;"
DROP_SPECIALOFFERPRODUCT_TABLE_SQL = "DROP TABLE IF EXISTS  SpecialOfferProduct;"
DROP_SALESORDERDETAIL_TABLE_SQL = "DROP TABLE IF EXISTS SalesOrderDetail;"

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
ACCESS_KEY_ID '{{}}'
SECRET_ACCESS_KEY '{{}}'
IGNOREHEADER 1
DELIMITER ','
"""

COPY_MONTHLY_TRIPS_SQL = COPY_SQL.format(
    "trips",
    "s3://udacity-dend/data-pipelines/divvy/partitioned/{year}/{month}/divvy_trips.csv"
)

COPY_ALL_TRIPS_SQL = COPY_SQL.format(
    "trips",
    "s3://udacity-dend/data-pipelines/divvy/unpartitioned/divvy_trips_2018.csv"
)

COPY_STATIONS_SQL = COPY_SQL.format(
    "trips",
    "s3://udacity-dend/data-pipelines/divvy/unpartitioned/divvy_stations_2017.csv"
)

# QUERY LISTS

create_table_queries = [
    DROP_PERSON_TABLE_SQL,
    DROP_PRODUCT_TABLE_SQL,
    DROP_CUSTOMER_TABLE_SQL,
    DROP_SALESORDERHEADER_TABLE_SQL,
    DROP_SPECIALOFFERPRODUCT_TABLE_SQL,
    DROP_SALESORDERDETAIL_TABLE_SQL,
]
drop_table_queries = [
    CREATE_PERSON_TABLE_SQL,
    CREATE_PRODUCT_TABLE_SQL,
    CREATE_CUSTOMER_TABLE_SQL,
    CREATE_SALESORDERHEADER_TABLE_SQL,
    CREATE_SPECIALOFFERPRODUCT_TABLE_SQL,
    CREATE_SALESORDERDETAIL_TABLE_SQL,
]
