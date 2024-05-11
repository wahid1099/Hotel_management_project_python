-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 11, 2024 at 04:02 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ooproject_htelmngmnt`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `booking_id` int(11) NOT NULL,
  `room_number` int(11) DEFAULT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `customer_email` varchar(255) DEFAULT NULL,
  `check_in_date` varchar(255) DEFAULT NULL,
  `check_out_date` varchar(255) DEFAULT NULL,
  `total_bill` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`booking_id`, `room_number`, `customer_name`, `customer_email`, `check_in_date`, `check_out_date`, `total_bill`) VALUES
(1, 103, 'wahid', 'wahid123@gmail.com', '0000-00-00', '0000-00-00', 4000),
(2, 105, 'sadman zahid', 'wa@gmail.com', '10/01/2024', '10/02/2024', 5500),
(3, 103, 'wahid', 'wa@gmail.com', '10/02/2024', '12/02/2024', 4000);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `check_in_date` varchar(255) DEFAULT NULL,
  `check_out_date` varchar(255) DEFAULT NULL,
  `room_no` int(11) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `address`, `check_in_date`, `check_out_date`, `room_no`, `user_email`) VALUES
(1, 'wa', 'dd', '0000-00-00', '0000-00-00', 101, 'abc@gmail.com'),
(2, 'wahid ahmeed', 'dhaka,bangladesh', '2/03/2024', '5/03/2025', 102, 'abc@gmail.com'),
(3, 'SADMAN', 'DHAKA', '10/02/2023', '10/05/2024', 101, 'abc@gmail.com'),
(4, 'ZARIR', 'DHAKA', '10/02/2024', '10/05/2025', 102, 'abc@gmail.com'),
(5, 'wahid khan', 'dhaka', '10/04/2024', '10/05/2024', 103, 'wahid@gmail.com'),
(6, 'wahid', 'dhaka', '10/02/2025/', '10/02/2026', 102, 'a@gmail.com'),
(7, 'wahid', 'saidpur', '10/03/2024', '12/03/2024', 103, 'wahid123@gmail.com'),
(8, 'sadman zahid', 'bogura', '10/01/2024', '10/02/2024', 105, 'sad@gmail.com'),
(9, 'wahid', 'dhk', '10/02/2024', '12/02/2024', 103, ' wa@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `room_number` int(11) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `is_booked` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`room_number`, `price`, `is_booked`) VALUES
(101, 6000, 0),
(102, 5000, 0),
(103, 4000, 1),
(104, 3000, 0),
(105, 5500, 1),
(106, 4500, 0),
(107, 3500, 0),
(108, 2500, 0),
(109, 7000, 0),
(110, 6200, 0),
(111, 5100, 0),
(112, 4800, 0),
(113, 4200, 0),
(114, 3900, 0),
(115, 3200, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pasword` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `pasword`) VALUES
(1, 's@gmail.com', '55899899'),
(2, 'wa@gmail.com', '123456'),
(3, 'zr@gmail.com', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `room_number` (`room_number`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`room_number`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`room_number`) REFERENCES `rooms` (`room_number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
