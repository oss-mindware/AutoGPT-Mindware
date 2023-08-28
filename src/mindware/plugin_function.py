class PluginFunction:
    def __init__(self, url, name, path, method, description, params=None, auth_info=None, requires_auth=False, response_type=None):
        self.url = url
        self.name = name
        self.path = path
        self.params = params
        self.method = method
        self.auth_info = auth_info
        self.description = description
        self.requires_auth = requires_auth
        self.response_type = response_type
