import json
from datetime import datetime
import os
import config
import json
from general.initialize_app import initialize_app_data
from enums.Stage import Stage
from managers.manager_ia import ManagerIA
from general.logger_config import get_logger

logger = get_logger()

def test_trend_search():
    try:
        # Initialize the application data structure
        initialize_app_data()

        manager = ManagerIA(stage=Stage.TREND_SEARCH)
        if manager.llm:
            logger.info(f"Successfully initialized the LLM for {Stage.TREND_SEARCH.value}: {config.MODEL_TREND_SEARCH}")
            response = manager.generate_response()

            # Create a timestamped filename
            timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
            filename = os.path.join(config.PATH_TMP, f"{timestamp}__response_trend.json")

            # Parse the response as JSON
            try:
                response_json = json.loads(response)
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing JSON response: {e}")
                response_json = {"error": "Failed to parse response as JSON"}

            # Save the response to a JSON file
            with open(filename, 'w', encoding=config.FILE_ENCODING) as file:
                json.dump(response_json, file, indent=2, ensure_ascii=False)

            logger.info(f"Response saved to file: {filename}")
        else:
            logger.error(f"Failed to initialize the LLM for {Stage.TREND_SEARCH.value}.")
    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    test_trend_search()
