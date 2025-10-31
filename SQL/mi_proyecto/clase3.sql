-- En myFirstDB (donde tenía creada la tabla de employees)

CREATE TABLE IF NOT EXISTS departments (
    id      BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name    VARCHAR NOT NULL
);

INSERT INTO departments (name)
VALUES
('Engineering'),
('Marketing')
;

SELECT * FROM departments;

ALTER TABLE employees ADD COLUMN department_id BIGINT REFERENCES departments(id);

SELECT * FROM departments; -- 1: Engineering; 2: Marketing;

INSERT INTO employees(birth_date, first_name, last_name, salary, title, title_date, department_id)
VALUES
('2011-11-11', 'Perico', 'Palotes', 25000.00, 'Analista de Datos', '2024-07-01', 1),
('2010-07-11', 'Pepito', 'Toledo', 20000.00, 'Analista de Datos', '2023-10-03', 1),
('2007-04-21', 'Raúl', 'Navarro', 35000.00, 'Fisioterapeuta', '2025-10-10', 2)
;

UPDATE employees SET department_id = 2 WHERE id = 8;
UPDATE employees SET department_id = 2 WHERE id = 9;
UPDATE employees SET department_id = 1 WHERE id = 11;

SELECT * FROM employees;

SELECT *
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.id;

SELECT CONCAT(e.first_name, e.last_name) AS full_name, d.name AS department
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.id;


-- EXTRA Práctica from Diapo 39/47 (SQL II)
SELECT CONCAT(employees.first_name, employees.last_name) AS full_name, departments.name AS department
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;
;

