SELECT 
    g.genero AS genero,
    COUNT(v.id_pasajeroV) AS num_pasajeros,
    (COUNT(v.id_pasajeroV) * 100.0 / (SELECT COUNT(*) FROM FACTVuelo)) AS porcentaje
FROM 
    FACTVuelo v
JOIN 
    DIMGenero g ON v.id_genero = g.id_genero
GROUP BY 
    g.genero;


