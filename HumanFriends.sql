CREATE DATABASE IF NOT EXISTS HumanFriends;
USE HumanFriends;

create table AnimalGroup(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name varchar(30)
);

create table AnimalView(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name varchar(30),
group_id INT,
foreign key(group_id) references AnimalGroup (id) on delete
cascade on update cascade
);

create table Comands (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
command varchar(30),
id_animal INT
);

drop table Comands;
insert into Comands(command,id_animal)
values
 ('Сидеть',1),
 ('К ноге',1),
 ('Вперед',3),
 ('Вперед',2),
 ('Кушать',2),
 ('Кушать',1);
drop table Comands;

CREATE TABLE Animals_of_the_nursery (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(30),
    birthDate DATE,
    view_id INT,
    FOREIGN KEY (view_id) REFERENCES AnimalView(id) ON DELETE CASCADE ON UPDATE CASCADE
);




drop table Animals_of_the_nursery;


insert into AnimalGroup(name)
values
 ('Вьючные животные'),
 ('Домашние животные');
 

 
 insert into AnimalView(name,group_id)
 values
 ('Кошка', 2),
 ('Собака',2),
 ('Хомяк',2),
 ('Лошадь', 1),
 ('Верблюд', 1),
 ('Осел', 1);
 USE HumanFriends;
 insert into Animals_of_the_nursery(name,birthDate,view_id)
 values
 ('Черныш','2023-01-17',1),
 ('Мисса','2022-01-17',2),
 ('верблюд','2023-05-17',5);
 
 
 

  insert into Animals_of_the_nursery(name,birthDate,view_id,command_id)
 values
 ('Черныш','2023-01-17',1,3);
drop table Animals_of_the_nursery;
delete from Animals_of_the_nursery where view_id=5;
USE HumanFriends;


create table TableHorseDonkey as
select * from Animals_of_the_nursery where view_id=4
union
select * from Animals_of_the_nursery where view_id=6;


SELECT * FROM animalview ;

create table Age_of_animals as
	select id,name,birthDate,
    datediff(curdate(),birthDate) div 31 as age,view_id
    from Animals_of_the_nursery
    where date_add(birthDate, interval 1 year)<curdate() and
		date_add(birthDate, interval 3 year) > curdate();
  create table FULL_tables as      
   select id, name, birthDate, view_id from TableHorseDonkey
   union ALL
   select id, name, birthDate, view_id from Age_of_animals;        
   
   USE HumanFriends;
   drop table FULL_tables;
