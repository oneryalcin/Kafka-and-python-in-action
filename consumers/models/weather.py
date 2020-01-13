"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is incomplete - skipping")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        if "com.udacity.kafka.producer.weather.v1" in message.topic():
            
            v = message.value()
            
            self.temperature = v['temperature']
            self.status = v['status']
            
            logger.debug("Weather message received, temp: %s , status: %s", self.temperature, self.status)
            
        else:
            logger.warning("Discarding message as it is not weather data")
        
