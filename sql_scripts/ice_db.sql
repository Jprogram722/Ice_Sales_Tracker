USE sales_db;

CREATE TABLE route (
	route_id_pk INTEGER AUTO_INCREMENT,
    route_name VARCHAR(255),
    CONSTRAINT PK_route_id PRIMARY KEY (route_id_pk)
);

INSERT INTO route (route_name) VALUES
('Valley 1.0/1.1'),
('Digby/Annapolis Royal'),
('Yarmouth/Shelburne'),
('kingston/Greenwood'),
('Windsor/East Hants');

CREATE TABLE days (
	days_id_pk INTEGER NOT NULL AUTO_INCREMENT,
    days_num_bails_sold INTEGER,
    days_max_tempurature FLOAT,
    days_num_stops INTEGER,
    route_id_fk INTEGER,
    days_date DATE,
    CONSTRAINT FK_route_id FOREIGN KEY (route_id_fk) REFERENCES route(route_id_pk),
    CONSTRAINT PK_route_id PRIMARY KEY (days_id_pk)
);