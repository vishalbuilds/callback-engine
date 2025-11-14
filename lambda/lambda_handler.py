import os
from aws_client_utils import ConnectUtils
from logger import Logger

LOGGER = Logger(__name__)

REGION = os.environ("REGION")

connect_client = ConnectUtils(REGION)


def lambda_handler(event, context):
    try:
        connect_client.start_outbound_voice_contact()
    except Exception as e:
        LOGGER.add_tempdata("error", str(e))
        LOGGER.error(f"Failed to process lambda handler: {str(e)}")
        raise
