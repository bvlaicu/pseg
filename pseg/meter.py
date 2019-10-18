"""PSE&G Gas Meter"""
import requests
import logging

_LOGGER = logging.getLogger(__name__)


class MeterError(Exception):
    pass


class Meter(object):
    """A gas meter of PSE&G.

    Attributes:
        energize_id: A string representing the meter's energize id
        session_id: A string representing the meter's session id
    """

    def __init__(self, energize_id, session_id):
        """Return a meter object whose energize id is *energize_id*"""
        self.energize_id = energize_id
        self.session_id = session_id

    def last_gas_read(self):
        """Return the last gas meter read"""
        try:
            url = 'https://myenergy.pseg.com/api/meter_for_year'
            _LOGGER.debug("url = %s", url)

            headers = {"Cookie": "_energize_session=%s; EMSSESSIONID=%s;" % (self.energize_id, self.session_id)}
            _LOGGER.debug("headers = %s", headers)

            response = requests.get(url, headers=headers)
            _LOGGER.debug("response = %s", response)

            jsonResponse = response.json()
            _LOGGER.debug("jsonResponse = %s", jsonResponse)

            if 'errors' in jsonResponse:
                raise MeterError('Error in getting the meter data: %s',
                                 jsonResponse['errors'])

            # parse the return reads and extract the most recent one
            # (i.e. last one in list)
            lastRead = None
            for read in jsonResponse['samples']['GAS']['GAS']:
                lastRead = read
            _LOGGER.debug("lastRead = %s", lastRead)

            val = lastRead
            _LOGGER.debug("val = %s", val)

            return val
        except requests.exceptions.RequestException:
            raise MeterError("Error retrieving meter data")

    def last_gas_read_consumption(self):
        """Return the consumption from the last gas meter read (in therms)"""
        try:
            lastRead = self.last_gas_read()

            val = lastRead['consumption']
            _LOGGER.debug("val = %s", val)

            return val
        except requests.exceptions.RequestException:
            raise MeterError("Error retrieving meter data")

    def last_gas_read_cost(self):
        """Return the cost from the last gas meter read (in dollars)"""
        try:
            lastRead = self.last_gas_read()

            val = lastRead['dollars']
            _LOGGER.debug("val = %s", val)

            return val
        except requests.exceptions.RequestException:
            raise MeterError("Error retrieving meter data")
