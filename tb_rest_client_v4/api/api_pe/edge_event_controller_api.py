# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client_v4.api_client import ApiClient


class EdgeEventControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_edge_events_using_get(self, edge_id, page_size, page, **kwargs):  # noqa: E501
        """Get Edge Events (getEdgeEvents)  # noqa: E501

        Returns a page of edge events for the requested edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_edge_events_using_get(edge_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_id: A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'startsWith' filter based on the edge event type name.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Edge events with creation time before it won't be queried
        :param int end_time: Timestamp. Edge events with creation time after it won't be queried
        :return: PageDataEdgeEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_edge_events_using_get_with_http_info(edge_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_edge_events_using_get_with_http_info(edge_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_edge_events_using_get_with_http_info(self, edge_id, page_size, page, **kwargs):  # noqa: E501
        """Get Edge Events (getEdgeEvents)  # noqa: E501

        Returns a page of edge events for the requested edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_edge_events_using_get_with_http_info(edge_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str edge_id: A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'startsWith' filter based on the edge event type name.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Edge events with creation time before it won't be queried
        :param int end_time: Timestamp. Edge events with creation time after it won't be queried
        :return: PageDataEdgeEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edge_id', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_edge_events_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edge_id' is set
        if ('edge_id' not in params or
                params['edge_id'] is None):
            raise ValueError("Missing the required parameter `edge_id` when calling `get_edge_events_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_edge_events_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_edge_events_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edge_id' in params:
            path_params['edgeId'] = params['edge_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/edge/{edgeId}/events{?endTime,page,pageSize,sortOrder,sortProperty,startTime,textSearch}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataEdgeEvent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
