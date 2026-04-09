-- flights.sql
-- Sprint 1: Core flights table for search functionality.
-- Stores departure, destination, date/time, and price.

CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique flight ID
    flight_number VARCHAR(20) NOT NULL,      -- Airline flight number
    departure VARCHAR(50) NOT NULL,          -- Departure airport/city
    destination VARCHAR(50) NOT NULL,        -- Destination airport/city
    departure_datetime DATETIME NOT NULL,    -- Full departure date/time
    arrival_datetime DATETIME NOT NULL,      -- Full arrival date/time
    price DECIMAL(10,2) NOT NULL             -- Ticket price
);