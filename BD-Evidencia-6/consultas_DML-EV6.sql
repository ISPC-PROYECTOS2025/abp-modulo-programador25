-- Datos inciales
-- Usuarios
INSERT INTO usuario (nombre_usuario, correo_electronico, contrasena, fecha_registro, rol) VALUES
('Gabriela', 'gaby_volm@hotmail.com', '1234567', '2025-05-01', 'estandar'),
('Franco', 'Franco_tribu@hotmail.com', 'franco12345', '2025-03-18', 'estandar'),
('Lucia', 'lucia_merida@gmail.com', '1236lucia', '2025-03-05', 'estandar'),
('Mariano', 'marianobri@hotmail.com', 'mariano1237', '2025-05-09', 'estandar'),
('Julio', 'juliovazques@hotmail.com', 'julio1238', '2025-06-12', 'estandar'),
('Ricardo', 'ricardoperez@hotmail.com', '12541239', '2025-06-29', 'admin'),
('Analia', 'anatorres@hotmail.com', 'juli1240', '2025-07-04', 'estandar'),
('Paola', 'paola_lopez@hotmail.com', 'pao1241', '2025-07-11', 'estandar'),
('Paula', 'pau2022@gmail.com', '202212874', '2025-09-04', 'estandar'),
('Valentin','valentin_2012@gmail.com','valen12875','2025-09-10','estandar');

-- Dispositivos
INSERT INTO dispositivo (id_usuario, nombre, tipo, fecha_registro) VALUES
(1, 'Detector de Gas', 'Sensor', '2025-10-10'),
(1, 'Enchufe Inteligente', 'Actuador', '2025-10-09'),
(2, 'Sensor de Vibración', 'Sensor', '2025-10-08'),
(2, 'Cámara Exterior', 'Sensor', '2025-10-11'),
(3, 'Persiana Automática', 'Actuador', '2025-10-10'),
(3, 'Sensor de Lluvia', 'Sensor', '2025-10-12'),
(2, 'Riego Automático', 'Actuador', '2025-10-12'),
(1, 'Sirena Inteligente', 'Actuador', '2025-10-07'),
(3, 'Medidor de Energía', 'Sensor', '2025-10-11'),
(2, 'Cámara Interior', 'Sensor', '2025-10-09');

-- Notificaciones
INSERT INTO notificaciones (id_usuario, mensaje, fecha_hora) VALUES
(1, 'El detector de gas ha detectado una fuga.', '2025-10-10 08:45:00'),
(1, 'El enchufe inteligente fue apagado automáticamente.', '2025-10-09 19:30:00'),
(2, 'Vibración detectada en la pared del garaje.', '2025-10-08 21:15:00'),
(2, 'La cámara exterior detectó movimiento.', '2025-10-11 22:05:00'),
(3, 'Persiana automática bajada por condiciones climáticas.', '2025-10-10 18:10:00'),
(3, 'Sensor de lluvia activado. Riego detenido.', '2025-10-12 09:00:00'),
(2, 'Sistema de riego automático activado correctamente.', '2025-10-12 07:45:00'),
(1, 'Sirena inteligente activada por detección de intruso.', '2025-10-07 23:59:00'),
(3, 'Medidor de energía registró consumo elevado.', '2025-10-11 12:20:00'),
(2, 'Cámara interior detectó movimiento en el living.', '2025-10-09 20:40:00');

-- Automatización
INSERT INTO automatizacion (id_usuario, id_dispositivo, condicion, fecha_hora) VALUES
(1, 1, 'Apagar el sistema si se detecta gas.', '2025-10-10 08:00:00'),
(2, 2, 'Encender el enchufe inteligente al detectar presencia.', '2025-10-09 19:00:00'),
(3, 3, 'Enviar alerta si hay vibración prolongada.', '2025-10-08 21:00:00'),
(4, 4, 'Grabar video al detectar movimiento.', '2025-10-11 22:00:00'),
(5, 5, 'Bajar persianas cuando haya viento fuerte.', '2025-10-10 18:00:00'),
(6, 6, 'Desactivar riego si se detecta lluvia.', '2025-10-12 09:00:00'),
(2, 7, 'Activar riego a las 07:30 todos los días.', '2025-10-12 07:30:00'),
(1, 8, 'Activar sirena si se detecta movimiento en la noche.', '2025-10-07 23:45:00'),
(3, 9, 'Enviar alerta si el consumo supera los 500W.', '2025-10-11 12:00:00'),
(2, 10, 'Encender luz si se detecta movimiento en interior.', '2025-10-09 20:30:00');


-- CONSULTAS SIMPLES
SELECT * FROM usuario;
SELECT * FROM dispositivo;
SELECT * FROM notificaciones;
SELECT * FROM automatizacion;

-- CONSULTAS MULTITABLA

-- Consulta 1: Mostrar todos los dispositivos con su usuario
-- Permite al administrador identificar qué usuario posee cada dispositivo en el sistema.
SELECT u.nombre_usuario, d.nombre AS dispositivo, d.tipo
FROM usuario u
JOIN dispositivo d ON u.id_usuario = d.id_usuario;

-- Consulta 2: Cantidad de dispositivos por usuario
-- Permite analizar la distribución de dispositivos entre usuarios y detectar usuarios con muchos o pocos dispositivos.
SELECT u.nombre_usuario, COUNT(d.id_dispositivo) AS cantidad_dispositivos
FROM usuario u
LEFT JOIN dispositivo d ON u.id_usuario = d.id_usuario
GROUP BY u.nombre_usuario;

-- Consulta 3: Dispositivos agregados en los últimos 3 días con su usuario
-- Permite al administrador identificar dispositivos recién registrados y su propietario para seguimiento.
SELECT d.nombre AS dispositivo, d.tipo, d.fecha_registro, u.nombre_usuario AS dueño
FROM dispositivo d
JOIN usuario u ON d.id_usuario = u.id_usuario
WHERE d.fecha_registro >= CURDATE() - INTERVAL 3 DAY
ORDER BY d.fecha_registro DESC;

-- Consulta 4: Usuarios con dispositivos recientes y cantidad
-- Permite detectar usuarios activos y su nivel de participación reciente.
SELECT u.nombre_usuario, COUNT(d.id_dispositivo) AS dispositivos_recientes
FROM usuario u
JOIN dispositivo d ON u.id_usuario = d.id_usuario
WHERE d.fecha_registro >= CURDATE() - INTERVAL 3 DAY
GROUP BY u.nombre_usuario
ORDER BY dispositivos_recientes DESC;

-- Consulta 5: Usuarios inactivos (no registran dispositivos hace 2 años)
-- Permite identificar usuarios que podrían estar inactivos y planificar acciones de reactivación
SELECT u.nombre_usuario, MAX(d.fecha_registro) AS ultimo_dispositivo
FROM usuario u
LEFT JOIN dispositivo d ON u.id_usuario = d.id_usuario
GROUP BY u.id_usuario
HAVING MAX(d.fecha_registro) < CURDATE() - INTERVAL 2 YEAR
   OR MAX(d.fecha_registro) IS NULL;  -- Incluye usuarios que nunca registraron dispositivos


-- SUBCONSULTAS

-- Usuarios que tienen más de 2 dispositivos
-- Permite identificar usuarios avanzados que poseen más de 2 dispositivos, útil para análisis de comportamiento.
SELECT nombre_usuario
FROM usuario
WHERE id_usuario IN (
    SELECT id_usuario
    FROM dispositivo
    GROUP BY id_usuario
    HAVING COUNT(*) > 2
);

-- Dispositivo más reciente registrado por cada usuario
-- Permite conocer el último dispositivo agregado por cada usuario, útil para seguimiento y posibles mejoras en la aplicación.
SELECT u.nombre_usuario, d.nombre AS dispositivo, d.fecha_registro
FROM usuario u
JOIN dispositivo d ON u.id_usuario = d.id_usuario
WHERE d.fecha_registro = (
    SELECT MAX(fecha_registro)
    FROM dispositivo
    WHERE id_usuario = u.id_usuario
);
