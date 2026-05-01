import yaml
import os

MANIFEST_PATH = "/opt/app/etc/default/model_manifest.yaml"

def load_config():
    if not os.path.exists(MANIFEST_PATH):
        raise FileNotFoundError(f"Config not found at {MANIFEST_PATH}")

    with open(MANIFEST_PATH, "r") as f:
        config = yaml.safe_load(f)

    profile = os.getenv("PROFILE", "default")

    if profile not in config["profiles"]:
        raise ValueError(f"Profile '{profile}' not found")

    return config["profiles"][profile]