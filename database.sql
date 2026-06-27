-- Company Database Setup


CREATE DATABASE IF NOT EXISTS company;
USE company;


-- Table: emp


DROP TABLE IF EXISTS emp;

CREATE TABLE emp (
    empno  INT PRIMARY KEY,
    name   VARCHAR(20),
    dept   VARCHAR(20),
    salary INT
);

INSERT INTO emp (empno, name, dept, salary) VALUES
(1,'Jitendra','it',120000),
(2,'Surendra','it',350000),
(3,'Vikas','hr',80000),
(4,'Nitin','hr',56000),
(5,'Akshay','marketing',95000),
(6,'Aamir','it',120000),
(7,'Ranvir','sales',60000),
(8,'Nasir','acting',75000),
(9,'Akshay','sales',8000),
(10,'Namra','supervisor',90000);


-- End of Database