CREATE TABLE airports (
    airportname VARCHAR(255),
    PRIMARY KEY (airportname)
);

CREATE TABLE flights (
    id SERIAL,
    flno VARCHAR(20),
    dateof date,
    timeof time,
    origin VARCHAR(255) REFERENCES airports (airportname),
    destination VARCHAR(255) REFERENCES airports(airportname),
    traveltime INT,
    PRIMARY KEY (id)
);

CREATE TABLE seats (
    flightid INT,
    seatid VARCHAR(3),
    booked BOOLEAN,
    PRIMARY KEY (flightid, seatid)
);

CREATE TABLE users (
    ssn CHAR(10),
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (ssn),
    CONSTRAINT ssn_match CHECK (ssn ~ '[0-9]{10}')
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    ssn CHAR(10) REFERENCES users (ssn),
    flightid INT REFERENCES flights (id),
    seatid VARCHAR(3),
    UNIQUE(flightid, seatid),
    FOREIGN KEY (flightid, seatid) REFERENCES seats(flightid, seatid)
);