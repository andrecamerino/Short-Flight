from jinja2 import Environment, FileSystemLoader
import os

template_file = 'effect_template.moef.j2'

DIRECTION_VECTORS = {
    "left": "-1000 0",
    "right": "1000 0",
    "top": "0 1000",
    "bottom": "0 -1000",
    "none": "0 0"
}

def generate_plugin(name, in_direction, out_direction, duration, pan):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    output = template.render(
        name=name,
        duration=duration,
        in_direction=in_direction,
        out_direction=out_direction,
        in_vector=DIRECTION_VECTORS.get(in_direction, "0 0"),
        out_vector=DIRECTION_VECTORS.get(out_direction, "0 0"),
        pan=pan
    )

    output_base = os.path.expanduser("~/Movies/Motion Templates.localized/Effects.localized")
    folder_name = f"{name}.localized"
    plugin_path = os.path.join(output_base, folder_name)
    os.makedirs(plugin_path, exist_ok=True)

    with open(os.path.join(plugin_path, f"{name}.moef"), 'w') as f:
        f.write(output)

    with open(os.path.join(plugin_path, "Template Info.plist"), 'w') as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>uuid</key>
    <string>{name}</string>
</dict>
</plist>
""")

    print(f"✅ Effect plugin '{name}' generated at: {plugin_path}")

if __name__ == "__main__":
    generate_plugin(
        name="Short-Flight",
        in_direction="left",
        out_direction="right",
        duration="4",
        pan=True
    )