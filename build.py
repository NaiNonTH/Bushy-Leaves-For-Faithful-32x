import os
import shutil

from string import Template

shutil.rmtree("./dist", ignore_errors=True)
os.makedirs("./dist")

shutil.copytree("./templates/models", "./dist/assets/minecraft/models/template")
shutil.copytree("./templates/textures/minecraft", "./dist/assets/minecraft/textures/block")
shutil.copytree("./templates/meta", "./dist", dirs_exist_ok=True)

tinted_leaves = [
    "minecraft:oak_leaves",
    "minecraft:spruce_leaves",
    "minecraft:birch_leaves",
    "minecraft:jungle_leaves",
    "minecraft:acacia_leaves",
    "minecraft:dark_oak_leaves",
    "minecraft:mangrove_leaves",
]

non_tinted_leaves = [
    "minecraft:azalea_leaves",
    "minecraft:flowering_azalea_leaves",
    "minecraft:cherry_leaves",
    "minecraft:pale_oak_leaves"
]

with open("./templates/block.json") as reader:
    leaves_templ = Template(reader.read())

with open("./templates/blockstate.json") as reader:
    leaves_blockstate_templ = Template(reader.read())

for leaf in tinted_leaves:
    namespace = leaf[:leaf.find(":")]
    leaf_name = leaf[leaf.find(":") + 1:]

    leaf_path = f"./dist/assets/{namespace}"
    if not os.path.exists(os.path.join(leaf_path, "models/block")):
        os.makedirs(os.path.join(leaf_path, "models/block"))

    if not os.path.exists(os.path.join(leaf_path, "blockstates")):
        os.makedirs(os.path.join(leaf_path, "blockstates"))

    with open(os.path.join(leaf_path, f"models/block/bushy_{leaf_name}.json"), "w") as writer:
        to_write = leaves_templ.substitute(name=f"{namespace}:block/{leaf_name}_bushy", parent="leaves_bushy")
        writer.write(to_write)
    
    with open(os.path.join(leaf_path, f"models/block/bushy_{leaf_name}_alt.json"), "w") as writer:
        to_write = leaves_templ.substitute(name=f"{namespace}:block/{leaf_name}_bushy", parent="leaves_bushy_alt")
        writer.write(to_write)

    with open(os.path.join(leaf_path, f"blockstates/{leaf_name}.json"), "w") as writer:
        to_write = leaves_blockstate_templ.substitute(name=leaf_name, name_alt=f"{leaf_name}_alt")
        writer.write(to_write)

for leaf in non_tinted_leaves:
    namespace = leaf[:leaf.find(":")]
    leaf_name = leaf[leaf.find(":") + 1:]

    leaf_path = f"./dist/assets/{namespace}"
    if not os.path.exists(os.path.join(leaf_path, "models/block")):
        os.makedirs(os.path.join(leaf_path, "models/block"))

    if not os.path.exists(os.path.join(leaf_path, "blockstates")):
        os.makedirs(os.path.join(leaf_path, "blockstates"))
    
    with open(os.path.join(leaf_path, f"models/block/bushy_{leaf_name}.json"), "w") as writer:
        to_write = leaves_templ.substitute(name=f"{namespace}:block/{leaf_name}_bushy", parent="leaves_bushy")
        writer.write(to_write)
    
    with open(os.path.join(leaf_path, f"models/block/bushy_{leaf_name}_alt.json"), "w") as writer:
        to_write = leaves_templ.substitute(name=f"{namespace}:block/{leaf_name}_bushy", parent="leaves_bushy_alt")
        writer.write(to_write)

    with open(os.path.join(leaf_path, f"blockstates/{leaf_name}.json"), "w") as writer:
        to_write = leaves_blockstate_templ.substitute(name=leaf_name, name_alt=f"{leaf_name}_alt")
        writer.write(to_write)