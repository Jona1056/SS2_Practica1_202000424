DROP TABLE IF EXISTS FACTVuelo;

-- Eliminar las tablas de dimensiones en el orden correcto
DROP TABLE IF EXISTS DIMPasajeros;
DROP TABLE IF EXISTS DIMNacionalidad;
DROP TABLE IF EXISTS DIMGenero;
DROP TABLE IF EXISTS DIMAereopuerto;
DROP TABLE IF EXISTS DIMPais;
DROP TABLE IF EXISTS DIMContinente;
DROP TABLE IF EXISTS DIMPiloto;
DROP TABLE IF EXISTS DIMEstado;
DROP TABLE IF EXISTS DIMFecha;
DROP TABLE IF EXISTS ProvisionalFlightInfo