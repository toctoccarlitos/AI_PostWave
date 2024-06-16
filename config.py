from os import getenv, path
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(Path('.') / '.env')

# Environment variables
PATH_APP_DATA = getenv("PATH_APP_DATA")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = getenv("CLAUDE_API_KEY")
WP_API_URL = getenv("WP_API_URL")
TOPIC = getenv("TOPIC")
REGION = getenv("REGION")
TIMEFRAME = getenv("TIMEFRAME")
NUM_TOPICS = getenv("NUM_TOPICS")
LANGUAGE = getenv("LANGUAGE")

# AI Models
MODEL_CONFIG = {
    "GPT-4o": {"owner": "OpenAI", "model": "gpt-4o"},
    "GPT 4 Turbo": {"owner": "OpenAI", "model": "gpt-4-turbo"},
    "GPT 4": {"owner": "OpenAI", "model": "gpt-4"},
    "GPT 3.5 Turbo": {"owner": "OpenAI", "model": "gpt-3.5-turbo"},
    "Claude 3 Opus": {"owner": "Anthropic", "model": "claude-3-opus-20240229"},
    "Claude 3 Sonnet": {"owner": "Anthropic", "model": "claude-3-sonnet-20240229"},
    "Claude 3 Haiku": {"owner": "Anthropic", "model": "claude-3-haiku-20240307"}
}

# Model names for different stages
MODEL_TREND_SEARCH=MODEL_CONFIG["GPT-4o"]
MODEL_CREATE_POST=MODEL_CONFIG["GPT 3.5 Turbo"]
MODEL_CREATE_IMAGES=MODEL_CONFIG["GPT-4o"]

# Prompts for different stages
PROMPT_TREND_SEARCH = (
    "Conduct a comprehensive internet search to identify the main trends and hot topics related to {topic} in {region} over the last {timeframe}. "
    "Use trend analysis tools and social media to obtain accurate and up-to-date information. From the collected data, identify the {num_topics} most relevant subtopics and generate a response strictly in the following JSON format without any additional comments or explanations: "
    "The JSON array should contain objects with the following fields: title (string), description (string), and hashtags (array of strings). Each object should represent a subtopic with its corresponding hashtags."
    "Ensure that the subtopics are diverse and cover different aspects of {topic}, such as emerging trends, challenges, innovative solutions, and practical tips. "
    "Also, consider any recent local events, holidays, or news that may be influencing the trends in {region}. Generate the response in the language specified in {language}. Remember, search on the internet before responding."
).format(
    topic=TOPIC,
    region=REGION,
    timeframe=TIMEFRAME,
    num_topics=NUM_TOPICS,
    language=LANGUAGE
)

PROMPT_CREATE_POST="Write a blog post about the benefits of natural skincare."
PROMPT_CREATE_IMAGES="A beautiful illustration of natural skincare products."

# Paths
PATH_LOG = path.join(PATH_APP_DATA, "logs")
PATH_TMP = path.join(PATH_APP_DATA, "tmp")

# others
FILE_ENCODING="utf-8"