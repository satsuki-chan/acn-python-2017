/* Step -3. Create a HR_db Database in MySql and creat an Employee table (feel free to add fields, populate some sample data with a good amount of records) */
CREATE DATABASE IF NOT EXISTS HR_db;
USE HR_db;

/* Tables structures */

DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
  a_id integer NOT NULL COMMENT 'Employee ID number',
  b_name varchar(25) NOT NULL COMMENT 'Employee first name',
  c_middle_name varchar(25) NULL COMMENT 'Employee middle or second name',
  d_last_name varchar(25) NOT NULL COMMENT 'Employee last name',
  f_department varchar(25) NOT NULL COMMENT 'Employee department or unit',
  e_role varchar(25) NOT NULL COMMENT 'Employee role or position in her or his department',
  g_boss_id integer NOT NULL NOT NULL COMMENT 'Employee boss or supervisor ID',
  h_salary double NOT NULL COMMENT 'Employee monthly salary',
  PRIMARY KEY (a_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO employee VALUES
(1,"Kami",NULL,"sama","World","Divinity",0,10000000000000000000000000000.00),
(2,"Goku",NULL,"Son","Earth","Divinity-like fighter",1,9.99),
(3,"Vegetta",NULL,"Saiyan","Earth","Divinity-like fighter",1,900000000.00),
(4,"Piccolo","Dai Maku","Nameku","Earth","Semi-divinity fighter",1,990000000.00),
(5,"Yamcha",NULL,"Earthling","Earth","Super fighter",1,50000000.00),
(6,"Han",NULL,"Ten Shin","Earth","Super fighter",1,60000000.00),
(7,"Krilin",NULL,"Earthling","Earth","Fighter",1,150000.00),
(8,"Gohan",NULL,"Son","Earth","Semi-divinity fighter",1,750000.00)
;
