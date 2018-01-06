# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataLakeAnalyticsCatalogCredentialCreateParameters(Model):
    """Data Lake Analytics catalog credential creation parameters.

    :param password: the password for the credential and user with access to
     the data source.
    :type password: str
    :param uri: the URI identifier for the data source this credential can
     connect to in the format <hostname>:<port>
    :type uri: str
    :param user_id: the object identifier for the user associated with this
     credential with access to the data source.
    :type user_id: str
    """

    _validation = {
        'password': {'required': True},
        'uri': {'required': True},
        'user_id': {'required': True},
    }

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
    }

    def __init__(self, password, uri, user_id):
        super(DataLakeAnalyticsCatalogCredentialCreateParameters, self).__init__()
        self.password = password
        self.uri = uri
        self.user_id = user_id
