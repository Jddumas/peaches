CREATE TABLE product (
    sku UUID DEFAULT gen_random_uuid() PRIMARY KEY ON DELETE CASCADE,
    name TEXT DEFAULT "untitled" NOT NULL,
    brand TEXT DEFAULT "untitled" NOT NULL,
    description TEXT,
    price decimal default 0.0 NOT NULL CHECK(price > 0.0),
    stock bigint default 0 NOT NULL CHECK(stock > 0.0),
    weight decimal default 0.0 NOT NULL CHECK(stock > 0.0),
    shelf_life decimal default 0.0 NOT NULL CHECK(shelf_life > 0.0)
    thumbnail_url text,
    active boolean default true NOT NULL
);

CREATE TABLE item (
    id UUID PRIMARY KEY, 
    sku UUID FOREIGN KEY REFERENCES product (sku), 
    reception_date varchar(20) NOT NULL,
    removal_date varchar(20), 
    state varchar(20) DEFAULT 'IN_INVENTORY' NOT NULL
);