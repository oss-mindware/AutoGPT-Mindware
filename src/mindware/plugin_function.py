class PluginFunction:
    def __init__(
        self,
        url,
        name,
        path,
        params=None,
        method=None,
        description=None,
        requires_auth=False,
        auth_info=None,
        response_type=None,
    ):
        self.url = url
        self.name = name
        self.path = path
        self.params = params
        self.method = method
        self.auth_info = auth_info
        self.description = description
        self.requires_auth = requires_auth
        self.response_type = response_type