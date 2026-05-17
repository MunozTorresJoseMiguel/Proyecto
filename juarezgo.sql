-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.paradas: ~0 rows (aproximadamente)
DELETE FROM `paradas`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.recorrido_ruta: ~0 rows (aproximadamente)
DELETE FROM `recorrido_ruta`;

-- Volcando estructura para tabla juarezgo.rutas
CREATE TABLE IF NOT EXISTS `rutas` (
  `id_ruta` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_ruta` varchar(100) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `tiempo_promedio` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ruta`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.rutas: ~0 rows (aproximadamente)
DELETE FROM `rutas`;
INSERT INTO `rutas` (`id_ruta`, `nombre_ruta`, `descripcion`, `tiempo_promedio`) VALUES
	(1, 'Ruta Centro', 'Recorre el centro y zonas principales', 40);

-- Volcando estructura para tabla juarezgo.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla juarezgo.usuarios: ~1 rows (aproximadamente)
DELETE FROM `usuarios`;
INSERT INTO `usuarios` (`id_usuario`, `nombre`, `correo`, `contrasena`, `fecha_registro`) VALUES
	(1, 'Juan', 'juan@gmail.com', '123456', '2026-05-11 06:40:49'),
	(2, 'Marisol Medina', 'medina@gmail.com', '654321', '2026-02-13 20:46:02');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
