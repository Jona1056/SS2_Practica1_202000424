SELECT 
    p.pais AS nombre_pais,
    COUNT(f.id_vuelo) AS total_vuelos
FROM 
    FACTVuelo f
JOIN 
    DIMAereopuerto a ON f.id_aeropuerto = a.id_aeropuerto
JOIN 
    DIMPais p ON a.id_pais = p.id_pais
GROUP BY 
    p.pais
ORDER BY 
    total_vuelos DESC
OFFSET 0 ROWS
FETCH NEXT 5 ROWS ONLY;