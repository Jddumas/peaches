CREATE TABLE product (
	sku SERIAL PRIMARY KEY, 
	name varchar(200) NOT NULL, 
	description TEXT,
	brand varchar(200) NOT NULL,
 	price NUMERIC NOT NULL,
	weight NUMERIC NOT NULL,
	category varchar(200)NOT NULL,
	stock int NOT NULL,
	thumbnail_url varchar(400) NOT NULL,
	shelf_life smallint NOT NULL,
	active BOOLEAN NOT NULL
	);