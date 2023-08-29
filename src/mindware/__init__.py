import os
from typing import Any, Dict, List, Optional, Tuple, TypedDict, TypeVar

from auto_gpt_plugin_template import AutoGPTPluginTemplate

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class MindwarePlugin(AutoGPTPluginTemplate):
    """
    Mindware plugin for AutoGPT.
    """

    def __init__(self):
        super().__init__()
        self._name = "AutoGPT-Mindware-Plugin"
        self._version = "0.0.3"
        self._description = "This plugin allows AutoGPT to access Mindware - the “App Store” for AI plugins."
        self.yt_api_key = os.environ.get("MINDWARE_API_KEY")
        if self.yt_api_key is None:
            print(
                "WARNING: The Mindware API key is not set, therefore Mindware commands are disabled. Please set the MINDWARE_API_KEY environment variable."
            )
        self.workspace_path = "autogpt\\auto_gpt_workspace"

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        """This method is called just after the generate_prompt is called,
            but actually before the prompt is generated.

        Args:
            prompt (PromptGenerator): The prompt generator.

        Returns:
            PromptGenerator: The prompt generator.
        """

        from .mindware import (
            get_enabled_plugin_functions,
            create_request_functions,
        )

        plugin_functions = get_enabled_plugin_functions()

        for plugin_function in plugin_functions:
            if plugin_function.method == 'get':
                query = {}
            if plugin_function.method == 'post':
                query = {"query": "Query to send to Mindware."}
            prompt.add_command(
                plugin_function.name,
                plugin_function.description,
                query,
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

    def can_handle_text_embedding(
        self, text: str
    ) -> bool:
        return False

    def handle_text_embedding(
        self, text: str
    ) -> list:
        pass

    def can_handle_user_input(self, user_input: str) -> bool:
        return False

    def user_input(self, user_input: str) -> str:
        return user_input

    def can_handle_report(self) -> bool:
        return False

    def report(self, message: str) -> None:
        pass
