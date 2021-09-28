
CREATE TABLE product (
    sku UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL DEFAULT 'untitled',
    brand TEXT NOT NULL DEFAULT 'untitled',
    category TEXT NOT NULL DEFAULT 'unknown',
    description TEXT DEFAULT 'untitled',
    price DECIMAL NOT NULL DEFAULT 0.0 CHECK(price > 0.0),
    stock BIGINT NOT NULL DEFAULT 0.0 CHECK(stock > 0.0),
    weight DECIMAL NOT NULL DEFAULT 0.0 CHECK(weight > 0.0),
    shelf_life DECIMAL NOT NULL DEFAULT 0.0 CHECK(shelf_life > 0.0),
    thumbnail_url TEXT,
    active BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE item (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
    sku UUID REFERENCES product(sku) ON DELETE RESTRICT, 
    reception_date VARCHAR(20) NOT NULL,
    removal_date VARCHAR(20), 
    state VARCHAR(20) NOT NULL DEFAULT 'IN_INVENTORY'
);