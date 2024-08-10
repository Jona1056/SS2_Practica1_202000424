CREATE TABLE DIMGenero (
    id_genero INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    genero VARCHAR(50) NOT NULL
);

CREATE Table DIMNacionalidad(
    id_nacionalidad INT PRIMARY KEY IDENTITY(1,1)  NOT NULL,
    nacionalidad VARCHAR(100) NOT NULL,
)




CREATE TABLE DIMEstado(
    id_estado INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    estado VARCHAR(50) NOT NULL,
)

CREATE TABLE DIMContinente(
    id_continente INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    continente VARCHAR(50) NOT NULL,
     
    codigo_continente VARCHAR(10) NOT NULL,

)

CREATE TABLE DIMPais(
    id_pais INT PRIMARY KEY  IDENTITY(1,1) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    codigo_pais VARCHAR(10) NOT NULL,
    id_continente INT NOT NULL,
    FOREIGN KEY (id_continente) REFERENCES DIMContinente(id_continente),
)

CREATE TABLE DIMAereopuerto(
    id_aeropuerto INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    aeropuerto VARCHAR(100) NOT NULL,
    siglas VARCHAR(10) NOT NULL,
    id_pais INT NOT NULL,
    FOREIGN KEY (id_pais) REFERENCES DIMPais(id_pais),
)

CREATE TABLE DIMFecha(
    id_fecha INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    fecha DATE NOT NULL,

)
CREATE TABLE FACTVuelo (
    id_vuelo INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    nombre_piloto VARCHAR(100) NOT NULL,
    id_aeropuerto INT NOT NULL,
    id_fecha INT NOT NULL,
    id_estado INT NOT NULL,
    id_genero INT NOT NULL,
    id_nacionalidad INT NOT NULL,
    id_pasajeroV VARCHAR(100) NULL,
    nombre_pasajero VARCHAR(100) NOT NULL,
    apellido_pasajero VARCHAR(100) NOT NULL,
    edad_pasajero INT NOT NULL,
    FOREIGN KEY (id_aeropuerto) REFERENCES DIMAereopuerto(id_aeropuerto),
    FOREIGN KEY (id_fecha) REFERENCES DIMFecha(id_fecha),
    FOREIGN KEY (id_estado) REFERENCES DIMEstado(id_estado),
    FOREIGN KEY (id_genero) REFERENCES DIMGenero(id_genero),
    FOREIGN KEY (id_nacionalidad) REFERENCES DIMNacionalidad(id_nacionalidad)
);

CREATE TABLE ProvisionalFlightInfo (
    PassengerID VARCHAR(50),
    FirstName VARCHAR(100) NULL,
    LastName VARCHAR(100) NULL,
    Gender VARCHAR(10) NULL,
    Age INT NULL,
    Nationality VARCHAR(100) NULL,
    AirportName VARCHAR(100) NULL,
    AirportCountryCode VARCHAR(10) NULL,
    CountryName VARCHAR(100) NULL,
    AirportContinent VARCHAR(50) NULL,
    Continents VARCHAR(50) NULL,
    DepartureDate DATE NULL,
    ArrivalAirport VARCHAR(100) NULL,
    PilotName VARCHAR(100) NULL,
    FlightStatus VARCHAR(50) NULL
);