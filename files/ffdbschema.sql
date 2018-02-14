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

CREATE TABLE users (
    ssn CHAR(10),
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (ssn),
    CONSTRAINT ssn_match CHECK (ssn ~ '[0-9]{10}')
);

CREATE TABLE bookings (
    flightid INT REFERENCES flights (id),
    ssn CHAR(11) REFERENCES users (ssn),
    PRIMARY KEY (flightid, ssn)
);

CREATE TABLE seats (
    flightid INT REFERENCES flights (id),
    seats INT,
    booked INT,
    CONSTRAINT seat_check CHECK (booked <= seats)
);