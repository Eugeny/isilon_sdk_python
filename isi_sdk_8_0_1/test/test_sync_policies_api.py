# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_0_1
from isi_sdk_8_0_1.api.sync_policies_api import SyncPoliciesApi  # noqa: E501
from isi_sdk_8_0_1.rest import ApiException


class TestSyncPoliciesApi(unittest.TestCase):
    """SyncPoliciesApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_0_1.api.sync_policies_api.SyncPoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_policy_reset_item(self):
        """Test case for create_policy_reset_item

        """
        pass


if __name__ == '__main__':
    unittest.main()
