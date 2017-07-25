DROP TABLE IF EXISTS trial_flask_user_role;DROP TABLE IF EXISTS trial_flask_role;DROP TABLE IF EXISTS trial_flask_user;CREATE TABLE trial_flask_role(id serial PRIMARY KEY,name VARCHAR (100) UNIQUE NOT NULL,description VARCHAR (255));CREATE TABLE trial_flask_user(id serial PRIMARY KEY,first_name VARCHAR(50) NOT NULL,last_name VARCHAR(50) NOT NULL);CREATE TABLE trial_flask_user_role(id serial PRIMARY KEY,user_id INTEGER NOT NULL,role_id INTEGER NOT NULL,UNIQUE (user_id, role_id),CONSTRAINT flask_user_role_role_id_fkey FOREIGN KEY (role_id) REFERENCES trial_flask_role (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,CONSTRAINT flask_user_role_user_id_fkey FOREIGN KEY (user_id) REFERENCES trial_flask_user (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);


CREATE TABLE orders(id serial PRIMARY KEY,name VARCHAR (100) UNIQUE NOT NULL);CREATE TABLE products(id serial PRIMARY KEY,name VARCHAR (100) UNIQUE NOT NULL);CREATE TABLE order_product(id serial PRIMARY KEY, product_id INTEGER NOT NULL,order_id INTEGER NOT NULL,UNIQUE (product_id, order_id), quantity INTEGER)