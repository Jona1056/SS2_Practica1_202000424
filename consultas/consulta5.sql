SELECT 
    a.aeropuerto,
    SUM(f.edad_pasajero) AS total_pasajeros
FROM 
    FACTVuelo f
JOIN 
    DIMAereopuerto a ON f.id_aeropuerto = a.id_aeropuerto
GROUP BY 
    a.aeropuerto
ORDER BY 
    total_pasajeros DESC
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY;
