DROP DATABASE IF EXISTS expresso_churn;
CREATE DATABASE expresso_churn;
USE expresso_churn;

CREATE TABLE expresso_user(
	user_id VARCHAR(100) NOT NULL PRIMARY KEY,
    region VARCHAR(40) ,
    tenure VARCHAR(20) ,
    montant DECIMAL(10,2),
    frequency_rech DECIMAL(8,2),
    revenue DECIMAL(10,2),
    arpu_segment DECIMAL(10,2),
    frequency INTEGER,
    data_volume DECIMAL(12,2),
    on_net DECIMAL(8,2) DEFAULT NULL ,
    orange DECIMAL(8,2) DEFAULT NULL,
    tigo DECIMAL(8,2) DEFAULT NULL,
    zone1 DECIMAL(8,2) DEFAULT NULL,
    zone2 DECIMAL(8,2) DEFAULT NULL  ,
    mrg VARCHAR(7),
    regularity INTEGER,
    top_pack VARCHAR(100),
    freq_top_pack DECIMAL(4,2)
    );
    
CREATE TABLE prediction_info(
	date_of_prediction DATETIME,
	user_id VARCHAR(100) NOT NULL PRIMARY KEY,
    churn_probability DECIMAL(2,2) NOT NULL
	);

CREATE TABLE user_churn(
	user_id VARCHAR(100) NOT NULL PRIMARY KEY,
    churn INTEGER NOT NULL
	);
    
CREATE TABLE employee(
	id VARCHAR(20) NOT NULL,
    email_address VARCHAR(40) NOT NULL,
    surname VARCHAR(20) ,
    firstname VARCHAR(20) ,
    middlename VARCHAR(20),
    employee_password VARCHAR(60),
    CONSTRAINT PK_employee_info PRIMARY KEY (id, email_address)
    );
    
