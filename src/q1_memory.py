from typing import List, Tuple
from datetime import datetime
import pandas as pd
from collections import defaultdict
import json
import os
from datetime import datetime

def q1_memory(file_path):
    file_lines = defaultdict(lambda: 1)
    # Hacemos la lectura del archivo línea a línea
    with open(file_path, 'r') as file:
        for line in file:
            json_value = json.loads(line)
            date = datetime.strptime(json_value["date"][:10], "%Y-%m-%d").date()
            user = json_value.get("user").get("username")
            data_id = json_value.get("id")
            data = {"user": user, "id": data_id}

            with open(f"{file_path[0:-5]}/{date}", "a") as fwrite:
                fwrite.write(json.dumps(data) + "\n")             
            # Contamos el número de líneas por día
            file_lines[date] += 1
    # Obtenemos el top 10 de días con más tweets
    top_10_days = sorted(file_lines, key=file_lines.get, reverse=True)[:10]
    # Utilizamos list comprehension para generar la lista de resultados
    result_list = [
        (
            date,
            pd.read_json(f'{file_path[0:-5]}/{date}', orient='records', lines=True)
            .groupby("user")
            .count()
            .sort_values("id", ascending=False)
            .iloc[0]
            .name
        )
        for date in top_10_days
    ]
    # Limpieza de datos
    directory_path = file_path[0:-5]
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

    return result_list