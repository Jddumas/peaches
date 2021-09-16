CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    sku_id smallint NOT NULL,
    reception_date varchar(200) NOT NULL,
    removal_date varchar(200) NOT NULL, 
    state varchar(200) NOT NULL,
	);