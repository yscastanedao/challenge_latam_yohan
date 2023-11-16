from typing import List, Tuple
import json
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Diccionario para almacenar el conteo de usuarios mencionados
    mentioned_users_counter = Counter()

    # Lectura línea a línea
    with open(file_path, 'r') as file:
        for line in file:
            json_value = json.loads(line)
            mentioned_users = json_value.get("mentionedUsers")
            if mentioned_users:
                mentioned_users_counter.update(i["username"] for i in mentioned_users)

    # Obtener los 10 usuarios más mencionados
    top_10_mentioned_users = mentioned_users_counter.most_common(10)

    # Convertir el resultado a una lista de tuplas
    mentioned_users_list = [(user, count) for user, count in top_10_mentioned_users]

    return mentioned_users_list