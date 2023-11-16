# librerías
from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Utilizamos un contexto "with" para garantizar que el archivo se cierre adecuadamente
    with open(file_path, 'r') as file1:
        # Utilizamos list comprehension para cargar en memoria las líneas del archivo y obtener los datos necesarios
        data = [
            {
                "date": datetime.strptime(json_value["date"][:10], "%Y-%m-%d").date(),
                "user": json_value["user"]["username"],
                "id": json_value["id"]
            }
            for json_value in map(json.loads, file1.readlines())
        ]
    # Creamos un DataFrame directamente desde la lista de datos
    tweets_data = pd.DataFrame(data)
    # Obtenemos los 10 días con más tweets
    top_10_days = tweets_data['date'].value_counts().nlargest(10).index
    # Filtramos los datos para el top 10 de días
    tweets_data = tweets_data[tweets_data['date'].isin(top_10_days)]
    # Agrupamos por fecha y usuario y contamos el número de tweets
    tweets_data = tweets_data.groupby(["date", "user"]).size().reset_index(name='count')
    # Obtenemos el usuario con mayor número de tweets por día
    idx = tweets_data.groupby('date')['count'].idxmax()
    tweets_data = tweets_data.loc[idx]
    # Transformamos en lista de tuplas para cumplir el tipo de dato de salida
    result = list(tweets_data.itertuples(index=False, name=None))
    return result