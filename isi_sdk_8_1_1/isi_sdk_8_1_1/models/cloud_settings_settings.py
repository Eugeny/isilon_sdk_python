# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_1_1.models.cloud_settings_settings_cloud_policy_defaults import CloudSettingsSettingsCloudPolicyDefaults  # noqa: F401,E501
from isi_sdk_8_1_1.models.cloud_settings_settings_sleep_timeout_cloud_garbage_collection import CloudSettingsSettingsSleepTimeoutCloudGarbageCollection  # noqa: F401,E501


class CloudSettingsSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cloud_policy_defaults': 'CloudSettingsSettingsCloudPolicyDefaults',
        'retry_coefficient_archive': 'str',
        'retry_coefficient_cache_invalidation': 'str',
        'retry_coefficient_cloud_garbage_collection': 'str',
        'retry_coefficient_local_garbage_collection': 'str',
        'retry_coefficient_read_ahead': 'str',
        'retry_coefficient_recall': 'str',
        'retry_coefficient_writeback': 'str',
        'sleep_timeout_archive': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection',
        'sleep_timeout_cache_invalidation': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection',
        'sleep_timeout_cloud_garbage_collection': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection',
        'sleep_timeout_local_garbage_collection': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection',
        'sleep_timeout_read_ahead': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection',
        'sleep_timeout_recall': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection',
        'sleep_timeout_writeback': 'CloudSettingsSettingsSleepTimeoutCloudGarbageCollection'
    }

    attribute_map = {
        'cloud_policy_defaults': 'cloud_policy_defaults',
        'retry_coefficient_archive': 'retry_coefficient_archive',
        'retry_coefficient_cache_invalidation': 'retry_coefficient_cache_invalidation',
        'retry_coefficient_cloud_garbage_collection': 'retry_coefficient_cloud_garbage_collection',
        'retry_coefficient_local_garbage_collection': 'retry_coefficient_local_garbage_collection',
        'retry_coefficient_read_ahead': 'retry_coefficient_read_ahead',
        'retry_coefficient_recall': 'retry_coefficient_recall',
        'retry_coefficient_writeback': 'retry_coefficient_writeback',
        'sleep_timeout_archive': 'sleep_timeout_archive',
        'sleep_timeout_cache_invalidation': 'sleep_timeout_cache_invalidation',
        'sleep_timeout_cloud_garbage_collection': 'sleep_timeout_cloud_garbage_collection',
        'sleep_timeout_local_garbage_collection': 'sleep_timeout_local_garbage_collection',
        'sleep_timeout_read_ahead': 'sleep_timeout_read_ahead',
        'sleep_timeout_recall': 'sleep_timeout_recall',
        'sleep_timeout_writeback': 'sleep_timeout_writeback'
    }

    def __init__(self, cloud_policy_defaults=None, retry_coefficient_archive=None, retry_coefficient_cache_invalidation=None, retry_coefficient_cloud_garbage_collection=None, retry_coefficient_local_garbage_collection=None, retry_coefficient_read_ahead=None, retry_coefficient_recall=None, retry_coefficient_writeback=None, sleep_timeout_archive=None, sleep_timeout_cache_invalidation=None, sleep_timeout_cloud_garbage_collection=None, sleep_timeout_local_garbage_collection=None, sleep_timeout_read_ahead=None, sleep_timeout_recall=None, sleep_timeout_writeback=None):  # noqa: E501
        """CloudSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._cloud_policy_defaults = None
        self._retry_coefficient_archive = None
        self._retry_coefficient_cache_invalidation = None
        self._retry_coefficient_cloud_garbage_collection = None
        self._retry_coefficient_local_garbage_collection = None
        self._retry_coefficient_read_ahead = None
        self._retry_coefficient_recall = None
        self._retry_coefficient_writeback = None
        self._sleep_timeout_archive = None
        self._sleep_timeout_cache_invalidation = None
        self._sleep_timeout_cloud_garbage_collection = None
        self._sleep_timeout_local_garbage_collection = None
        self._sleep_timeout_read_ahead = None
        self._sleep_timeout_recall = None
        self._sleep_timeout_writeback = None
        self.discriminator = None

        if cloud_policy_defaults is not None:
            self.cloud_policy_defaults = cloud_policy_defaults
        if retry_coefficient_archive is not None:
            self.retry_coefficient_archive = retry_coefficient_archive
        if retry_coefficient_cache_invalidation is not None:
            self.retry_coefficient_cache_invalidation = retry_coefficient_cache_invalidation
        if retry_coefficient_cloud_garbage_collection is not None:
            self.retry_coefficient_cloud_garbage_collection = retry_coefficient_cloud_garbage_collection
        if retry_coefficient_local_garbage_collection is not None:
            self.retry_coefficient_local_garbage_collection = retry_coefficient_local_garbage_collection
        if retry_coefficient_read_ahead is not None:
            self.retry_coefficient_read_ahead = retry_coefficient_read_ahead
        if retry_coefficient_recall is not None:
            self.retry_coefficient_recall = retry_coefficient_recall
        if retry_coefficient_writeback is not None:
            self.retry_coefficient_writeback = retry_coefficient_writeback
        if sleep_timeout_archive is not None:
            self.sleep_timeout_archive = sleep_timeout_archive
        if sleep_timeout_cache_invalidation is not None:
            self.sleep_timeout_cache_invalidation = sleep_timeout_cache_invalidation
        if sleep_timeout_cloud_garbage_collection is not None:
            self.sleep_timeout_cloud_garbage_collection = sleep_timeout_cloud_garbage_collection
        if sleep_timeout_local_garbage_collection is not None:
            self.sleep_timeout_local_garbage_collection = sleep_timeout_local_garbage_collection
        if sleep_timeout_read_ahead is not None:
            self.sleep_timeout_read_ahead = sleep_timeout_read_ahead
        if sleep_timeout_recall is not None:
            self.sleep_timeout_recall = sleep_timeout_recall
        if sleep_timeout_writeback is not None:
            self.sleep_timeout_writeback = sleep_timeout_writeback

    @property
    def cloud_policy_defaults(self):
        """Gets the cloud_policy_defaults of this CloudSettingsSettings.  # noqa: E501

        The default filepool policy values for cloudpools.  # noqa: E501

        :return: The cloud_policy_defaults of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsCloudPolicyDefaults
        """
        return self._cloud_policy_defaults

    @cloud_policy_defaults.setter
    def cloud_policy_defaults(self, cloud_policy_defaults):
        """Sets the cloud_policy_defaults of this CloudSettingsSettings.

        The default filepool policy values for cloudpools.  # noqa: E501

        :param cloud_policy_defaults: The cloud_policy_defaults of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsCloudPolicyDefaults
        """

        self._cloud_policy_defaults = cloud_policy_defaults

    @property
    def retry_coefficient_archive(self):
        """Gets the retry_coefficient_archive of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive archive attempts.  # noqa: E501

        :return: The retry_coefficient_archive of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_archive

    @retry_coefficient_archive.setter
    def retry_coefficient_archive(self, retry_coefficient_archive):
        """Sets the retry_coefficient_archive of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive archive attempts.  # noqa: E501

        :param retry_coefficient_archive: The retry_coefficient_archive of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_archive = retry_coefficient_archive

    @property
    def retry_coefficient_cache_invalidation(self):
        """Gets the retry_coefficient_cache_invalidation of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive cache invalidation attempts.  # noqa: E501

        :return: The retry_coefficient_cache_invalidation of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_cache_invalidation

    @retry_coefficient_cache_invalidation.setter
    def retry_coefficient_cache_invalidation(self, retry_coefficient_cache_invalidation):
        """Sets the retry_coefficient_cache_invalidation of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive cache invalidation attempts.  # noqa: E501

        :param retry_coefficient_cache_invalidation: The retry_coefficient_cache_invalidation of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_cache_invalidation = retry_coefficient_cache_invalidation

    @property
    def retry_coefficient_cloud_garbage_collection(self):
        """Gets the retry_coefficient_cloud_garbage_collection of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive cloud garbage collection attempts.  # noqa: E501

        :return: The retry_coefficient_cloud_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_cloud_garbage_collection

    @retry_coefficient_cloud_garbage_collection.setter
    def retry_coefficient_cloud_garbage_collection(self, retry_coefficient_cloud_garbage_collection):
        """Sets the retry_coefficient_cloud_garbage_collection of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive cloud garbage collection attempts.  # noqa: E501

        :param retry_coefficient_cloud_garbage_collection: The retry_coefficient_cloud_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_cloud_garbage_collection = retry_coefficient_cloud_garbage_collection

    @property
    def retry_coefficient_local_garbage_collection(self):
        """Gets the retry_coefficient_local_garbage_collection of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive local garbage collection attempts.  # noqa: E501

        :return: The retry_coefficient_local_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_local_garbage_collection

    @retry_coefficient_local_garbage_collection.setter
    def retry_coefficient_local_garbage_collection(self, retry_coefficient_local_garbage_collection):
        """Sets the retry_coefficient_local_garbage_collection of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive local garbage collection attempts.  # noqa: E501

        :param retry_coefficient_local_garbage_collection: The retry_coefficient_local_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_local_garbage_collection = retry_coefficient_local_garbage_collection

    @property
    def retry_coefficient_read_ahead(self):
        """Gets the retry_coefficient_read_ahead of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive read ahead attempts.  # noqa: E501

        :return: The retry_coefficient_read_ahead of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_read_ahead

    @retry_coefficient_read_ahead.setter
    def retry_coefficient_read_ahead(self, retry_coefficient_read_ahead):
        """Sets the retry_coefficient_read_ahead of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive read ahead attempts.  # noqa: E501

        :param retry_coefficient_read_ahead: The retry_coefficient_read_ahead of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_read_ahead = retry_coefficient_read_ahead

    @property
    def retry_coefficient_recall(self):
        """Gets the retry_coefficient_recall of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive recall attempts.  # noqa: E501

        :return: The retry_coefficient_recall of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_recall

    @retry_coefficient_recall.setter
    def retry_coefficient_recall(self, retry_coefficient_recall):
        """Sets the retry_coefficient_recall of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive recall attempts.  # noqa: E501

        :param retry_coefficient_recall: The retry_coefficient_recall of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_recall = retry_coefficient_recall

    @property
    def retry_coefficient_writeback(self):
        """Gets the retry_coefficient_writeback of this CloudSettingsSettings.  # noqa: E501

        Coefficients in the quadratic function for determining the rest period between successive writeback attempts.  # noqa: E501

        :return: The retry_coefficient_writeback of this CloudSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._retry_coefficient_writeback

    @retry_coefficient_writeback.setter
    def retry_coefficient_writeback(self, retry_coefficient_writeback):
        """Sets the retry_coefficient_writeback of this CloudSettingsSettings.

        Coefficients in the quadratic function for determining the rest period between successive writeback attempts.  # noqa: E501

        :param retry_coefficient_writeback: The retry_coefficient_writeback of this CloudSettingsSettings.  # noqa: E501
        :type: str
        """

        self._retry_coefficient_writeback = retry_coefficient_writeback

    @property
    def sleep_timeout_archive(self):
        """Gets the sleep_timeout_archive of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file archive operations.  # noqa: E501

        :return: The sleep_timeout_archive of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_archive

    @sleep_timeout_archive.setter
    def sleep_timeout_archive(self, sleep_timeout_archive):
        """Sets the sleep_timeout_archive of this CloudSettingsSettings.

        Amount of time to wait between successive file archive operations.  # noqa: E501

        :param sleep_timeout_archive: The sleep_timeout_archive of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_archive = sleep_timeout_archive

    @property
    def sleep_timeout_cache_invalidation(self):
        """Gets the sleep_timeout_cache_invalidation of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file cache_invalidation operations.  # noqa: E501

        :return: The sleep_timeout_cache_invalidation of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_cache_invalidation

    @sleep_timeout_cache_invalidation.setter
    def sleep_timeout_cache_invalidation(self, sleep_timeout_cache_invalidation):
        """Sets the sleep_timeout_cache_invalidation of this CloudSettingsSettings.

        Amount of time to wait between successive file cache_invalidation operations.  # noqa: E501

        :param sleep_timeout_cache_invalidation: The sleep_timeout_cache_invalidation of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_cache_invalidation = sleep_timeout_cache_invalidation

    @property
    def sleep_timeout_cloud_garbage_collection(self):
        """Gets the sleep_timeout_cloud_garbage_collection of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file cloud garbage collection operations.  # noqa: E501

        :return: The sleep_timeout_cloud_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_cloud_garbage_collection

    @sleep_timeout_cloud_garbage_collection.setter
    def sleep_timeout_cloud_garbage_collection(self, sleep_timeout_cloud_garbage_collection):
        """Sets the sleep_timeout_cloud_garbage_collection of this CloudSettingsSettings.

        Amount of time to wait between successive file cloud garbage collection operations.  # noqa: E501

        :param sleep_timeout_cloud_garbage_collection: The sleep_timeout_cloud_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_cloud_garbage_collection = sleep_timeout_cloud_garbage_collection

    @property
    def sleep_timeout_local_garbage_collection(self):
        """Gets the sleep_timeout_local_garbage_collection of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file local garbage collection operations.  # noqa: E501

        :return: The sleep_timeout_local_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_local_garbage_collection

    @sleep_timeout_local_garbage_collection.setter
    def sleep_timeout_local_garbage_collection(self, sleep_timeout_local_garbage_collection):
        """Sets the sleep_timeout_local_garbage_collection of this CloudSettingsSettings.

        Amount of time to wait between successive file local garbage collection operations.  # noqa: E501

        :param sleep_timeout_local_garbage_collection: The sleep_timeout_local_garbage_collection of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_local_garbage_collection = sleep_timeout_local_garbage_collection

    @property
    def sleep_timeout_read_ahead(self):
        """Gets the sleep_timeout_read_ahead of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file read ahead operations.  # noqa: E501

        :return: The sleep_timeout_read_ahead of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_read_ahead

    @sleep_timeout_read_ahead.setter
    def sleep_timeout_read_ahead(self, sleep_timeout_read_ahead):
        """Sets the sleep_timeout_read_ahead of this CloudSettingsSettings.

        Amount of time to wait between successive file read ahead operations.  # noqa: E501

        :param sleep_timeout_read_ahead: The sleep_timeout_read_ahead of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_read_ahead = sleep_timeout_read_ahead

    @property
    def sleep_timeout_recall(self):
        """Gets the sleep_timeout_recall of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file recall operations.  # noqa: E501

        :return: The sleep_timeout_recall of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_recall

    @sleep_timeout_recall.setter
    def sleep_timeout_recall(self, sleep_timeout_recall):
        """Sets the sleep_timeout_recall of this CloudSettingsSettings.

        Amount of time to wait between successive file recall operations.  # noqa: E501

        :param sleep_timeout_recall: The sleep_timeout_recall of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_recall = sleep_timeout_recall

    @property
    def sleep_timeout_writeback(self):
        """Gets the sleep_timeout_writeback of this CloudSettingsSettings.  # noqa: E501

        Amount of time to wait between successive file writeback operations.  # noqa: E501

        :return: The sleep_timeout_writeback of this CloudSettingsSettings.  # noqa: E501
        :rtype: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """
        return self._sleep_timeout_writeback

    @sleep_timeout_writeback.setter
    def sleep_timeout_writeback(self, sleep_timeout_writeback):
        """Sets the sleep_timeout_writeback of this CloudSettingsSettings.

        Amount of time to wait between successive file writeback operations.  # noqa: E501

        :param sleep_timeout_writeback: The sleep_timeout_writeback of this CloudSettingsSettings.  # noqa: E501
        :type: CloudSettingsSettingsSleepTimeoutCloudGarbageCollection
        """

        self._sleep_timeout_writeback = sleep_timeout_writeback

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
