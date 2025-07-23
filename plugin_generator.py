from jinja2 import Environment, FileSystemLoader
import os

template_file = 'animation_template.motn.j2'

DIRECTION_VECTORS = {
    "left": "-1000 0",
    "right": "1000 0",
    "top": "0 1000",
    "bottom": "0 -1000",
    "none": "0 0"
}

def generate_plugin(name, in_direction, out_direction, duration, motion_blur, pan):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    output = template.render(
        duration=duration,
        in_direction=in_direction,
        out_direction=out_direction,
        in_vector=DIRECTION_VECTORS.get(in_direction, "0 0"),
        out_vector=DIRECTION_VECTORS.get(out_direction, "0 0"),
        motion_blur=motion_blur,
        pan=pan
    )

    folder_name = f"{name}.localized"
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, f"{name}.motn"), 'w') as f:
        f.write(output)

    with open(os.path.join(folder_name, "Template Info.plist"), 'w') as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>uuid</key>
    <string>{name}</string>
</dict>
</plist>
""")

    print(f"✅ Plugin '{name}' generated at: {folder_name}/")

# Example run
if __name__ == "__main__":
    generate_plugin(
        name="FlyInPlugin",
        in_direction="left",
        out_direction="top",
        duration="4s",
        motion_blur="medium",
        pan=True
    )