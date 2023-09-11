import unittest
from src.mindware import MindwarePlugin
from unittest.mock import Mock, patch, ANY
from typing import TypeVar

PromptGenerator = TypeVar("PromptGenerator")

class TestMindwarePlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = MindwarePlugin()

    def test_encrypt_credentials(self):
        credential = "secret_password"
        encrypted = self.plugin.encrypt_credentials(credential)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    @patch('os.environ.get')
    def test_generate_credentials_with_authentication(self, mock_os_environ_get):
        mock_os_environ_get.side_effect = lambda key: {
            'TOKEN': 'token_value',
            'USERNAME': 'username_value',
            'PASSWORD': 'password_value'
        }.get(key)

        plugin_function = Mock()
        plugin_function.requires_auth = True
        plugin_function.auth_info = {
            'token_field': 'TOKEN',
            'username_field': 'USERNAME',
            'password_field': 'PASSWORD'
        }

        credentials = self.plugin.generate_credentials(plugin_function)

        self.assertEqual(len(credentials), 3)
        self.assertIsInstance(credentials['token_field'], str)
        self.assertIsInstance(credentials['username_field'], str)
        self.assertIsInstance(credentials['password_field'], str)

    def test_generate_credentials_without_authentication(self):
        plugin_function = Mock()
        plugin_function.requires_auth = False

        credentials = self.plugin.generate_credentials(plugin_function)

        self.assertEqual(len(credentials), 0)

    @patch('os.environ.get')
    def test_generate_credentials_missing_environment_variables(self, mock_os_environ_get):
        mock_os_environ_get.return_value = None

        plugin_function = Mock()
        plugin_function.requires_auth = True
        plugin_function.auth_info = {
            'token_field': 'TOKEN',
            'username_field': 'USERNAME',
            'password_field': 'PASSWORD'
        }

        credentials = self.plugin.generate_credentials(plugin_function)

        self.assertEqual(len(credentials), 0)

    @patch('os.environ.get')
    @patch('requests.post')
    @patch('requests.get')
    def test_post_prompt_enabled_plugin_functions(self, mock_requests_get, mock_requests_post, mock_os_environ_get):
        mock_os_environ_get.side_effect = lambda key: {
            'MINDWARE_API_KEY': 'mindware_key',
        }.get(key)
        mock_plugins_response = Mock()
        mock_plugins_response.status_code = 200
        mock_plugins_response.json.return_value = [
            {
                "functions": [
                    {
                        "url": "https://example.com",
                        "name": "search-youtube",
                        "path": "/youtube/search",
                        "method": "post",
                        "params": {
                            "query": "<query>"
                        },
                        "description": "Function to search youtube",
                        "requires_auth": False,
                        "response_type": "object"
                    },
                ]
            }
        ]
        mock_requests_get.return_value = mock_plugins_response

        mock_function_response = Mock()
        mock_function_response.json.return_value = { "property": "value" }
        mock_requests_post.return_value = mock_function_response

        prompt_generator = Mock(spec=PromptGenerator)
        prompt_generator.add_command = Mock()
        
        self.plugin.post_prompt(prompt_generator)

        prompt_generator.add_command.assert_called_once()
        prompt_generator.add_command.assert_called_with(
            'search-youtube', 'Function to search youtube', {'query': '<query>'}, ANY
        )
        args = prompt_generator.add_command.call_args
        response = args[0][3]()
        self.assertEqual(response, { "property": "value" })


    @patch('os.environ.get')
    @patch('requests.get')
    def test_post_prompt_empty_response(self, mock_requests_get, mock_os_environ_get):
        mock_os_environ_get.side_effect = lambda key: {
            'MINDWARE_API_KEY': 'mindware_key',
        }.get(key)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_requests_get.return_value = mock_response

        prompt_generator = Mock(spec=PromptGenerator)
        prompt_generator.add_command = Mock()

        self.plugin.post_prompt(prompt_generator)

        prompt_generator.add_command.assert_not_called()

if __name__ == '__main__':
    unittest.main()
