CREATE DATABASE myFirstDB;

CREATE TABLE IF NOT EXISTS employees (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    birth_date  DATE NOT NULL,
    first_name  VARCHAR(100) NOT NULL,
    last_name   VARCHAR(100) NOT NULL
);

ALTER TABLE employees ADD COLUMN salary NUMERIC(10,2);
ALTER TABLE employees ADD COLUMN title VARCHAR(100);
ALTER TABLE employees ADD COLUMN title_date DATE;

INSERT INTO employees (birth_date, first_name, last_name, salary, title, title_date)
VALUES ('2001-12-03', 'Miguel', 'Navarro', 99999.99, 'Engineer', '2019-01-01');

INSERT INTO employees (birth_date, first_name, last_name, salary, title, title_date)
VALUES ('2001-12-03', 'Miguel', 'Navarro', 50000, 'Engineer', '2019-01-01');

INSERT INTO employees (birth_date, first_name, last_name, salary, title, title_date)
VALUES ('1990-05-15', 'Ana', 'Pérez', 35000, 'Ingeniera de Software', '2021-01-01'),
('1985-08-20', 'Luis', 'Gómez', 50000, 'Gerente de Producto', '2018-01-01'),
('1998-03-10', 'María', 'Rodríguez', 12000, 'Analista Júnior', '2020-01-01'),
('1991-11-25', 'Ana', 'López', 28000, 'Especialista en Marketing', '2020-01-01'),
('1980-06-01', 'Carlos', 'Sánchez', 45000, 'Desarrollador Senior', '2019-01-01'),
('2000-09-12', 'Elena', 'Martín', 7500, 'Asistente Administrativa', '2022-01-01'),
('1995-04-30', 'David', 'Ruiz', 15000, 'Técnico de Soporte', '2020-01-01'),
('1988-02-18', 'Ana', 'Torres', 40000, 'Arquitecta de Soluciones', '2023-01-01'),
('2001-10-05', 'Jorge', 'Moreno', 5000, 'Becario de Ventas', '2020-01-01'),
('1993-07-07', 'Sonia', 'Navarro', 32000, 'Diseñadora UX/UI', '2021-01-01'),
('1996-01-22', 'Pedro', 'Gil', 20000, 'Contable', '2020-01-01'),
('1994-12-03', 'Laura', 'Ramos', 18000, 'Especialista en RR.HH.', '2019-01-01'),
('1975-09-19', 'Miguel', 'Vega', 48000, 'Director de Operaciones', '2017-01-01'),
('2002-04-28', 'Isabel', 'Castro', 9000, 'Ayudante de Almacén', '2024-01-01');

SELECT * FROM employees;
SELECT first_name, salary FROM employees;

SELECT * FROM employees WHERE id = 2;
SELECT * FROM employees WHERE salary > 20000;
SELECT * FROM employees WHERE salary <= 10000;

UPDATE employees SET first_name = 'Alexis' WHERE id = 7;
DELETE FROM employees WHERE id = 5;
DELETE FROM employees WHERE salary > 20000;
SELECT * FROM employees WHERE salary BETWEEN 14000 AND 50000;
SELECT * FROM employees ORDER BY birth_date DESC;

SELECT * FROM employees;