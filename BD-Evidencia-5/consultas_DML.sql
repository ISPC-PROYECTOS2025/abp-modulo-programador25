USE bd_gestion;

INSERT INTO usuario (nombre_usuario, correo_electronico, contrasena, fecha_registro) VALUES
('Jesica', 'jesivaldi@hotmail.com', '1234', '2025-09-07'),
('Ana', 'Ana_hartl@hotmail.com', '1235', '2025-09-08'),
('Francisco', 'franserafini@hotmail.com', '1236', '2025-09-08'),
('Santiago', 'santibri@hotmail.com', '1237', '2025-09-09'),
('Juan', 'Juanavazques@hotmail.com', '1238', '2025-09-09'),
('Marisa', 'mariperez@hotmail.com', '1239', '2025-09-10'),
('Claudia', 'clautorres@hotmail.com', '1240', '2025-09-10'),
('Mario', 'mario_lopez@hotmail.com', '1241', '2025-09-11'),
('Pablo', 'pablito22@hotmail.com', '12874', '2025-09-11'),
('Valentina','valentina@gmail.com','12875','2025-09-10');

INSERT INTO dispositivo (id_usuario, nombre, tipo, fecha_registro) VALUES
(1,'Sensor Temperatura','Sensor','2025-09-01'),
(2,'Lámpara LED','Actuador','2025-09-01'),
(3,'Cámara IP','Sensor','2025-09-03'),
(4,'Sensor Humedad','Sensor','2025-09-04'),
(5,'Termostato','Actuador','2025-09-05'),
(6,'Sensor Movimiento','Sensor','2025-09-05'),
(7,'Bombilla Inteligente','Actuador','2025-09-06'),
(8,'Cerradura Smart','Actuador','2025-09-07'),
(9,'Sensor Luz','Sensor','2025-09-07'),
(10,'Alarma','Actuador','2025-09-08');


INSERT INTO notificaciones (id_usuario, mensaje, fecha_hora) VALUES
(1,'Temperatura alta','2025-09-12 08:00:00'),
(2,'Humedad baja','2025-09-12 09:00:00'),
(3,'Cámara encendida','2025-09-13 10:00:00'),
(4,'Termostato ajustado','2025-09-13 11:00:00'),
(5,'Movimiento detectado','2025-09-14 12:00:00'),
(6,'Luz encendida','2025-09-14 13:00:00'),
(7,'Puerta abierta','2025-09-15 14:00:00'),
(8,'Sensor luz activado','2025-09-15 15:00:00'),
(9,'Alarma activada','2025-09-16 16:00:00'),
(10,'Usuario registrado','2025-09-16 17:00:00');

INSERT INTO automatizacion (id_usuario, id_dispositivo, condicion, fecha_hora) VALUES
(1,1,'38°C','2025-09-12 08:10:00'),
(1,2,'Encender si temperatura 38°C','2025-09-12 08:20:00'),
(2,3,'Detectar movimiento','2025-09-13 10:10:00'),
(3,4,'Encender si humedad <40%','2025-09-13 11:10:00'),
(4,5,'Apagar si movimiento','2025-09-14 12:10:00'),
(5,6,'Encender a las 20:00','2025-09-14 13:10:00'),
(6,7,'Cerrar si puerta abierta','2025-09-15 14:10:00'),
(7,8,'Activar si luz <50','2025-09-15 15:10:00'),
(8,9,'Activar alarma si movimiento','2025-09-16 16:10:00'),
(9,1,'Medir temperatura cada 10 min','2025-09-16 17:10:00');


SELECT * FROM usuario;
SELECT * FROM dispositivo;
SELECT * FROM notificaciones;
SELECT * FROM automatizacion;

SELECT nombre_usuario, correo_electronico FROM usuario WHERE id_usuario <= 5;

UPDATE usuario
SET contrasena = 'jesi1234'
WHERE id_usuario = 1;

