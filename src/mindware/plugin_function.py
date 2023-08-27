class PluginFunction:
    def __init__(self, url, name, path, method, description, requires_auth, response_type):
        self.url = url
        self.name = name
        self.path = path
        self.method = method
        self.description = description
        self.requires_auth = requires_auth
        self.response_type = response_type
