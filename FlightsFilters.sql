-- Flights table for Jetstream Sprint 1.
-- Stores departure, destination, date/time, and price.

CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    departure VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    departure_datetime DATETIME NOT NULL,
    arrival_datetime DATETIME NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
