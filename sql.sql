CREATE TABLE
    Goods (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        unit TEXT NOT NULL
    );

CREATE TABLE
    DeliveryNote (
        id INTEGER PRIMARY KEY,
        date DATE NOT NULL,
        supplier TEXT NOT NULL,
        goods_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (goods_id) REFERENCES Goods(id)
    );

CREATE TABLE
    Sale (
        id INTEGER PRIMARY KEY,
        date DATE NOT NULL,
        customer TEXT NOT NULL,
        goods_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (goods_id) REFERENCES Goods(id)
    );

CREATE TABLE
    AdditionalService (
        id INTEGER PRIMARY KEY,
        service_name TEXT NOT NULL,
        cost REAL NOT NULL
    );

CREATE TABLE
    SaleService (
        id INTEGER PRIMARY KEY,
        sale_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        FOREIGN KEY (sale_id) REFERENCES Sale(id),
        FOREIGN KEY (service_id) REFERENCES AdditionalService(id)
    );

CREATE TABLE
    Cost (
        id INTEGER PRIMARY KEY,
        goods_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        cost_per_unit REAL NOT NULL,
        date_added DATE NOT NULL,
        FOREIGN KEY (goods_id) REFERENCES Goods(id)
    );