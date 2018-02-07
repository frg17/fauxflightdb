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

CREATE TABLE bookings (
    flightid INT REFERENCES flights (id),
    seats INT,
    booked INT DEFAULT 0,
    PRIMARY KEY (flightid)
);