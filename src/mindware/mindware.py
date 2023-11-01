import os
import requests
from .plugin_function import PluginFunction

api_key = os.environ.get("MINDWARE_API_KEY")
if api_key is None:
    raise ValueError("MINDWARE_API_KEY environment variable is not set")
headers = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}


def get_enabled_plugin_functions() -> list[PluginFunction]:
    url = "https://gateway.mindware.xyz/plugins"

    response = requests.get(url, headers=headers, timeout=30)

    if response.status_code == 200:
        plugins = response.json()
        functions = []

        for plugin in plugins:
            plugin_functions = plugin.get("functions", [])

            if plugin_functions is not None:
                for plugin_function in plugin_functions:
                    function_object = PluginFunction(**plugin_function)
                    functions.append(function_object)

        return functions
    else:
        print("Failed to fetch plugin functions.")
        return []


def create_request_functions(function_info):
    def send_request(**kwargs):
        kwargs = kwargs or {}
        full_url = function_info.url + function_info.path

        if function_info.method == "get":
            response = requests.get(full_url, headers=headers, params=kwargs)
        elif function_info.method == "post":
            response = requests.post(full_url, headers=headers, json=kwargs)
        else:
            print("Unsupported HTTP method:", function_info.method)
            return None

        return response.json()

    return send_request
