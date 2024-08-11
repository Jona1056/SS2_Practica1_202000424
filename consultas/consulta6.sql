SELECT 
    e.estado AS estado_vuelo,
    COUNT(f.id_vuelo) AS total_vuelos
FROM 
    FACTVuelo f
JOIN 
    DIMEstado e ON f.id_estado = e.id_estado
GROUP BY 
    e.estado;
