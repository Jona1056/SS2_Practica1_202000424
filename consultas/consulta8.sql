SELECT TOP 5
    c.continente AS continent,
    COUNT(f.id_vuelo) AS flight_count
FROM 
    FACTVuelo f
JOIN 
    DIMAereopuerto a ON f.id_aeropuerto = a.id_aeropuerto
JOIN 
    DIMPais p ON a.id_pais = p.id_pais
JOIN 
    DIMContinente c ON p.id_continente = c.id_continente
GROUP BY 
    c.continente
ORDER BY 
    flight_count DESC;
