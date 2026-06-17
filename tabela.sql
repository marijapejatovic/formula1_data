CREATE TABLE IF NOT EXISTS dimStatus (
    statusId INT PRIMARY KEY,
    status VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS dimConstructors (
    constructorId INT PRIMARY KEY,
    constructorRef VARCHAR(200),
    constructor_name VARCHAR(200),
    constructor_nationality VARCHAR(200),
    constructor_url VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS dimDriver (
    driverId INT PRIMARY KEY,
    driverRef VARCHAR(200),
    number INT,
    code VARCHAR(200),
    forename VARCHAR(200),
    surname VARCHAR(200),
    nationality VARCHAR(200),
    driver_url VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS dimRace (
    raceId INT PRIMARY KEY,
    year INT,
    round INT,
    race_name VARCHAR(200),
    race_url VARCHAR(200),
    quali_date DATE,
    quali_time VARCHAR(200),
    date DATE,
    races_time VARCHAR(200),
    sprint_date DATE,
    sprint_time VARCHAR(200),
    fp1_date DATE,
    fp1_time VARCHAR(200),
    fp2_date DATE,
    fp2_time VARCHAR(200),
    fp3_date DATE,
    fp3_time VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS dimCircuit (
    circuitId INT PRIMARY KEY,
    circuitRef VARCHAR(200),
    circuit_name VARCHAR(200),
    location VARCHAR(200),
    country VARCHAR(200),
    lat FLOAT,
    lng FLOAT,
    alt FLOAT,
    circuit_url VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS dimDriverStandings (
    driverStandingsId INT PRIMARY KEY,
    driverstandings_points FLOAT,
    driverstandings_position INT,
    driverstandings_positionText VARCHAR(200),
    wins INT
);

CREATE TABLE IF NOT EXISTS dimConstructorStandings (
    constructorStandingsId INT PRIMARY KEY,
    constructorstandings_points FLOAT,
    constructorstandings_position INT,
    constructorstandings_positionText VARCHAR(200),
    constructorstandings_wins INT
);

CREATE TABLE IF NOT EXISTS dimDate (
    dateId INT PRIMARY KEY,
    date DATE,
    year INT,
    month INT,
    day INT
);

CREATE TABLE IF NOT EXISTS factResults (
    id INT PRIMARY KEY,
    resultId INT,
    raceId INT,
    driverId INT,
    constructorId INT,
    statusId INT,
    circuitId INT,
    driverStandingsId INT,
    constructorStandingsId INT,
    dateId INT,
    points FLOAT,
    position INT,
    positionText VARCHAR(200),
    positionOrder INT,
    grid INT,
    laps INT,
    time VARCHAR(200),
    milliseconds INT,
    rank INT,
    fastestLap INT,
    fastestLapTime VARCHAR(200),
    fastestLapSpeed FLOAT,

    CONSTRAINT fk_raceId FOREIGN KEY (raceId) REFERENCES dimRace(raceId),
    CONSTRAINT fk_driverId FOREIGN KEY (driverId) REFERENCES dimDriver(driverId),
    CONSTRAINT fk_constructorId FOREIGN KEY (constructorId) REFERENCES dimConstructors(constructorId),
    CONSTRAINT fk_statusId FOREIGN KEY (statusId) REFERENCES dimStatus(statusId),
    CONSTRAINT fk_driverStandingsId FOREIGN KEY (driverStandingsId) REFERENCES dimDriverStandings(driverStandingsId),
    CONSTRAINT fk_constructorStandingsId FOREIGN KEY (constructorStandingsId) REFERENCES dimConstructorStandings(constructorStandingsId),
    CONSTRAINT fk_dateId FOREIGN KEY (dateId) REFERENCES dimDate(dateId),
    CONSTRAINT fk_circuitId FOREIGN KEY (circuitId) REFERENCES dimCircuit(circuitId)
);

CREATE TABLE IF NOT EXISTS factLap (
    raceId INT,
    driverId INT,
    lap INT,
    laptimes_position INT,
    laptimes_time VARCHAR(200),
    laptimes_milliseconds INT,
    PRIMARY KEY (raceId, driverId, lap),
    CONSTRAINT fklap_raceId FOREIGN KEY (raceId) REFERENCES dimRace(raceId),
    CONSTRAINT fklap_driverId FOREIGN KEY (driverId) REFERENCES dimDriver(driverId)
);

CREATE TABLE IF NOT EXISTS factPitstop (
    raceId INT,
    driverId INT,
    stop INT,
    pitstops_time VARCHAR(200),
    duration FLOAT,
    pitstops_milliseconds INT,
    PRIMARY KEY (raceId, driverId, stop),
    CONSTRAINT fkpitstops_raceId FOREIGN KEY (raceId) REFERENCES dimRace(raceId),
    CONSTRAINT fkpitstops_driverId FOREIGN KEY (driverId) REFERENCES dimDriver(driverId)
);