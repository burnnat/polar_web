# -*- coding: utf-8 -*-

"""Main module."""

import logging
import time

import aiohttp
import async_timeout

_LOGGER = logging.getLogger(__name__)

DEFAULT_URL = 'https://flow.polar.com'

HTTP_OK = 200
HEADER_ORIGIN = 'Origin'
COOKIE_SESSION = 'POLAR_SESSION'

class PolarWeb:
    """
    Polar Web API class.
    """

    def __init__(self, websession, email, password, url=DEFAULT_URL, timeout=None):
        self.websession = websession
        self._email = email
        self._password = password
        self._url = url
        self._timeout = timeout
        self._headers = {
            HEADER_ORIGIN: url }

    async def log_weight(self, user_id, date, weight):
        if not await self.login_if_needed():
            return False

        form = aiohttp.FormData()
        form.add_field('userId', user_id)
        form.add_field('date', date.strftime('%d.%m.%Y'))
        form.add_field('weight', '{0:.1f}'.format(weight))
        
        response = await self.send_request('training/updateDailyData', body=form, method='POST')
        return response.status is HTTP_OK

    async def login_if_needed(self):
        if COOKIE_SESSION in self.websession.cookie_jar.filter_cookies(DEFAULT_URL):
            _LOGGER.debug('Active session found, skipping login.')
            return

        _LOGGER.info('No active session found for Polar Web. Attempting login...')
        form = aiohttp.FormData()
        form.add_field('email', self._email)
        form.add_field('password', self._password)

        response = await self.send_request('login', body=form, method='POST')

        if response.status is not HTTP_OK:
            _LOGGER.error('Login failed. Please check user credentials.')
            return False
        else:
            return True

    async def send_request(self, endpoint, params=None, body=None, method='GET'):
        """Send request to Polar."""
        try:
            url = '{url}/{endpoint}'.format(
                url=self._url,
                endpoint=endpoint
            )

            _LOGGER.debug("Sending request to endpoint %s", url)

            async with self.websession.request(method=method, url=url, params=params, data=body, headers=self._headers, timeout=self._timeout) as response:
                if response.status == HTTP_OK:
                    return response
                else:
                    _LOGGER.warning("Error %d from Polar.", response.status)
                    return None

        except (aiohttp.ClientError, aiohttp.ClientConnectionError) as e:
            _LOGGER.debug(e, exc_info=True)
            return None