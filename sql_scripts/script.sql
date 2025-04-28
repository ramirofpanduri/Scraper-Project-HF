CREATE DATABASE clothes_shop;

USE clothes_shop;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(255),
    name VARCHAR(255),
    price VARCHAR(255)
);

select * from products;