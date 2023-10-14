import os
import shutil
import sys

if len(sys.argv) != 3:
    print("Usage: python install.py <autogpt_directory_path> <mindware_api_key>")
    sys.exit(1)

autogpt_directory_path = sys.argv[1]
mindware_api_key = sys.argv[2]

if os.path.isdir(os.path.join(autogpt_directory_path, "plugins")) and os.path.isfile(os.path.join(autogpt_directory_path, ".env")):
    destination_plugins_mindware_dir = os.path.join(autogpt_directory_path, "plugins", "mindware")

    if os.path.exists(destination_plugins_mindware_dir):
        shutil.rmtree(destination_plugins_mindware_dir)

    os.makedirs(destination_plugins_mindware_dir)

    for item in os.listdir("./src/mindware"):
        source = os.path.join("./src/mindware", item)
        if os.path.isdir(source):
            shutil.copytree(source, os.path.join(destination_plugins_mindware_dir, item))
        else:
            shutil.copy(source, destination_plugins_mindware_dir)

    print(f"Plugin has been copied to {destination_plugins_mindware_dir}")

    env_file_path = os.path.join(autogpt_directory_path, ".env")
    config_file_path = os.path.join(autogpt_directory_path, "plugins_config.yaml")

    with open(env_file_path, "r") as env_file:
        env_content = env_file.read()

    config_content = ""
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            config_content = config_file.read()

    with open(config_file_path, "r") as config_file:
        config_content = config_file.read()

    if f"MINDWARE_API_KEY=" not in env_content:
        with open(os.path.join(autogpt_directory_path, ".env"), "a") as env_file:
            env_file.write(f"\nMINDWARE_API_KEY={mindware_api_key}\n")
        print(f"API key has been added to {env_file_path}")

    if not os.path.exists(config_file_path) or "\nmindware:\n  config: {}\n  enabled: true\n" not in config_content:
        with open(config_file_path, "a") as config_file:
            config_file.write("\nmindware:\n  config: {}\n  enabled: true\n")
        print(f"Configuration has been added to {config_file_path}")

    print("Plugin installed successfully")
else:
    print("Not a valid Auto-GPT directory")
    sys.exit(1)
