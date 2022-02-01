from pathlib import Path
from typing import Dict, Any

import yaml

def filter_file_names(data: Dict[str, Any]):
    file_names = []
    for entry in data.values():
        file_name = entry.get("file-name")
        if file_name is not None:
            file_names.append(file_name)
    
    return file_names

def print_unique_file_ext(data):
    file_names = filter_file_names(data)
    file_extensions = set()
    for file_name in file_names:
        file_extensions.add(Path(file_name).suffix)
    print(list(file_extensions))

if __name__=="__main__":
    data = yaml.load(Path("./clean-data-big/image-data.yaml").open())
    print_unique_file_ext(data)