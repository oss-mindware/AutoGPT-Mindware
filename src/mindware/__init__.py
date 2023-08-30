import os
from typing import Any, Dict, List, Optional, Tuple, TypedDict, TypeVar

from auto_gpt_plugin_template import AutoGPTPluginTemplate

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class MindwarePlugin(AutoGPTPluginTemplate):
    """
    This is a plugin for Auto-GPT which grants access to the Mindware plugin marketplace.
    """

    def __init__(self):
        super().__init__()
        self._name = "AutoGPT-Mindware-Plugin"
        self._version = "0.0.3"
        self._description = "This is a plugin for Auto-GPT which grants access to the Mindware plugin marketplace."
        self.workspace_path = "autogpt\\auto_gpt_workspace"

    def generate_credentials(self, plugin_function) -> Dict[str, str]:
        """
        Generates the param_object based on the plugin_function.

        Args:
            plugin_function: The plugin function for which to generate the param_object.

        Returns:
            Dict[str, str]: The dynamically generated param_object.
        """
        credentials = {}

        if plugin_function.requires_auth is True:
            if "token_field" in plugin_function.auth_info:
                credentials["token_field"] = os.environ.get(
                    plugin_function.auth_info["token_field"]
                )
            if "username_field" in plugin_function.auth_info:
                credentials["username_field"] = os.environ.get(
                    plugin_function.auth_info["username_field"]
                )
            if "password_field" in plugin_function.auth_info:
                credentials["password_field"] = os.environ.get(
                    plugin_function.auth_info["password_field"]
                )

        return credentials

    def generate_parameters(self, plugin_function) -> Dict[str, str]:
        """
        Generates the param_object based on the plugin_function.

        Args:
            plugin_function: The plugin function for which to generate the param_object.

        Returns:
            Dict[str, str]: The dynamically generated param_object.
        """
        params = {}

        if plugin_function.params is not None:
            params = plugin_function.params
            return params

        return params

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        """This method is called just after the generate_prompt is called,
            but actually before the prompt is generated.

        Args:
            prompt (PromptGenerator): The prompt generator.

        Returns:
            PromptGenerator: The prompt generator.
        """

        from .mindware import (
            create_request_functions,
            get_enabled_plugin_functions,
        )

        plugin_functions = get_enabled_plugin_functions()

        for plugin_function in plugin_functions:
            params = self.generate_parameters(plugin_function)
            credentials = self.generate_credentials(plugin_function)

            prompt.add_command(
                plugin_function.name,
                plugin_function.description,
                params,
                create_request_functions(plugin_function),
            )

        return prompt

    def can_handle_post_prompt(self) -> bool:
        return True

    def can_handle_on_response(self) -> bool:
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        pass

    def can_handle_on_planning(self) -> bool:
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        pass

    def can_handle_post_planning(self) -> bool:
        return False

    def post_planning(self, response: str) -> str:
        pass

    def can_handle_pre_instruction(self) -> bool:
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        pass

    def can_handle_on_instruction(self) -> bool:
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        pass

    def can_handle_post_instruction(self) -> bool:
        return False

    def post_instruction(self, response: str) -> str:
        pass

    def can_handle_pre_command(self) -> bool:
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        pass

    def can_handle_post_command(self) -> bool:
        return False

    def post_command(self, command_name: str, response: str) -> str:
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        pass

    def can_handle_text_embedding(self, text: str) -> bool:
        return False

    def handle_text_embedding(self, text: str) -> list:
        pass

    def can_handle_user_input(self, user_input: str) -> bool:
        return False

    def user_input(self, user_input: str) -> str:
        return user_input

    def can_handle_report(self) -> bool:
        return False

    def report(self, message: str) -> None:
        pass
