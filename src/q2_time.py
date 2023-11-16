from collections import Counter
from typing import List, Tuple
import emoji
import json

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo y extraer el campo "content" directamente usando list comprehension
    with open(file_path, 'r') as file_data:
        data = [json.loads(line)["content"] for line in file_data]
    # Concatenar todos los emojis en una lista
    emoji_values = [value.chars for text in data for value in emoji.analyze(text)]
    # Usar Counter para contar la frecuencia de cada emoji
    emoji_counter = Counter(emoji_values)
    # Obtener los 10 emojis más frecuentes
    top_10_emojis = emoji_counter.most_common(10)
    # Convertir el resultado a una lista de tuplas
    emoji_list = [(emoji, count) for emoji, count in top_10_emojis]
    return emoji_list