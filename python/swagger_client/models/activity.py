# coding: utf-8

"""
    Route Optimization API

    Our Route Optimization API solves the so called vehicle routing problem fast. It calculates an optimal tour for a set of vehicles, services and constraints

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Activity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, id=None, location_id=None, arr_time=None, end_time=None, waiting_time=None, distance=None, driving_time=None, load_before=None, load_after=None):
        """
        Activity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'location_id': 'str',
            'arr_time': 'int',
            'end_time': 'int',
            'waiting_time': 'int',
            'distance': 'int',
            'driving_time': 'int',
            'load_before': 'list[int]',
            'load_after': 'list[int]'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'location_id': 'location_id',
            'arr_time': 'arr_time',
            'end_time': 'end_time',
            'waiting_time': 'waiting_time',
            'distance': 'distance',
            'driving_time': 'driving_time',
            'load_before': 'load_before',
            'load_after': 'load_after'
        }

        self._type = type
        self._id = id
        self._location_id = location_id
        self._arr_time = arr_time
        self._end_time = end_time
        self._waiting_time = waiting_time
        self._distance = distance
        self._driving_time = driving_time
        self._load_before = load_before
        self._load_after = load_after

    @property
    def type(self):
        """
        Gets the type of this Activity.
        type of activity

        :return: The type of this Activity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Activity.
        type of activity

        :param type: The type of this Activity.
        :type: str
        """
        allowed_values = ["start", "end", "service", "pickupShipment", "deliverShipment", "pickup", "delivery"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this Activity.
        id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to

        :return: The id of this Activity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Activity.
        id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to

        :param id: The id of this Activity.
        :type: str
        """

        self._id = id

    @property
    def location_id(self):
        """
        Gets the location_id of this Activity.
        id that refers to address

        :return: The location_id of this Activity.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this Activity.
        id that refers to address

        :param location_id: The location_id of this Activity.
        :type: str
        """

        self._location_id = location_id

    @property
    def arr_time(self):
        """
        Gets the arr_time of this Activity.
        arrival time at this activity in ms

        :return: The arr_time of this Activity.
        :rtype: int
        """
        return self._arr_time

    @arr_time.setter
    def arr_time(self, arr_time):
        """
        Sets the arr_time of this Activity.
        arrival time at this activity in ms

        :param arr_time: The arr_time of this Activity.
        :type: int
        """

        self._arr_time = arr_time

    @property
    def end_time(self):
        """
        Gets the end_time of this Activity.
        end time of and thus departure time at this activity

        :return: The end_time of this Activity.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this Activity.
        end time of and thus departure time at this activity

        :param end_time: The end_time of this Activity.
        :type: int
        """

        self._end_time = end_time

    @property
    def waiting_time(self):
        """
        Gets the waiting_time of this Activity.
        waiting time at this activity in ms

        :return: The waiting_time of this Activity.
        :rtype: int
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        """
        Sets the waiting_time of this Activity.
        waiting time at this activity in ms

        :param waiting_time: The waiting_time of this Activity.
        :type: int
        """

        self._waiting_time = waiting_time

    @property
    def distance(self):
        """
        Gets the distance of this Activity.
        cumulated distance from start to this activity in m

        :return: The distance of this Activity.
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """
        Sets the distance of this Activity.
        cumulated distance from start to this activity in m

        :param distance: The distance of this Activity.
        :type: int
        """

        self._distance = distance

    @property
    def driving_time(self):
        """
        Gets the driving_time of this Activity.
        driving time of driver in ms

        :return: The driving_time of this Activity.
        :rtype: int
        """
        return self._driving_time

    @driving_time.setter
    def driving_time(self, driving_time):
        """
        Sets the driving_time of this Activity.
        driving time of driver in ms

        :param driving_time: The driving_time of this Activity.
        :type: int
        """

        self._driving_time = driving_time

    @property
    def load_before(self):
        """
        Gets the load_before of this Activity.
        Array with size/capacity dimensions before this activity

        :return: The load_before of this Activity.
        :rtype: list[int]
        """
        return self._load_before

    @load_before.setter
    def load_before(self, load_before):
        """
        Sets the load_before of this Activity.
        Array with size/capacity dimensions before this activity

        :param load_before: The load_before of this Activity.
        :type: list[int]
        """

        self._load_before = load_before

    @property
    def load_after(self):
        """
        Gets the load_after of this Activity.
        Array with size/capacity dimensions after this activity

        :return: The load_after of this Activity.
        :rtype: list[int]
        """
        return self._load_after

    @load_after.setter
    def load_after(self, load_after):
        """
        Sets the load_after of this Activity.
        Array with size/capacity dimensions after this activity

        :param load_after: The load_after of this Activity.
        :type: list[int]
        """

        self._load_after = load_after

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
