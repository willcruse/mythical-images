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

def update_yaml(data: Dict[str, Any]) -> Dict[str, Any]:
    new_dict = {}
    for key, entry in data.items():
        file_name = entry.get("file-path")
        if file_name is not None:
            file_check = Path(file_name)
            print(file_check)
            if file_check.exists():
                new_dict[key] = entry
    return new_dict

if __name__=="__main__":
    yaml_base_path = Path("./clean-data-big/")
    data = yaml.load((yaml_base_path / Path("image-data.yaml")).open())
    print_unique_file_ext(data)
    new_data = update_yaml(data)

    file_path = str(yaml_base_path / Path("new-image-data.yaml"))
    with open(file_path, "w") as file:
        yaml.dump(new_data, file)
