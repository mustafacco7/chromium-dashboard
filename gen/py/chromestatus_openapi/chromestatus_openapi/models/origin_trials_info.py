from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class OriginTrialsInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, display_name=None, description=None, origin_trial_feature_name=None, enabled=None, status=None, chromestatus_url=None, start_milestone=None, end_milestone=None, original_end_milestone=None, end_time=None, documentation_url=None, feedback_url=None, intent_to_experiment_url=None, trial_extensions=None, type=None, allow_third_party_origins=None):  # noqa: E501
        """OriginTrialsInfo - a model defined in OpenAPI

        :param id: The id of this OriginTrialsInfo.  # noqa: E501
        :type id: str
        :param display_name: The display_name of this OriginTrialsInfo.  # noqa: E501
        :type display_name: str
        :param description: The description of this OriginTrialsInfo.  # noqa: E501
        :type description: str
        :param origin_trial_feature_name: The origin_trial_feature_name of this OriginTrialsInfo.  # noqa: E501
        :type origin_trial_feature_name: str
        :param enabled: The enabled of this OriginTrialsInfo.  # noqa: E501
        :type enabled: bool
        :param status: The status of this OriginTrialsInfo.  # noqa: E501
        :type status: str
        :param chromestatus_url: The chromestatus_url of this OriginTrialsInfo.  # noqa: E501
        :type chromestatus_url: str
        :param start_milestone: The start_milestone of this OriginTrialsInfo.  # noqa: E501
        :type start_milestone: str
        :param end_milestone: The end_milestone of this OriginTrialsInfo.  # noqa: E501
        :type end_milestone: str
        :param original_end_milestone: The original_end_milestone of this OriginTrialsInfo.  # noqa: E501
        :type original_end_milestone: str
        :param end_time: The end_time of this OriginTrialsInfo.  # noqa: E501
        :type end_time: str
        :param documentation_url: The documentation_url of this OriginTrialsInfo.  # noqa: E501
        :type documentation_url: str
        :param feedback_url: The feedback_url of this OriginTrialsInfo.  # noqa: E501
        :type feedback_url: str
        :param intent_to_experiment_url: The intent_to_experiment_url of this OriginTrialsInfo.  # noqa: E501
        :type intent_to_experiment_url: str
        :param trial_extensions: The trial_extensions of this OriginTrialsInfo.  # noqa: E501
        :type trial_extensions: List[object]
        :param type: The type of this OriginTrialsInfo.  # noqa: E501
        :type type: str
        :param allow_third_party_origins: The allow_third_party_origins of this OriginTrialsInfo.  # noqa: E501
        :type allow_third_party_origins: bool
        """
        self.openapi_types = {
            'id': str,
            'display_name': str,
            'description': str,
            'origin_trial_feature_name': str,
            'enabled': bool,
            'status': str,
            'chromestatus_url': str,
            'start_milestone': str,
            'end_milestone': str,
            'original_end_milestone': str,
            'end_time': str,
            'documentation_url': str,
            'feedback_url': str,
            'intent_to_experiment_url': str,
            'trial_extensions': List[object],
            'type': str,
            'allow_third_party_origins': bool
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'display_name',
            'description': 'description',
            'origin_trial_feature_name': 'origin_trial_feature_name',
            'enabled': 'enabled',
            'status': 'status',
            'chromestatus_url': 'chromestatus_url',
            'start_milestone': 'start_milestone',
            'end_milestone': 'end_milestone',
            'original_end_milestone': 'original_end_milestone',
            'end_time': 'end_time',
            'documentation_url': 'documentation_url',
            'feedback_url': 'feedback_url',
            'intent_to_experiment_url': 'intent_to_experiment_url',
            'trial_extensions': 'trial_extensions',
            'type': 'type',
            'allow_third_party_origins': 'allow_third_party_origins'
        }

        self._id = id
        self._display_name = display_name
        self._description = description
        self._origin_trial_feature_name = origin_trial_feature_name
        self._enabled = enabled
        self._status = status
        self._chromestatus_url = chromestatus_url
        self._start_milestone = start_milestone
        self._end_milestone = end_milestone
        self._original_end_milestone = original_end_milestone
        self._end_time = end_time
        self._documentation_url = documentation_url
        self._feedback_url = feedback_url
        self._intent_to_experiment_url = intent_to_experiment_url
        self._trial_extensions = trial_extensions
        self._type = type
        self._allow_third_party_origins = allow_third_party_origins

    @classmethod
    def from_dict(cls, dikt) -> 'OriginTrialsInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OriginTrialsInfo of this OriginTrialsInfo.  # noqa: E501
        :rtype: OriginTrialsInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this OriginTrialsInfo.


        :return: The id of this OriginTrialsInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this OriginTrialsInfo.


        :param id: The id of this OriginTrialsInfo.
        :type id: str
        """

        self._id = id

    @property
    def display_name(self) -> str:
        """Gets the display_name of this OriginTrialsInfo.


        :return: The display_name of this OriginTrialsInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this OriginTrialsInfo.


        :param display_name: The display_name of this OriginTrialsInfo.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self) -> str:
        """Gets the description of this OriginTrialsInfo.


        :return: The description of this OriginTrialsInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this OriginTrialsInfo.


        :param description: The description of this OriginTrialsInfo.
        :type description: str
        """

        self._description = description

    @property
    def origin_trial_feature_name(self) -> str:
        """Gets the origin_trial_feature_name of this OriginTrialsInfo.


        :return: The origin_trial_feature_name of this OriginTrialsInfo.
        :rtype: str
        """
        return self._origin_trial_feature_name

    @origin_trial_feature_name.setter
    def origin_trial_feature_name(self, origin_trial_feature_name: str):
        """Sets the origin_trial_feature_name of this OriginTrialsInfo.


        :param origin_trial_feature_name: The origin_trial_feature_name of this OriginTrialsInfo.
        :type origin_trial_feature_name: str
        """

        self._origin_trial_feature_name = origin_trial_feature_name

    @property
    def enabled(self) -> bool:
        """Gets the enabled of this OriginTrialsInfo.


        :return: The enabled of this OriginTrialsInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        """Sets the enabled of this OriginTrialsInfo.


        :param enabled: The enabled of this OriginTrialsInfo.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def status(self) -> str:
        """Gets the status of this OriginTrialsInfo.


        :return: The status of this OriginTrialsInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this OriginTrialsInfo.


        :param status: The status of this OriginTrialsInfo.
        :type status: str
        """

        self._status = status

    @property
    def chromestatus_url(self) -> str:
        """Gets the chromestatus_url of this OriginTrialsInfo.


        :return: The chromestatus_url of this OriginTrialsInfo.
        :rtype: str
        """
        return self._chromestatus_url

    @chromestatus_url.setter
    def chromestatus_url(self, chromestatus_url: str):
        """Sets the chromestatus_url of this OriginTrialsInfo.


        :param chromestatus_url: The chromestatus_url of this OriginTrialsInfo.
        :type chromestatus_url: str
        """

        self._chromestatus_url = chromestatus_url

    @property
    def start_milestone(self) -> str:
        """Gets the start_milestone of this OriginTrialsInfo.


        :return: The start_milestone of this OriginTrialsInfo.
        :rtype: str
        """
        return self._start_milestone

    @start_milestone.setter
    def start_milestone(self, start_milestone: str):
        """Sets the start_milestone of this OriginTrialsInfo.


        :param start_milestone: The start_milestone of this OriginTrialsInfo.
        :type start_milestone: str
        """

        self._start_milestone = start_milestone

    @property
    def end_milestone(self) -> str:
        """Gets the end_milestone of this OriginTrialsInfo.


        :return: The end_milestone of this OriginTrialsInfo.
        :rtype: str
        """
        return self._end_milestone

    @end_milestone.setter
    def end_milestone(self, end_milestone: str):
        """Sets the end_milestone of this OriginTrialsInfo.


        :param end_milestone: The end_milestone of this OriginTrialsInfo.
        :type end_milestone: str
        """

        self._end_milestone = end_milestone

    @property
    def original_end_milestone(self) -> str:
        """Gets the original_end_milestone of this OriginTrialsInfo.


        :return: The original_end_milestone of this OriginTrialsInfo.
        :rtype: str
        """
        return self._original_end_milestone

    @original_end_milestone.setter
    def original_end_milestone(self, original_end_milestone: str):
        """Sets the original_end_milestone of this OriginTrialsInfo.


        :param original_end_milestone: The original_end_milestone of this OriginTrialsInfo.
        :type original_end_milestone: str
        """

        self._original_end_milestone = original_end_milestone

    @property
    def end_time(self) -> str:
        """Gets the end_time of this OriginTrialsInfo.


        :return: The end_time of this OriginTrialsInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: str):
        """Sets the end_time of this OriginTrialsInfo.


        :param end_time: The end_time of this OriginTrialsInfo.
        :type end_time: str
        """

        self._end_time = end_time

    @property
    def documentation_url(self) -> str:
        """Gets the documentation_url of this OriginTrialsInfo.


        :return: The documentation_url of this OriginTrialsInfo.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url: str):
        """Sets the documentation_url of this OriginTrialsInfo.


        :param documentation_url: The documentation_url of this OriginTrialsInfo.
        :type documentation_url: str
        """

        self._documentation_url = documentation_url

    @property
    def feedback_url(self) -> str:
        """Gets the feedback_url of this OriginTrialsInfo.


        :return: The feedback_url of this OriginTrialsInfo.
        :rtype: str
        """
        return self._feedback_url

    @feedback_url.setter
    def feedback_url(self, feedback_url: str):
        """Sets the feedback_url of this OriginTrialsInfo.


        :param feedback_url: The feedback_url of this OriginTrialsInfo.
        :type feedback_url: str
        """

        self._feedback_url = feedback_url

    @property
    def intent_to_experiment_url(self) -> str:
        """Gets the intent_to_experiment_url of this OriginTrialsInfo.


        :return: The intent_to_experiment_url of this OriginTrialsInfo.
        :rtype: str
        """
        return self._intent_to_experiment_url

    @intent_to_experiment_url.setter
    def intent_to_experiment_url(self, intent_to_experiment_url: str):
        """Sets the intent_to_experiment_url of this OriginTrialsInfo.


        :param intent_to_experiment_url: The intent_to_experiment_url of this OriginTrialsInfo.
        :type intent_to_experiment_url: str
        """

        self._intent_to_experiment_url = intent_to_experiment_url

    @property
    def trial_extensions(self) -> List[object]:
        """Gets the trial_extensions of this OriginTrialsInfo.


        :return: The trial_extensions of this OriginTrialsInfo.
        :rtype: List[object]
        """
        return self._trial_extensions

    @trial_extensions.setter
    def trial_extensions(self, trial_extensions: List[object]):
        """Sets the trial_extensions of this OriginTrialsInfo.


        :param trial_extensions: The trial_extensions of this OriginTrialsInfo.
        :type trial_extensions: List[object]
        """

        self._trial_extensions = trial_extensions

    @property
    def type(self) -> str:
        """Gets the type of this OriginTrialsInfo.


        :return: The type of this OriginTrialsInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this OriginTrialsInfo.


        :param type: The type of this OriginTrialsInfo.
        :type type: str
        """

        self._type = type

    @property
    def allow_third_party_origins(self) -> bool:
        """Gets the allow_third_party_origins of this OriginTrialsInfo.


        :return: The allow_third_party_origins of this OriginTrialsInfo.
        :rtype: bool
        """
        return self._allow_third_party_origins

    @allow_third_party_origins.setter
    def allow_third_party_origins(self, allow_third_party_origins: bool):
        """Sets the allow_third_party_origins of this OriginTrialsInfo.


        :param allow_third_party_origins: The allow_third_party_origins of this OriginTrialsInfo.
        :type allow_third_party_origins: bool
        """

        self._allow_third_party_origins = allow_third_party_origins
