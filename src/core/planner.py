from langchain.messages import HumanMessage, AIMessage
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException
from src.chains.itinerary import generate_prompt

logger = get_logger(__name__)

class TravelPlanner:
    """
    TravelPlanner manages user travel preferences and generates
    a personalized travel itinerary using an LLM chain.

    This class keeps track of:
    - User inputs (city and interests)
    - Conversation history using LangChain message objects
    - Generated itinerary

    Workflow:
    ---------
    1. User sets a city
    2. User provides interests
    3. The planner generates an itinerary using an LLM prompt
    """

    def __init__(self):
        """
        Initialize the TravelPlanner instance.

        Attributes
        ----------
        message : list
            Stores conversation history using LangChain messages.

        city : str
            Destination city provided by the user.

        interests : list
            List of user interests (e.g., food, museums, nightlife).

        itinerary : str
            Generated travel itinerary.
        """

        self.message = []
        self.city = ""
        self.interests = []
        self.itinerary = ""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self, city: str):
        """
        Set the destination city for the travel plan.

        Parameters
        ----------
        city : str
            Name of the city for which the itinerary should be generated.

        Raises
        ------
        CustomException
            If setting the city fails.
        """

        try:
            self.city = city
            self.message.append(HumanMessage(content=city))

            logger.info("City successfully set")

        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city", e)

    def set_interests(self, interests: str):
        """
        Set the user's interests for the travel plan.

        Parameters
        ----------
        interests : str
            Comma-separated interests (e.g., "food, museums, nightlife").

        Raises
        ------
        CustomException
            If setting interests fails.
        """

        try:
            self.interests = [i.strip() for i in interests.split(",")]
            self.message.append(HumanMessage(content=interests))

            logger.info("Interests successfully set")

        except Exception as e:
            logger.error(f"Error while setting interests: {e}")
            raise CustomException("Failed to set interests", e)

    def create_itinerary(self):
        """
        Generate a travel itinerary based on the selected city and interests.

        Returns
        -------
        str
            Generated travel itinerary.

        Raises
        ------
        CustomException
            If itinerary generation fails.
        """

        try:
            logger.info(
                f"Generating itinerary for {self.city} with interests: {self.interests}"
            )

            itinerary = generate_prompt(self.city, self.interests)

            self.itinerary = itinerary
            self.message.append(AIMessage(content=itinerary))

            logger.info("Itinerary generated successfully")

            return itinerary

        except Exception as e:
            logger.error(f"Error while creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)