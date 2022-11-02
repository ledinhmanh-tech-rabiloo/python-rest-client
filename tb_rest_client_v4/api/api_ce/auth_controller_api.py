# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class AuthControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activate_user_using_post(self, **kwargs):  # noqa: E501
        """Activate User  # noqa: E501

        Checks the activation token and updates corresponding user password in the database. Now the user may start using his password to login. The response already contains the [JWT](https://jwt.io) activation and refresh tokens, to simplify the user activation flow and avoid asking user to input password again after activation. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_user_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActivateUserRequest body:
        :param bool send_activation_mail: sendActivationMail
        :return: JWTTokenPair
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.activate_user_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.activate_user_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def activate_user_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Activate User  # noqa: E501

        Checks the activation token and updates corresponding user password in the database. Now the user may start using his password to login. The response already contains the [JWT](https://jwt.io) activation and refresh tokens, to simplify the user activation flow and avoid asking user to input password again after activation. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_user_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActivateUserRequest body:
        :param bool send_activation_mail: sendActivationMail
        :return: JWTTokenPair
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'send_activation_mail']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'send_activation_mail' in params:
            query_params.append(('sendActivationMail', params['send_activation_mail']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/activate{?sendActivationMail}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JWTTokenPair',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_password_using_post(self, **kwargs):  # noqa: E501
        """Change password for current User (changePassword)  # noqa: E501

        Change the password for the User which credentials are used to perform this REST API call. Be aware that previously generated [JWT](https://jwt.io/) tokens will be still valid until they expire.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_password_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePasswordRequest body:
        :return: ObjectNode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_password_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.change_password_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def change_password_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Change password for current User (changePassword)  # noqa: E501

        Change the password for the User which credentials are used to perform this REST API call. Be aware that previously generated [JWT](https://jwt.io/) tokens will be still valid until they expire.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_password_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePasswordRequest body:
        :return: ObjectNode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_password_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/auth/changePassword', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectNode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def check_activate_token_using_get(self, activate_token, **kwargs):  # noqa: E501
        """Check Activate User Token (checkActivateToken)  # noqa: E501

        Checks the activation token and forwards user to 'Create Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Create Password' page and same 'activateToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_activate_token_using_get(activate_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activate_token: The activate token string. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_activate_token_using_get_with_http_info(activate_token, **kwargs)  # noqa: E501
        else:
            (data) = self.check_activate_token_using_get_with_http_info(activate_token, **kwargs)  # noqa: E501
            return data

    def check_activate_token_using_get_with_http_info(self, activate_token, **kwargs):  # noqa: E501
        """Check Activate User Token (checkActivateToken)  # noqa: E501

        Checks the activation token and forwards user to 'Create Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Create Password' page and same 'activateToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_activate_token_using_get_with_http_info(activate_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activate_token: The activate token string. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activate_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_activate_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activate_token' is set
        if ('activate_token' not in params or
                params['activate_token'] is None):
            raise ValueError("Missing the required parameter `activate_token` when calling `check_activate_token_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'activate_token' in params:
            query_params.append(('activateToken', params['activate_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/activate{?activateToken}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def check_reset_token_using_get(self, reset_token, **kwargs):  # noqa: E501
        """Check password reset token (checkResetToken)  # noqa: E501

        Checks the password reset token and forwards user to 'Reset Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Reset Password' page and same 'resetToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_reset_token_using_get(reset_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str reset_token: The reset token string. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_reset_token_using_get_with_http_info(reset_token, **kwargs)  # noqa: E501
        else:
            (data) = self.check_reset_token_using_get_with_http_info(reset_token, **kwargs)  # noqa: E501
            return data

    def check_reset_token_using_get_with_http_info(self, reset_token, **kwargs):  # noqa: E501
        """Check password reset token (checkResetToken)  # noqa: E501

        Checks the password reset token and forwards user to 'Reset Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Reset Password' page and same 'resetToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_reset_token_using_get_with_http_info(reset_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str reset_token: The reset token string. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reset_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_reset_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reset_token' is set
        if ('reset_token' not in params or
                params['reset_token'] is None):
            raise ValueError("Missing the required parameter `reset_token` when calling `check_reset_token_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'reset_token' in params:
            query_params.append(('resetToken', params['reset_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/resetPassword{?resetToken}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_password_policy_using_get(self, **kwargs):  # noqa: E501
        """Get the current User password policy (getUserPasswordPolicy)  # noqa: E501

        API call to get the password policy for the password validation form(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_password_policy_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserPasswordPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_password_policy_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_password_policy_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_password_policy_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the current User password policy (getUserPasswordPolicy)  # noqa: E501

        API call to get the password policy for the password validation form(s).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_password_policy_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserPasswordPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_password_policy_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/userPasswordPolicy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserPasswordPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_using_get(self, **kwargs):  # noqa: E501
        """Get current User (getUser)  # noqa: E501

        Get the information about the User which credentials are used to perform this REST API call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get current User (getUser)  # noqa: E501

        Get the information about the User which credentials are used to perform this REST API call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/api/auth/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout_using_post(self, **kwargs):  # noqa: E501
        """Logout (logout)  # noqa: E501

        Special API call to record the 'logout' of the user to the Audit Logs. Since platform uses [JWT](https://jwt.io/), the actual logout is the procedure of clearing the [JWT](https://jwt.io/) token on the client side.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logout_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.logout_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def logout_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Logout (logout)  # noqa: E501

        Special API call to record the 'logout' of the user to the Audit Logs. Since platform uses [JWT](https://jwt.io/), the actual logout is the procedure of clearing the [JWT](https://jwt.io/) token on the client side.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/api/auth/logout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_reset_password_by_email_using_post(self, **kwargs):  # noqa: E501
        """Request reset password email (requestResetPasswordByEmail)  # noqa: E501

        Request to send the reset password email if the user with specified email address is present in the database. Always return '200 OK' status for security purposes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_reset_password_by_email_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordEmailRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_reset_password_by_email_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.request_reset_password_by_email_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def request_reset_password_by_email_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Request reset password email (requestResetPasswordByEmail)  # noqa: E501

        Request to send the reset password email if the user with specified email address is present in the database. Always return '200 OK' status for security purposes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_reset_password_by_email_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordEmailRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_reset_password_by_email_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/resetPasswordByEmail', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_password_using_post(self, **kwargs):  # noqa: E501
        """Reset password (resetPassword)  # noqa: E501

        Checks the password reset token and updates the password. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_password_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordRequest body:
        :return: JWTTokenPair
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_password_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.reset_password_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def reset_password_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Reset password (resetPassword)  # noqa: E501

        Checks the password reset token and updates the password. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_password_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordRequest body:
        :return: JWTTokenPair
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_password_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/resetPassword', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JWTTokenPair',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)