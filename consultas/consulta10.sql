SELECT 
    FORMAT(d.fecha, 'MM-yyyy') AS month_year,
    COUNT(f.id_vuelo) AS total_flights
FROM 
    FACTVuelo f
JOIN 
    DIMFecha d ON f.id_fecha = d.id_fecha
GROUP BY 
    FORMAT(d.fecha, 'MM-yyyy')
ORDER BY 
    month_year;
