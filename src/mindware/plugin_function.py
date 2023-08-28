class PluginFunction:
    def __init__(self, url, name, path, params, method, auth_info, description, requires_auth, response_type):
        self.url = url
        self.name = name
        self.path = path
        self.params = params
        self.method = method
        self.auth_info = auth_info
        self.description = description
        self.requires_auth = requires_auth
        self.response_type = response_type
