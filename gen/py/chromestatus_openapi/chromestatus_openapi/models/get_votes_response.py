from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.vote import Vote
from chromestatus_openapi import util

from chromestatus_openapi.models.vote import Vote  # noqa: E501

class GetVotesResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, votes=None):  # noqa: E501
        """GetVotesResponse - a model defined in OpenAPI

        :param votes: The votes of this GetVotesResponse.  # noqa: E501
        :type votes: List[Vote]
        """
        self.openapi_types = {
            'votes': List[Vote]
        }

        self.attribute_map = {
            'votes': 'votes'
        }

        self._votes = votes

    @classmethod
    def from_dict(cls, dikt) -> 'GetVotesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetVotesResponse of this GetVotesResponse.  # noqa: E501
        :rtype: GetVotesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def votes(self) -> List[Vote]:
        """Gets the votes of this GetVotesResponse.


        :return: The votes of this GetVotesResponse.
        :rtype: List[Vote]
        """
        return self._votes

    @votes.setter
    def votes(self, votes: List[Vote]):
        """Sets the votes of this GetVotesResponse.


        :param votes: The votes of this GetVotesResponse.
        :type votes: List[Vote]
        """

        self._votes = votes