drop database if exists Moda;

create database Moda;

use Moda;
drop table if exists Stroj;

CREATE TABLE Stroj (
    idStroj INT PRIMARY KEY AUTO_INCREMENT,
    nazwaStroju VARCHAR(255),
    dataUtworzenia DATE,
    dataWaznosci DATE,
    firma VARCHAR(255),
    wlasciciel VARCHAR(255)
);

CREATE TABLE Materialy (
    idMaterial INT PRIMARY KEY AUTO_INCREMENT,
    nazwaMaterialu VARCHAR(255),
    kategoria VARCHAR(100),
    kolor VARCHAR(100),
    rozmiar VARCHAR(1)
);

CREATE TABLE Kreacja (
    idKreacja INT PRIMARY KEY AUTO_INCREMENT,
    idElement INT,
    idStroj INT,
    idMaterial INT,
    FOREIGN KEY (idStroju) REFERENCES Stroj(idStroju),
    FOREIGN KEY (idMaterialu) REFERENCES Materialy(idMaterialu),
    dataUtworzenia DATE
);


