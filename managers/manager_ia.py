import re
import config

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import config
from enums.Stage import Stage
from general.logger_config import get_logger

logger = get_logger()

class ManagerIA:

    def __init__(self, stage: Stage):
        """
        Initializes the ManagerIA instance.

        Args:
            stage (Stage): The stage for which to initialize the ManagerIA instance.

        Raises:
            ValueError: If the provided stage is not an instance of Stage Enum.
        """
        try:
            if not isinstance(stage, Stage):
                raise ValueError(f"Invalid stage: {stage}. Must be an instance of Stage Enum.")
            self.stage = stage
            self.llm = self.initialize_llm()
        except Exception as e:
            logger.error(f"Error initializing ManagerIA: {e}")

    def get_model_info(self):
        """
        Retrieves the model information based on the current stage.

        Returns:
            dict: The model information dictionary if found, None otherwise.
        """
        try:
            model_info = ""
            if self.stage == Stage.TREND_SEARCH:
                model_info = config.MODEL_TREND_SEARCH
            elif self.stage == Stage.CREATE_POST:
                model_info = config.MODEL_CREATE_POST
            elif self.stage == Stage.CREATE_IMAGES:
                model_info = config.MODEL_CREATE_IMAGES
            else:
                logger.error(f"Stage {self.stage} is not recognized.")
                return None

            return model_info
        except Exception as e:
            logger.error(f"Error getting model info for stage {self.stage}: {e}")
            return None

    def initialize_llm(self):
        """
        Initializes the Language Learning Model (LLM) based on the model information.

        Returns:
            object: An instance of ChatOpenAI or ChatAnthropic, or None if initialization fails.
        """
        try:
            model_info = self.get_model_info()
            if not model_info:
                return None

            if model_info["owner"] == "OpenAI":
                logger.info(f"Initializing OpenAI model: {model_info['model']} for stage {self.stage}")
                return ChatOpenAI(openai_api_key=config.OPENAI_API_KEY, model=model_info["model"])
            elif model_info["owner"] == "Anthropic":
                logger.info(f"Initializing Anthropic model: {model_info['model']} for stage {self.stage}")
                return ChatAnthropic(anthropic_api_key=config.CLAUDE_API_KEY, model=model_info["model"])
            else:
                logger.error(f"Owner {model_info['owner']} is not recognized.")
                return None
        except Exception as e:
            logger.error(f"Error initializing LLM: {e}")
            return None

    def generate_response(self):
        """
        Generates a response from the LLM based on the current stage's prompt.

        Returns:
            str: The generated response from the LLM, or an error message if something goes wrong.
        """
        try:
            if self.stage == Stage.TREND_SEARCH:
                prompt = config.PROMPT_TREND_SEARCH
            elif self.stage == Stage.CREATE_POST:
                prompt = config.PROMPT_CREATE_POST
            elif self.stage == Stage.CREATE_IMAGES:
                prompt = config.PROMPT_CREATE_IMAGES
            else:
                logger.error(f"Stage {self.stage} is not recognized.")
                return "Invalid stage."

            logger.info(f"Calling LLM for stage {self.stage.value} with prompt loaded.")

            promptTemplate = ChatPromptTemplate.from_messages([("system", prompt)])
            chain = promptTemplate | self.llm | StrOutputParser()
            result = chain.invoke({})

             # Process the response to remove code block delimiters and extra newlines
            if result.startswith("```json"):
                result = result[7:]  # Remove the leading ```json
            if result.endswith("```"):
                result = result[:-3]  # Remove the trailing ```
            result = re.sub(r'\n{2,}', '\n', result).strip()

            response_length = len(result)
            logger.info(f"Response length: {response_length} characters")

            return result
        except Exception as e:
            logger.error(f"Error generating response for stage {self.stage}: {e}")
            return "An error occurred while generating the response."
