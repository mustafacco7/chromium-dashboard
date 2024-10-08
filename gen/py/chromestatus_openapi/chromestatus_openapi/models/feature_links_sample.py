from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class FeatureLinksSample(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, type=None, information=None, http_error_code=None, feature_ids=None):  # noqa: E501
        """FeatureLinksSample - a model defined in OpenAPI

        :param url: The url of this FeatureLinksSample.  # noqa: E501
        :type url: str
        :param type: The type of this FeatureLinksSample.  # noqa: E501
        :type type: str
        :param information: The information of this FeatureLinksSample.  # noqa: E501
        :type information: object
        :param http_error_code: The http_error_code of this FeatureLinksSample.  # noqa: E501
        :type http_error_code: int
        :param feature_ids: The feature_ids of this FeatureLinksSample.  # noqa: E501
        :type feature_ids: List[int]
        """
        self.openapi_types = {
            'url': str,
            'type': str,
            'information': object,
            'http_error_code': int,
            'feature_ids': List[int]
        }

        self.attribute_map = {
            'url': 'url',
            'type': 'type',
            'information': 'information',
            'http_error_code': 'http_error_code',
            'feature_ids': 'feature_ids'
        }

        self._url = url
        self._type = type
        self._information = information
        self._http_error_code = http_error_code
        self._feature_ids = feature_ids

    @classmethod
    def from_dict(cls, dikt) -> 'FeatureLinksSample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FeatureLinksSample of this FeatureLinksSample.  # noqa: E501
        :rtype: FeatureLinksSample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this FeatureLinksSample.


        :return: The url of this FeatureLinksSample.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this FeatureLinksSample.


        :param url: The url of this FeatureLinksSample.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def type(self) -> str:
        """Gets the type of this FeatureLinksSample.


        :return: The type of this FeatureLinksSample.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this FeatureLinksSample.


        :param type: The type of this FeatureLinksSample.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def information(self) -> object:
        """Gets the information of this FeatureLinksSample.


        :return: The information of this FeatureLinksSample.
        :rtype: object
        """
        return self._information

    @information.setter
    def information(self, information: object):
        """Sets the information of this FeatureLinksSample.


        :param information: The information of this FeatureLinksSample.
        :type information: object
        """

        self._information = information

    @property
    def http_error_code(self) -> int:
        """Gets the http_error_code of this FeatureLinksSample.


        :return: The http_error_code of this FeatureLinksSample.
        :rtype: int
        """
        return self._http_error_code

    @http_error_code.setter
    def http_error_code(self, http_error_code: int):
        """Sets the http_error_code of this FeatureLinksSample.


        :param http_error_code: The http_error_code of this FeatureLinksSample.
        :type http_error_code: int
        """

        self._http_error_code = http_error_code

    @property
    def feature_ids(self) -> List[int]:
        """Gets the feature_ids of this FeatureLinksSample.


        :return: The feature_ids of this FeatureLinksSample.
        :rtype: List[int]
        """
        return self._feature_ids

    @feature_ids.setter
    def feature_ids(self, feature_ids: List[int]):
        """Sets the feature_ids of this FeatureLinksSample.


        :param feature_ids: The feature_ids of this FeatureLinksSample.
        :type feature_ids: List[int]
        """

        self._feature_ids = feature_ids
