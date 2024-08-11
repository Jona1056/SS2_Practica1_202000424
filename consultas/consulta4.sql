SELECT 
    p.pais AS country,
    COUNT(f.id_vuelo) AS flight_count
FROM 
    FACTVuelo f
JOIN 
    DIMAereopuerto a ON f.id_aeropuerto = a.id_aeropuerto
JOIN 
    DIMPais p ON a.id_pais = p.id_pais
GROUP BY 
    p.pais
ORDER BY 
    flight_count DESC;
