from pathlib import Path
import yaml


data_set = yaml.load(Path("./image-data.yaml").read_text(), Loader=yaml.Loader)

all_image_paths = set([
    Path(data["file-name"]).stem for data in filter(lambda x: x["beast"] == "pegasus", data_set.values())
])

print(len(all_image_paths))

this_dir = Path(".")

count = -2
all_images = set()
for file_name in this_dir.iterdir():
    all_images.add(str(file_name.stem))
    if str(file_name.stem) not in all_image_paths:
        count += 1
        file_name.unlink()
        # print(file_name)

all_images.remove("image-data")
all_images.remove("filter")

print(len(all_image_paths.union(all_images)))

print(all_image_paths.difference(all_images))

print(count)
print(len(all_images) - count)