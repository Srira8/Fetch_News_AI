import os
import json
from datetime import datetime

def save_data(data, prefix="news", directory="data"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{prefix}_{timestamp}.json"
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    return filepath
