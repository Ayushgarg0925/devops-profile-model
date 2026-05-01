import yaml

with open("etc/default/model_manifest.yaml") as f:
    data = yaml.safe_load(f)

print("Available Profiles:")
for profile in data["profiles"]:
    print("-", profile)