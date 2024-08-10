from config.db_config import (
    DatabaseConnection,
)  # Importa la clase desde el archivo config
import csv


def menu():
    print("1. Borrar Modelo")
    print("2. Crear Modelo")
    print("3. Extraer Informacion")
    print("4. Cargar Informacion")
    print("5. Realizar Consultas")
    print("6. Exit")
    opcion = input("Elige una opcion: ")
    return opcion


def main():
    # Crear una instancia de la conexión
    db_instance = DatabaseConnection()

    while True:
        opcion = menu()
        if opcion == "1":
            with open("delete_tables.sql", "r") as file:
                sql_script = file.read()

            try:
                query, error = db_instance.execute_query(sql_script)
                if query:
                    print("")
                    print("Tablas borradas correctamente")
                    print("")
                else:
                    print("")
                    print("No se pudieron borrar las tablas", error)
                    print("")
            except Exception as e:
                print("")
                print("Error al ejecutar el script SQL")
                print(e)
                print("")

        elif opcion == "2":
            # ejecturar script
            with open("create_tables.sql", "r") as file:
                sql_script = file.read()
            try:
                query, error = db_instance.execute_query(sql_script)
                if query:
                    print("")
                    print("Tablas creadas correctamente")
                    print("")
                else:
                    print("")
                    print("No se pudieron crear las tablas", error)
                    print("")
            except Exception as e:
                print("")
                print("Error al ejecutar el script SQL")
                print(e)
                print("")

        elif opcion == "3":
            # cargar informacion
            print("")
            print("Extraer Informacion")
            Ruta = input("Escribe la ruta del archivo: ")
            # obtener datos de un csv
            with open(Ruta, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                contador = 1
                for row in reader:
                    id_passenger = (
                        row["Passenger ID"] if row["Passenger ID"] else "None"
                    )
                    name_passenger = row["First Name"] if row["First Name"] else "None"
                    lastname_passenger = (
                        row["Last Name"] if row["Last Name"] else "None"
                    )
                    Gender = row["Gender"] if row["Gender"] else "None"
                    Age = row["Age"] if row["Age"] else 0
                    Nationality = row["Nationality"] if row["Nationality"] else "None"
                    Airport_Name = (
                        row["Airport Name"] if row["Airport Name"] else "None"
                    )
                    Airport_Country_Code = (
                        row["Airport Country Code"]
                        if row["Airport Country Code"]
                        else "None"
                    )
                    Country_Name = (
                        row["Country Name"] if row["Country Name"] else "None"
                    )
                    Airport_Continent = (
                        row["Airport Continent"] if row["Airport Continent"] else "None"
                    )
                    Continents = row["Continents"] if row["Continents"] else "None"
                    Departure_Date = (
                        row["Departure Date"] if row["Departure Date"] else "1970-01-01"
                    )
                    Arrival_Airport = (
                        row["Arrival Airport"] if row["Arrival Airport"] else "None"
                    )
                    Pilot_Name = row["Pilot Name"] if row["Pilot Name"] else "None"
                    Flight_Status = (
                        row["Flight Status"] if row["Flight Status"] else "None"
                    )

                    id_passenger = id_passenger.replace("'", "''")
                    name_passenger = name_passenger.replace("'", "''")
                    lastname_passenger = lastname_passenger.replace("'", "''")
                    Gender = Gender.replace("'", "''")
                    Nationality = Nationality.replace("'", "''")
                    Airport_Name = Airport_Name.replace("'", "''")
                    Airport_Country_Code = Airport_Country_Code.replace("'", "''")
                    Country_Name = Country_Name.replace("'", "''")
                    Airport_Continent = Airport_Continent.replace("'", "''")
                    Continents = Continents.replace("'", "''")
                    Departure_Date = Departure_Date.replace("'", "''")
                    Arrival_Airport = Arrival_Airport.replace("'", "''")
                    Pilot_Name = Pilot_Name.replace("'", "''")
                    Flight_Status = Flight_Status.replace("'", "''")

                    query = f"INSERT INTO ProvisionalFlightInfo (PassengerID, FirstName, LastName, Gender,Age, Nationality, AirportName, AirportCountryCode,CountryName,AirportContinent,Continents,DepartureDate,ArrivalAirport,PilotName,FlightStatus) VALUES ('{id_passenger}', '{name_passenger}', '{lastname_passenger}', '{Gender}', '{Age}', '{Nationality}', '{Airport_Name}', '{Airport_Country_Code}', '{Country_Name}', '{Airport_Continent}', '{Continents}', '{Departure_Date}', '{Arrival_Airport}', '{Pilot_Name}', '{Flight_Status}')"
                    try:
                        result, error = db_instance.execute_query(query)
                        if not result:
                             print(f"Error al insertar fila: {error}")
                   
                    except Exception as e:
                        print(f"Error al insertar fila: {e}")
                print("")

        elif opcion == "4":
            query = """
                        SELECT 
                            PassengerID,
                            REPLACE(REPLACE(REPLACE(FirstName, '.', ''), ';', ''), '/', '') AS CleanFirstName,
                            REPLACE(REPLACE(REPLACE(LastName, '.', ''), ';', ''), '/', '') AS CleanLastName,
                            Gender,
                            Age,
                            Nationality,
                            AirportName,
                            AirportCountryCode,
                            CountryName,
                            AirportContinent,
                            Continents,
                            DepartureDate,
                            ArrivalAirport,
                            PilotName,
                            FlightStatus
                        FROM 
                            ProvisionalFlightInfo;
                        """

            try:
                resultados, error = db_instance.fetch_data(query)
                if error:
                    print(f"Error al obtener datos: {error}")
                    continue
                else:
                    for row in resultados:
                        genero = row[3]
                    # Verificar si el género existe en la tabla DIMGenero
                        query = f"SELECT id_genero FROM DIMGenero WHERE genero = '{genero}'"
                        result, error = db_instance.fetch_data(query)
                        
                        if error:
                            print(result)
                            print(f"Error al verificar género: {error}")
                            continue
                
                        if not result:  
                            query = f"INSERT INTO DIMGenero (genero) VALUES ('{genero}')"
                            success, message = db_instance.execute_query(query)
                   
                            if success:
                                query = f"SELECT id_genero FROM DIMGenero WHERE genero = '{genero}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID del nuevo género: {error}")
                                    continue
                            else:
                                print(f"Error al insertar género: {message}")
                                continue
                        
                        # Obtener el ID del género
                        id_genero = result[0][0]
                        Nationality = row[5]
                        #lo mismo 
                        query = f"SELECT id_nacionalidad FROM DIMNacionalidad WHERE nacionalidad = '{Nationality}'"
                        result, error = db_instance.fetch_data(query)
                        if error:
                            print(f"Error al verificar nacionalidad: {error}")
                            continue
                        if not result:
                            query = f"INSERT INTO DIMNacionalidad (nacionalidad) VALUES ('{Nationality}')"
                            success, message = db_instance.execute_query(query)
                            if success:
                                query = f"SELECT id_nacionalidad FROM DIMNacionalidad WHERE nacionalidad = '{Nationality}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID de la nueva nacionalidad: {error}")
                                    continue
                            else:
                                print(f"Error al insertar nacionalidad: {message}")
                                continue
                        # Obtener el ID de la nacionalidad
                        id_nacionalidad = result[0][0]
                        id_passenger = row[0]
                        firstName = row[1].replace("'", "''")  # Escapar comillas simples
                        lastname = row[2].replace("'", "''")  # Escapar comillas simples
                        age = row[4]

                        nombre_continente = row[10].replace("'", "''")
                        codigo_continente = row[9].replace("'", "''")
                       
                        #continente 
                        query = f"SELECT id_continente FROM DIMContinente WHERE continente = '{nombre_continente}'"
                        result, error = db_instance.fetch_data(query)
                        if error:
                            print(f"Error al verificar continente: {error}")
                            continue
                        if not result:
                            query = f"INSERT INTO DIMContinente (continente, codigo_continente) VALUES ('{nombre_continente}', '{codigo_continente}')"
                            success, message = db_instance.execute_query(query)
                            if success:
                                query = f"SELECT id_continente FROM DIMContinente WHERE continente = '{nombre_continente}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID del nuevo continente: {error}")
                                    continue
                            else:
                                print(f"Error al insertar continente: {message}")
                                continue
                        id_continente = result[0][0]
                        #PAIS
                       
                        codigo_pais = row[7].replace("'", "''")
                        nombre_pais = row[8].replace("'", "''")
                      
                        #pais
                        query = f"SELECT id_pais FROM DIMPais WHERE pais = '{nombre_pais}'"
                        result, error = db_instance.fetch_data(query)
                        if error:
                            print(f"Error al verificar pais: {error}")
                            continue
                        if not result:
                            query = f"INSERT INTO DIMPais (pais, codigo_pais, id_continente) VALUES ('{nombre_pais}', '{codigo_pais}', {id_continente})"
                            success, message = db_instance.execute_query(query)
                            if success:
                                query = f"SELECT id_pais FROM DIMPais WHERE pais = '{nombre_pais}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID del nuevo pais: {error}")
                                    continue
                            else:
                                print(f"Error al insertar pais: {message}")
                                continue
                        id_pais = result[0][0]
                       
                        #AEROPUERTO
                        nombre_aeropuerto = row[6].replace("'", "''")
                        codigo_aeropuerto = row[12].replace("'", "''")
                        ##verificar si el codigo_aerepuerto es 0 saltar
                        if codigo_aeropuerto == "0":
                            continue
                        #aeropuerto
                        query = f"SELECT id_aeropuerto FROM DIMAereopuerto WHERE aeropuerto = '{nombre_aeropuerto}'"
                        result, error = db_instance.fetch_data(query)
                        if error:
                            print(f"Error al verificar aeropuerto: {error}")
                            continue
                        if not result:
                            query = f"INSERT INTO DIMAereopuerto (aeropuerto,siglas, id_pais) VALUES ('{nombre_aeropuerto}', '{codigo_aeropuerto}', {id_pais})"
                            success, message = db_instance.execute_query(query)
                            if success:
                                query = f"SELECT id_aeropuerto FROM DIMAereopuerto WHERE aeropuerto = '{nombre_aeropuerto}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID del nuevo aeropuerto: {error}")
                                    continue
                            else:
                                print(f"Error al insertar aeropuerto: {message}")
                                continue
                        id_aeropuerto = result[0][0]
                        
                        #status
                        status = row[14].replace("'", "''")
                        query = f"SELECT id_estado FROM DIMEstado WHERE estado = '{status}'"
                        result, error = db_instance.fetch_data(query)
                        if error:
                            print(f"Error al verificar status: {error}")
                            continue
                        if not result:
                            query = f"INSERT INTO DIMEstado (estado) VALUES ('{status}')"
                            success, message = db_instance.execute_query(query)
                            if success:
                                query = f"SELECT id_estado FROM DIMEstado WHERE estado = '{status}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID del nuevo status: {error}")
                                    continue
                            else:
                                print(f"Error al insertar status: {message}")
                                continue
                        id_status = result[0][0]
                        fecha = row[11].replace("'", "''")
                        #Vuelo
                        query = f"SELECT id_fecha FROM DIMFecha WHERE fecha = '{fecha}'"
                        result, error = db_instance.fetch_data(query)
                        if error:
                            print(f"Error al verificar fecha: {error}")
                            continue
                        if not result:
                            query = f"INSERT INTO  DIMFecha (fecha) VALUES ('{fecha}')"
                            success, message = db_instance.execute_query(query)
                            if success:
                                query = f"SELECT id_fecha FROM  DIMFecha WHERE fecha = '{fecha}'"
                                result, error = db_instance.fetch_data(query)
                                if error:
                                    print(f"Error al obtener el ID de la nueva fecha: {error}")
                                    continue
                            else:
                                print(f"Error al insertar fecha: {message}")
                                continue

                        id_fecha = result[0][0]

                    # Insertar vuelo en FACTVuelo
                        nombre_piloto = row[13].replace("'", "''")
                        query = f"""
                            INSERT INTO FACTVuelo (
                                nombre_piloto, id_aeropuerto, id_fecha, id_estado, 
                                id_genero, id_nacionalidad, id_pasajeroV, 
                                nombre_pasajero, apellido_pasajero, edad_pasajero
                            ) VALUES (
                                '{nombre_piloto}', {id_aeropuerto}, {id_fecha}, {id_status}, 
                                {id_genero}, {id_nacionalidad}, '{id_passenger}', 
                                '{firstName}', '{lastname}', {age}
                            )
                        """
                        success, message = db_instance.execute_query(query)
                        if not success:
                            print(f"Error al insertar vuelo: {message}")
                            continue


                            
                        
                        
                        
                      
                        
                            

            except Exception as e:
                 
                    print(f"Error al obtener datos: {e}")
                    continue
                # Cerrar la conexión

        elif opcion == "5":
            print("Realizar Consultas")
            # Aquí podrías realizar más consultas
        elif opcion == "6":
            break
        else:
            print("Opcion Incorrecta")
            print("")

    # Cerrar la conexión
    db_instance.close_connection()


if __name__ == "__main__":
    main()
