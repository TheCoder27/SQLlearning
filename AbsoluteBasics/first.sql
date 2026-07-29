DROP TABLE IF EXISTS persons;

CREATE TABLE persons
(
    -- column || datatype || constraint
    ID int PRIMARY KEY,
    name varchar(25) NOT NULL,
    age int NOT NULL,
    middleName varchar(255)
);

INSERT INTO persons
VALUES 
(1, "John", 20, "Light"),
(2, "Ali", 38, "SHAWARMA"),
(3, "Lily", 25, "Nox");