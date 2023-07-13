delete from clientes_orm_area;
delete from clientes_orm_personal;
delete from clientes_orm_estudio;
delete from clientes_orm_autor;

insert into clientes_orm_autor values(1,True,'2023-02-21','2023-02-23','Paula Dorian Roldan',1);
insert into clientes_orm_autor values(2,True,'2023-02-21','2023-02-20','Daniel Juarez Lopez',1);
insert into clientes_orm_autor values(3,True,'2023-02-21','2023-02-19','Adrian Jimenez Cacho',1);
insert into clientes_orm_autor values(4,True,'2023-02-19','2023-02-21','Raul Soria Chavez',1);
insert into clientes_orm_autor values(5,True,'2023-02-18','2023-02-22','Juan Suarez Gomez',1);
insert into clientes_orm_area values(1,True,'2023-02-21','2023-02-23','Sistemas',1);
insert into clientes_orm_area values(2,True,'2023-02-21','2023-02-20','Contabilidad',1);
insert into clientes_orm_area values(3,True,'2023-02-21','2023-02-19','Ventas',1);
insert into clientes_orm_area values(4,True,'2023-02-19','2023-02-21','Programacion',1);
insert into clientes_orm_area values(5,True,'2023-02-18','2023-02-22','Marketing',1);

insert into clientes_orm_estudio values(1,True,'2023-02-21','2023-02-23','Tenico',1);
insert into clientes_orm_estudio values(2,True,'2023-02-21','2023-02-20','Maestria',1);
insert into clientes_orm_estudio values(3,True,'2023-02-21','2023-02-19','Secundaria',1);
insert into clientes_orm_estudio values(4,True,'2023-02-19','2023-02-21','Preparatoria',1);
insert into clientes_orm_estudio values(5,True,'2023-02-18','2023-02-22','Universidad',1);


insert into clientes_orm_personal values(1,True,'2023-02-21','2023-02-23','Juan Carlos','Roldan','Soria','imagenes/descarga_1.jpg','Ingeniero',2,3,1);
insert into clientes_orm_personal values(2,True,'2023-02-21','2023-02-23','Daniel','Suarez','Ramirez','imagenes/descarga_1.jpg','Sistemas',2,1,1);
insert into clientes_orm_personal values(3,True,'2023-02-21','2023-02-23','Javier','Martino','Garcia','imagenes/descarga_1.jpg','Contabilidad',1,2,1);
insert into clientes_orm_personal values(4,True,'2023-02-21','2023-02-23','Leonel','Lora','Cordova','imagenes/descarga_1.jpg','Diseño',3,3,1);
insert into clientes_orm_personal values(5,True,'2023-02-21','2023-02-23','Graciela','Garza','Sartre','imagenes/descarga_1.jpg','Administracion',1,4,1);

