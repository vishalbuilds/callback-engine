import boto3
from logger import Logger

LOGGER = Logger(__name__)


class ConnectUtils:
    def __init__(self, region):
        self.connect_client = boto3.client("connect", region)

    def start_outbound_voice_contact(
        self,
        DestinationPhoneNumber,
        ContactFlowId,
        InstanceId,
        SourcePhoneNumber=None,
        QueueId=None,
    ):
        try:
            if not (SourcePhoneNumber and QueueId):
                LOGGER.error("SourcePhoneNumber or QueueId are required")
                raise ValueError("SourcePhoneNumber or QueueId are required")

            response = self.connect_client.start_outbound_voice_contact(
                name="Callback",
                DestinationPhoneNumber=DestinationPhoneNumber,
                ContactFlowId=ContactFlowId,
                InstanceId=InstanceId,
                SourcePhoneNumber=SourcePhoneNumber if SourcePhoneNumber else None,
                QueueId=QueueId if QueueId else None,
            )
            LOGGER.add_tempdata("Callback_contactId", response.get("ContactId"))
            LOGGER.info("Outbound voice contact started successfully")
            return response

        except Exception as e:
            LOGGER.add_tempdata("error", str(e))
            LOGGER.error(f"Failed to start outbound voice contact: {str(e)}")
            raise
