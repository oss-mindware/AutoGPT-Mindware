import os
import unittest
from . import MindwarePlugin
from unittest.mock import Mock, patch
from mindware import get_enabled_plugin_functions, create_request_functions, headers


class TestMindwarePlugin(unittest.TestCase):
    def setUp(self):
        os.environ["MINDWARE_API_KEY"] = "api_key"
        self.plugin = MindwarePlugin()

    def tearDown(self):
        os.environ.pop("MINDWARE_API_KEY", None)

    @patch("requests.get")
    def test_get_enabled_plugin_functions_successful(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "functions": [
                    {"url": "https://example.com", "path": "/path", "method": "get"}
                ]
            }
        ]
        mock_get.return_value = mock_response

        plugin_functions = get_enabled_plugin_functions()
        self.assertEqual(len(plugin_functions), 1)
        self.assertEqual(plugin_functions[0].url, "https://example.com")
        self.assertEqual(plugin_functions[0].path, "/path")
        self.assertEqual(plugin_functions[0].method, "get")

    @patch("requests.get")
    def test_get_enabled_plugin_functions_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        plugin_functions = get_enabled_plugin_functions()
        self.assertEqual(len(plugin_functions), 0)

    def test_create_request_functions_get(self):
        function_info = Mock(url="https://example.com", path="/path", method="get")
        send_request = create_request_functions(function_info)

        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {"response_key": "response_value"}
            mock_get.return_value = mock_response

            response = send_request()

            mock_get.assert_called_once_with(
                "https://example.com/path", headers=headers
            )
            self.assertEqual(response, {"response_key": "response_value"})

    def test_create_request_functions_post(self):
        function_info = Mock(url="https://example.com", path="/path", method="post")
        send_request = create_request_functions(function_info)

        with patch("requests.post") as mock_post:
            mock_response = Mock()
            mock_response.json.return_value = {"response_key": "response_value"}
            mock_post.return_value = mock_response

            response = send_request(query="test_query")

            mock_post.assert_called_once_with(
                "https://example.com/path",
                headers=headers,
                json={"query": "test_query"},
            )
            self.assertEqual(response, {"response_key": "response_value"})


if __name__ == "__main__":
    unittest.main()
