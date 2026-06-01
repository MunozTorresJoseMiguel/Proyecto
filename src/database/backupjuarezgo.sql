-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.17.0.7270
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para juarezgo
CREATE DATABASE IF NOT EXISTS `juarezgo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `juarezgo`;

-- Volcando estructura para tabla juarezgo.paradas
CREATE TABLE IF NOT EXISTS `paradas` (
  `id_parada` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_parada` varchar(100) DEFAULT NULL,
  `latitud` decimal(10,7) DEFAULT NULL,
  `longitud` decimal(10,7) DEFAULT NULL,
  PRIMARY KEY (`id_parada`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.paradas: ~8 rows (aproximadamente)
INSERT INTO `paradas` (`id_parada`, `nombre_parada`, `latitud`, `longitud`) VALUES
	(1, 'Tecnologico', NULL, NULL),
	(2, 'Las Torres', NULL, NULL),
	(3, 'Pronaf', NULL, NULL),
	(4, 'Centro', NULL, NULL),
	(5, 'sorina zaragoza', NULL, NULL),
	(6, 'smart aztecas', NULL, NULL),
	(7, 'walmart gran patio', NULL, NULL),
	(8, 'aztecas', NULL, NULL);

-- Volcando estructura para tabla juarezgo.recorrido_ruta
CREATE TABLE IF NOT EXISTS `recorrido_ruta` (
  `id_recorrido` int(11) NOT NULL AUTO_INCREMENT,
  `id_ruta` int(11) DEFAULT NULL,
  `id_parada` int(11) DEFAULT NULL,
  `orden_parada` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_recorrido`),
  KEY `id_ruta` (`id_ruta`),
  KEY `id_parada` (`id_parada`),
  CONSTRAINT `recorrido_ruta_ibfk_1` FOREIGN KEY (`id_ruta`) REFERENCES `rutas` (`id_ruta`),
  CONSTRAINT `recorrido_ruta_ibfk_2` FOREIGN KEY (`id_parada`) REFERENCES `paradas` (`id_parada`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.recorrido_ruta: ~16 rows (aproximadamente)
INSERT INTO `recorrido_ruta` (`id_recorrido`, `id_ruta`, `id_parada`, `orden_parada`) VALUES
	(1, 1, 1, 1),
	(2, 1, 2, 2),
	(3, 1, 3, 3),
	(4, 1, 4, 4),
	(5, 2, 7, 1),
	(6, 2, 5, 2),
	(7, 2, 4, 3),
	(8, 3, 1, 1),
	(9, 3, 2, 2),
	(10, 3, 5, 3),
	(11, 4, 8, 1),
	(12, 4, 1, 2),
	(13, 4, 4, 3),
	(14, 5, 6, 1),
	(15, 5, 5, 2),
	(16, 5, 4, 3);

-- Volcando estructura para tabla juarezgo.rutas
CREATE TABLE IF NOT EXISTS `rutas` (
  `id_ruta` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_ruta` varchar(100) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `tiempo_promedio` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ruta`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.rutas: ~5 rows (aproximadamente)
INSERT INTO `rutas` (`id_ruta`, `nombre_ruta`, `descripcion`, `tiempo_promedio`) VALUES
	(1, 'Ruta Centro', 'Recorre el centro y zonas principales', 40),
	(2, 'Pantoja', 'kilometro 20 ,eje vial, cerezo,centro', 24),
	(3, '5A', 'Recorre todo juarez', 55),
	(4, 'universitaria ', 'AUCJ', 20),
	(5, 'Cerezo', 'Militares', 15);

-- Volcando estructura para tabla juarezgo.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.usuarios: ~4 rows (aproximadamente)
INSERT INTO `usuarios` (`id_usuario`, `nombre`, `correo`, `contrasena`, `fecha_registro`) VALUES
	(9, 'MiguelJose', 'eltaquitosalsa@gmail.com', '$2b$12$IwhVEjI0RagZ1rOMsgzNv.2SZ9OWZdHGT9pq2lrqAmm0mLkvFTF7a', '2026-05-19 06:12:21'),
	(10, 'Joaquin', 'Joaquin@gmail.com', '$2b$12$/6ymbzXPQ5zYps6nHzgNmu5jKy1x8ZW/OBj6PgDuIpEVkK3umX9gi', '2026-05-19 12:48:37'),
	(11, 'marisol', 'marisol@gmail.com', '$2b$12$oXUrqzPIwoO1JS/std2m9ujP801crS0ncLTh6Vxtj.SYsU6Q1v6km', '2026-05-19 20:46:55'),
	(12, 'ADMIN', 'admin@gmail.com', '$2b$12$Kc/SqRH3bHVmYhXtdJf3q.OOO0EZXoh/AvZOmnEcHAuFjR5nBNdUm', '2026-05-27 12:37:42');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
