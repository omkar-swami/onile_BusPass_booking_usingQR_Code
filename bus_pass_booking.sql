CREATE DATABASE  IF NOT EXISTS `bus_pass_booking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bus_pass_booking`;
-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bus_pass_booking
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `applications`
--

DROP TABLE IF EXISTS `applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applications` (
  `application_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `pass_type_id` int DEFAULT NULL,
  `route_id` int DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `applied_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applications`
--

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;
INSERT INTO `applications` VALUES (1,2,1,2,'Approved','2026-03-10'),(2,5,1,8,'Approved','2026-03-10'),(3,4,1,18,'Approved','2026-03-11'),(4,3,1,30,'Approved','2026-03-11'),(5,12,NULL,NULL,'Pending','2026-03-14'),(6,12,NULL,NULL,'Pending','2026-03-14'),(7,12,1,3,'Pending','2026-03-14');
/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bus_pass`
--

DROP TABLE IF EXISTS `bus_pass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus_pass` (
  `pass_id` int DEFAULT NULL,
  `pass_type_id` int DEFAULT NULL,
  `application_id` int DEFAULT NULL,
  `base_amount` decimal(10,2) DEFAULT NULL,
  `discount_amount` decimal(10,2) DEFAULT NULL,
  `final_amount` decimal(10,2) DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `Status` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus_pass`
--

LOCK TABLES `bus_pass` WRITE;
/*!40000 ALTER TABLE `bus_pass` DISABLE KEYS */;
INSERT INTO `bus_pass` VALUES (1,1,1,4125.00,1650.00,2475.00,'2026-03-10','2026-04-09','Approved'),(2,1,2,4500.00,1800.00,2700.00,'2026-03-10','2026-04-09','Approved'),(3,1,3,4875.00,487.00,4387.00,'2026-03-11','2026-04-10','Approved'),(4,1,4,4500.00,2700.00,1800.00,'2026-03-11','2026-04-10','Approved'),(5,1,7,1350.00,540.00,810.00,'2026-03-14','2026-04-13','Pending');
/*!40000 ALTER TABLE `bus_pass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_types`
--

DROP TABLE IF EXISTS `document_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document_types` (
  `document_type_id` int DEFAULT NULL,
  `document_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_types`
--

LOCK TABLES `document_types` WRITE;
/*!40000 ALTER TABLE `document_types` DISABLE KEYS */;
INSERT INTO `document_types` VALUES (1,'Student ID'),(2,'Employee ID'),(3,'Aadhar Card'),(4,'Address Proof'),(5,'Disability Certificate'),(6,'photo');
/*!40000 ALTER TABLE `document_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentdetails`
--

DROP TABLE IF EXISTS `documentdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentdetails` (
  `documentDet_id` int DEFAULT NULL,
  `document_id` int DEFAULT NULL,
  `document_type_id` int DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentdetails`
--

LOCK TABLES `documentdetails` WRITE;
/*!40000 ALTER TABLE `documentdetails` DISABLE KEYS */;
INSERT INTO `documentdetails` VALUES (1,1,2,'A1_U2_Employee ID.png'),(2,1,3,'A1_U2_Aadhar Card.png'),(3,1,4,'A1_U2_Address Proof.png'),(4,1,6,'A1_U2_photo.png'),(5,2,2,'A2_U5_Employee ID.png'),(6,2,3,'A2_U5_Aadhar Card.png'),(7,2,4,'A2_U5_Address Proof.png'),(8,2,6,'A2_U5_photo.png'),(9,3,3,'A3_U4_Aadhar Card.png'),(10,3,4,'A3_U4_Address Proof.png'),(11,3,6,'A3_U4_photo.png'),(12,4,1,'A4_U3_Student ID.png'),(13,4,3,'A4_U3_Aadhar Card.png'),(14,4,4,'A4_U3_Address Proof.png'),(15,4,6,'A4_U3_photo.png'),(16,5,2,'A7_U12_Employee ID.png'),(17,5,3,'A7_U12_Aadhar Card.png'),(18,5,4,'A7_U12_Address Proof.png'),(19,5,6,'A7_U12_photo.png');
/*!40000 ALTER TABLE `documentdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentsmaster`
--

DROP TABLE IF EXISTS `documentsmaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentsmaster` (
  `document_id` int DEFAULT NULL,
  `application_id` int DEFAULT NULL,
  `uploaded_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentsmaster`
--

LOCK TABLES `documentsmaster` WRITE;
/*!40000 ALTER TABLE `documentsmaster` DISABLE KEYS */;
INSERT INTO `documentsmaster` VALUES (1,1,'2026-03-10'),(2,2,'2026-03-10'),(3,3,'2026-03-11'),(4,4,'2026-03-11'),(5,7,'2026-03-14');
/*!40000 ALTER TABLE `documentsmaster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pass_discounts`
--

DROP TABLE IF EXISTS `pass_discounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pass_discounts` (
  `discount_id` int DEFAULT NULL,
  `user_type_id` int DEFAULT NULL,
  `pass_type_id` int DEFAULT NULL,
  `discount_percentage` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pass_discounts`
--

LOCK TABLES `pass_discounts` WRITE;
/*!40000 ALTER TABLE `pass_discounts` DISABLE KEYS */;
INSERT INTO `pass_discounts` VALUES (1,1,1,60.00),(2,2,1,40.00),(3,3,1,20.00),(4,1,2,60.00),(5,2,2,40.00),(6,3,1,10.00),(7,4,1,50.00),(8,5,1,70.00),(9,3,2,15.00),(10,4,2,55.00),(11,5,2,75.00),(12,1,3,35.00),(13,2,3,20.00),(14,4,3,50.00),(15,1,4,45.00),(16,5,4,70.00),(17,2,5,15.00),(18,4,5,40.00),(19,3,6,20.00),(20,1,6,40.00);
/*!40000 ALTER TABLE `pass_discounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pass_type`
--

DROP TABLE IF EXISTS `pass_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pass_type` (
  `pass_type_id` int DEFAULT NULL,
  `pass_name` varchar(50) DEFAULT NULL,
  `validity_days` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pass_type`
--

LOCK TABLES `pass_type` WRITE;
/*!40000 ALTER TABLE `pass_type` DISABLE KEYS */;
INSERT INTO `pass_type` VALUES (1,'Monthly',30),(2,'Yearly',365),(3,'Quarterly',90),(4,'Half-Yearly',180),(5,'Weekly',7),(6,'Five Months ',150);
/*!40000 ALTER TABLE `pass_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pass_type_required_documents`
--

DROP TABLE IF EXISTS `pass_type_required_documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pass_type_required_documents` (
  `doc_req_id` int DEFAULT NULL,
  `pass_type_id` int DEFAULT NULL,
  `document_type_id` int DEFAULT NULL,
  `user_type_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pass_type_required_documents`
--

LOCK TABLES `pass_type_required_documents` WRITE;
/*!40000 ALTER TABLE `pass_type_required_documents` DISABLE KEYS */;
INSERT INTO `pass_type_required_documents` VALUES (1,1,1,1),(2,1,3,1),(3,1,4,1),(4,1,6,1),(5,1,2,2),(6,1,3,2),(7,1,4,2),(8,1,6,2),(9,1,3,3),(10,1,4,3),(11,1,6,3),(12,1,3,4),(13,1,4,4),(14,1,6,4),(15,1,5,5),(16,1,3,5),(17,1,4,5),(18,1,6,5),(19,2,1,1),(20,2,3,1),(21,2,4,1),(22,2,6,1),(23,2,2,2),(24,2,3,2),(25,2,4,2),(26,2,6,2),(27,2,3,3),(28,2,4,3),(29,2,6,3),(30,2,3,4),(31,2,4,4),(32,2,6,4),(33,2,5,5),(34,2,3,5),(35,2,4,5),(36,2,6,5),(37,3,1,1),(38,3,3,1),(39,3,4,1),(40,3,6,1),(41,3,2,2),(42,3,3,2),(43,3,4,2),(44,3,6,2),(45,3,3,3),(46,3,4,3),(47,3,6,3),(48,3,3,4),(49,3,4,4),(50,3,6,4),(51,3,5,5),(52,3,3,5),(53,3,4,5),(54,3,6,5),(55,4,1,1),(56,4,3,1),(57,4,4,1),(58,4,6,1),(59,4,2,2),(60,4,3,2),(61,4,4,2),(62,4,6,2),(63,4,3,3),(64,4,4,3),(65,4,6,3),(66,4,3,4),(67,4,4,4),(68,4,6,4),(69,4,5,5),(70,4,3,5),(71,4,4,5),(72,4,6,5),(73,5,1,1),(74,5,3,1),(75,5,4,1),(76,5,6,1),(77,5,2,2),(78,5,3,2),(79,5,4,2),(80,5,6,2),(81,5,3,3),(82,5,4,3),(83,5,6,3),(84,5,3,4),(85,5,4,4),(86,5,6,4),(87,5,5,5),(88,5,3,5),(89,5,4,5),(90,5,6,5),(91,6,1,1),(92,6,3,1),(93,6,4,1),(94,6,6,1),(95,6,2,2),(96,6,3,2),(97,6,4,2),(98,6,6,2),(99,6,3,3),(100,6,4,3),(101,6,6,3),(102,6,3,4),(103,6,4,4),(104,6,6,4),(105,6,5,5),(106,6,3,5),(107,6,4,5),(108,6,6,5);
/*!40000 ALTER TABLE `pass_type_required_documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int DEFAULT NULL,
  `application_id` int DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,1,2475.00,'2026-03-10'),(2,2,2700.00,'2026-03-10'),(3,3,4387.00,'2026-03-11'),(4,4,1800.00,'2026-03-11'),(5,7,810.00,'2026-03-14');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routes`
--

DROP TABLE IF EXISTS `routes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routes` (
  `route_id` int DEFAULT NULL,
  `route_source` varchar(100) DEFAULT NULL,
  `route_destination` varchar(100) DEFAULT NULL,
  `distance_km` decimal(6,2) DEFAULT NULL,
  `price_per_km` decimal(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routes`
--

LOCK TABLES `routes` WRITE;
/*!40000 ALTER TABLE `routes` DISABLE KEYS */;
INSERT INTO `routes` VALUES (1,'Kolhapur','Kagal',20.00,1.00),(2,'Kolhapur','Radhanagari',55.00,1.00),(3,'Kolhapur','Gargoti',45.00,1.00),(4,'Kolhapur','Ichalkaranji',30.00,1.00),(5,'Kolhapur','Ajra',85.00,1.00),(6,'Kolhapur','Gadhinglaj',65.00,1.00),(7,'Kagal','Gargoti',35.00,1.00),(8,'Kagal','Radhanagari',60.00,1.00),(9,'Kagal','Gadhinglaj',25.00,1.00),(10,'Kagal','Ajra',70.00,1.00),(11,'Radhanagari','Gargoti',25.00,1.00),(12,'Radhanagari','Ajra',60.00,1.00),(13,'Radhanagari','Gadhinglaj',75.00,1.00),(14,'Radhanagari','Ichalkaranji',80.00,1.00),(15,'Radhanagari','Kagal',60.00,1.00),(16,'Gargoti','Ajra',50.00,1.00),(17,'Gargoti','Gadhinglaj',40.00,1.00),(18,'Gargoti','Ichalkaranji',65.00,1.00),(19,'Gargoti','Kagal',35.00,1.00),(20,'Gargoti','Kolhapur',45.00,1.00),(21,'Ichalkaranji','Kagal',25.00,1.00),(22,'Ichalkaranji','Gadhinglaj',55.00,1.00),(23,'Ichalkaranji','Ajra',90.00,1.00),(24,'Ichalkaranji','Radhanagari',80.00,1.00),(25,'Ichalkaranji','Kolhapur',30.00,1.00),(26,'Gadhinglaj','Ajra',30.00,1.00),(27,'Gadhinglaj','Kolhapur',65.00,1.00),(28,'Ajra','Kolhapur',85.00,1.00),(29,'Ajra','Kagal',70.00,1.00),(30,'Ajra','Radhanagari',60.00,1.00),(31,'Kolhapur','Panhala',20.00,1.00),(32,'Kolhapur','Nipani',25.00,1.00),(33,'Kolhapur','Hupari',23.00,1.00),(34,'Kolhapur','Shiroli',12.00,1.00),(35,'Kolhapur','Ujalaiwadi',10.00,1.00),(36,'Kolhapur','Kanerimath',15.00,1.00),(37,'Kolhapur','Gokul Shirgaon',14.00,1.00),(38,'Kolhapur','Valivade',18.00,1.00),(39,'Panhala','Nipani',30.00,1.00),(40,'Panhala','Hupari',28.00,1.00),(41,'Panhala','Shiroli',22.00,1.00),(42,'Nipani','Hupari',20.00,1.00),(43,'Nipani','Kagal',25.00,1.00),(44,'Hupari','Ichalkaranji',15.00,1.00),(45,'Hupari','Kagal',18.00,1.00),(46,'Shiroli','Gokul Shirgaon',8.00,1.00),(47,'Shiroli','Valivade',12.00,1.00),(48,'Kanerimath','Panhala',18.00,1.00),(49,'Gokul Shirgaon','Kagal',16.00,1.00),(50,'Valivade','Hupari',17.00,1.00),(51,'Kolhapur','Murgud',40.00,1.00),(52,'Kolhapur','Senapati Kapshi',60.00,1.00),(53,'Kolhapur','Kuditre',25.00,1.00),(54,'Kolhapur','Kasaba Bawada',5.00,1.00),(55,'Kolhapur','Balinga',12.00,1.00),(56,'Kolhapur','Chandgad',95.00,1.00),(57,'Kolhapur','Nesari',70.00,1.00),(58,'Kolhapur','Kapshi',60.00,1.00),(59,'Kolhapur','Kowad',85.00,1.00),(60,'Kolhapur','Kadgaon',50.00,1.00),(61,'Murgud','Gargoti',30.00,1.00),(62,'Murgud','Senapati Kapshi',22.00,1.00),(63,'Murgud','Nipani',35.00,1.00),(64,'Murgud','Kagal',20.00,1.00),(65,'Murgud','Ajra',55.00,1.00),(66,'Murgud','Gadhinglaj',30.00,1.00),(67,'Murgud','Radhanagari',40.00,1.00),(68,'Murgud','Ichalkaranji',25.00,1.00),(69,'Murgud','Hupari',28.00,1.00),(70,'Murgud','Nesari',40.00,1.00),(71,'Senapati Kapshi','Nesari',12.00,1.00),(72,'Senapati Kapshi','Gadhinglaj',18.00,1.00),(73,'Senapati Kapshi','Ajra',35.00,1.00),(74,'Senapati Kapshi','Kagal',28.00,1.00),(75,'Senapati Kapshi','Nipani',20.00,1.00),(76,'Senapati Kapshi','Murgud',22.00,1.00),(77,'Senapati Kapshi','Gargoti',45.00,1.00),(78,'Senapati Kapshi','Kolhapur',60.00,1.00),(79,'Gargoti','Kadgaon',15.00,1.00),(80,'Gargoti','Chandgad',60.00,1.00),(81,'Gargoti','Kowad',70.00,1.00),(82,'Gargoti','Nesari',50.00,1.00),(83,'Gargoti','Kapshi',45.00,1.00),(84,'Gargoti','Murgud',30.00,1.00),(85,'Radhanagari','Kadgaon',20.00,1.00),(86,'Radhanagari','Chandgad',70.00,1.00),(87,'Radhanagari','Kowad',80.00,1.00),(88,'Radhanagari','Nesari',60.00,1.00),(89,'Radhanagari','Kapshi',55.00,1.00),(90,'Nipani','Murgud',35.00,1.00),(91,'Nipani','Senapati Kapshi',20.00,1.00),(92,'Nipani','Gadhinglaj',45.00,1.00),(93,'Nipani','Ajra',75.00,1.00),(94,'Nipani','Ichalkaranji',40.00,1.00),(95,'Kagal','Murgud',20.00,1.00),(96,'Kagal','Senapati Kapshi',28.00,1.00),(97,'Kagal','Nesari',40.00,1.00),(98,'Kagal','Kadgaon',35.00,1.00),(99,'Kagal','Kapshi',30.00,1.00),(100,'Kagal','Chandgad',75.00,1.00);
/*!40000 ALTER TABLE `routes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_type`
--

DROP TABLE IF EXISTS `user_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_type` (
  `user_type_id` int DEFAULT NULL,
  `type_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_type`
--

LOCK TABLES `user_type` WRITE;
/*!40000 ALTER TABLE `user_type` DISABLE KEYS */;
INSERT INTO `user_type` VALUES (1,'Student'),(2,'Employee'),(3,'Normal'),(4,'Senior Citizen'),(5,'Disabled');
/*!40000 ALTER TABLE `user_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int DEFAULT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `address` text,
  `user_type_id` int NOT NULL,
  `created_at` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Omkar Swami','omkar@gmail.com','9876543210','12345','Pune, Maharashtra',1,'2026-02-01'),(2,'Rahul Patil','rahul@gmail.com','9123456780','rahul@123','Mumbai, Maharashtra',2,'2026-02-02'),(3,'Sneha Joshi','sneha@gmail.com','9988776655','sneha@123','Nagpur, Maharashtra',1,'2026-02-03'),(4,'Amit Sharma','amit@gmail.com','9012345678','amit@123','Delhi, India',3,'2026-02-04'),(5,'Priya Deshmukh','priya@gmail.com','8899776655','priya@123','Nashik, Maharashtra',2,'2026-02-05'),(7,'Anjali Mehta','anjali@gmail.com','9090909090','anjali@123','Ahmedabad, Gujarat',2,'2026-02-07'),(8,'Vikram Singh','vikram@gmail.com','8787878787','vikram@123','Jaipur, Rajasthan',3,'2026-02-08'),(9,'Pooja Kulkarni','pooja@gmail.com','9696969696','pooja@123','Kolhapur, Maharashtra',1,'2026-02-09'),(10,'Karan Malhotra','karan@gmail.com','8585858585','karan@123','Hyderabad, Telangana',2,'2026-02-10'),(11,'nilesh','nilesh@gmail.com','7845961236','Demo@1234','sadashivnager',2,'2026-02-14'),(12,'Rahul patil','rahul@gmail.com','9786541230','Rahul@12345','Kolhapur',2,'2026-03-14'),(13,'demo','rahul@gmail.com','9635857410','Rahul@12345','Kolhapur',1,'2026-03-14'),(14,'Omkar Swami','rahul@gmail.com','9876543210','Rahul@12345','kolhapur',3,'2026-03-14'),(15,'Omkar Swami','swamiomkar17@gmail.com','7845961236','Omkar@123','sadashivnager',3,'2026-03-14');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-16  9:59:52
