from typing import List, Tuple
import emoji
import json
from collections import Counter

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Diccionario para almacenar el conteo de emojis
    emoji_counter = Counter()
    # Lectura línea a línea
    with open(file_path, "r") as file:
        for line in file:
            json_value = json.loads(line)
            content = json_value.get("content")
            # Extraer emojis y actualizar el contador
            emojis = [value.chars for value in emoji.analyze(content)]
            emoji_counter.update(emojis)
    # Obtener los 10 emojis más frecuentes
    top_10_emojis = emoji_counter.most_common(10)
    # Convertir el resultado a una lista de tuplas
    emoji_list = [(emoji, count) for emoji, count in top_10_emojis]
    return emoji_list