WITH AgeGenderCounts AS (
    SELECT 
        g.genero AS gender,
        f.edad_pasajero AS age,
        COUNT(f.id_vuelo) AS flight_count
    FROM 
        FACTVuelo f
    JOIN 
        DIMGenero g ON f.id_genero = g.id_genero
    GROUP BY 
        g.genero, f.edad_pasajero
),
RankedAges AS (
    SELECT
        gender,
        age,
        flight_count,
        ROW_NUMBER() OVER (PARTITION BY gender ORDER BY flight_count DESC) AS rank
    FROM
        AgeGenderCounts
)
SELECT
    gender,
    age,
    flight_count
FROM
    RankedAges
WHERE
    rank <= 5
ORDER BY
    gender, rank;
