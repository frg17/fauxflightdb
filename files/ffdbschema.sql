CREATE TABLE airports (
    id SERIAL,
    airportname VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE flights (
    id SERIAL,
    flno VARCHAR(20),
    dateof date,
    timeof time,
    origin int REFERENCES airports (id),
    destination int REFERENCES airports(id),
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
    FOREIGN KEY (flightid, seatid) REFERENCES seats(flightid, seatid)
);