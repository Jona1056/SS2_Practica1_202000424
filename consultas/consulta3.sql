SELECT 
    n.nacionalidad,
    FORMAT(d.fecha, 'MM-yyyy') AS mes_anio,
    COUNT(f.id_vuelo) AS total_salidas
FROM 
    FACTVuelo f
JOIN 
    DIMNacionalidad n ON f.id_nacionalidad = n.id_nacionalidad
JOIN 
    DIMFecha d ON f.id_fecha = d.id_fecha
GROUP BY 
    n.nacionalidad,
    FORMAT(d.fecha, 'MM-yyyy')
ORDER BY 
    n.nacionalidad, mes_anio;
