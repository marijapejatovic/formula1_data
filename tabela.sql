create table IF NOT EXISTS DIM_Status(
    statusId int primary key,
    status VARCHAR(200)
);
create table IF NOT EXISTS DIM_Constructors(
    constructorId int primary key,
    constructorRef VARCHAR(200),
    name VARCHAR(200),
    nationality_constructor VARCHAR(200),
    url_constructors VARCHAR(200)
);
create table IF NOT EXISTS DIM_Driver(
    driverId int primary key,
    driverRef VARCHAR(200),
    number int,
    code VARCHAR(200),
    forename VARCHAR(200),
    surname VARCHAR(200),
    nationality VARCHAR(200),
    url VARCHAR(200)
);
create table IF NOT EXISTS DIM_Race(
    raceId int primary key,
    year int,
    round int,
    name_x VARCHAR(200),
    URL_X varchar(200),
    quali_date date,
    quali_time time,
    date date,
    time_races time,
    sprint_date date,
    sprint_time time
);
create table if not exists DIM_Circuit(
    circuitId int primary key,
    circuitRef VARCHAR(200),
    name_y VARCHAR(200),
    location VARCHAR(200),
    country VARCHAR(200),
    lat float,
    lng float,
    alt float,
    url_y VARCHAR(200)
);
create table if not exists DIM_driverStandings(
    driverStandingsId int primary key,
    points_driverstandings FLOAT,
    position_driverstandings int,
    positionText_driverstandings varchar(200),
    wins int
);
create table if not exists DIM_constructorStandings(
    constructorStandingsId int primary key,
    points_constructorstandings FLOAT,
    position_constructorstandings int,
    positionText_constructorstandings varchar(200),
    wins_constructorstandings int
);
create table if not exists DIM_date(
    dateId int primary key,
    date DATE,
    year int,
    month int,
    day int,
    quarter int
);
create table if not exists FACT(
    id int primary key,
    resultId int ,
    raceId int,
    driverId int,
    constructorId int,
    statusId int,
    circuitId int,
    driverStandingsId int,
    constructorStandingsId int,
    dateId int,
    points FLOAT,
    position int,
    positionText varchar(200),
    positionOrder int,
    grid int,
    laps int,
    time time,
    milliseconds int,
    rank int,
    fastestLap int,
    fastestLapTime time,
    fastestLapSpeed float,


    constraint fk_raceId  foreign key (raceId) references DIM_Race(raceId),
    constraint fk_driverId foreign key (driverId)references DIM_Driver(driverId),
    constraint fk_constructorId foreign key (constructorId) references DIM_Constructors(constructorId),
    constraint fk_statusId foreign key (statusId) references DIM_Status(statusId),
    constraint fk_driverStandingsId foreign key (driverStandingsId) references DIM_driverStandings(driverStandingsId),
    constraint fk_constructorStandingsId foreign key (constructorStandingsId) references DIM_constructorStandings(constructorStandingsId),
    constraint fk_dateId foreign key (dateId) references DIM_date(dateId),
    constraint fk_circuitId  foreign key (circuitId) references DIM_Circuit(circuitId)

);
create table if not exists FACT_Lap(
    raceId int,
    driverId int,
    lap int,
    position_laptimes int,
    time_laptimes time,
    milliseconds_laptimes int,
    primary key(raceId, driverId, lap),
    constraint fklap_raceId foreign key(raceId) references DIM_Race(raceId),
    constraint fklap_driverId foreign key(driverId) references DIM_Driver(driverId)
);
create table if not exists FACT_LapPitstops(
    raceId int,
    driverId int,
    stop int,
    time_pitstops time,
    duration interval,
    milliseconds_pitstops int,
    primary key(raceId, driverId,stop),
    constraint fkpitstops_raceId foreign key(raceId) references DIM_Race(raceId),
    constraint fkpitstops_driverId foreign key(driverId) references DIM_Driver(driverId)
);

