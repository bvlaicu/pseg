"""Main test class for pseg"""

from pseg import Meter
from pseg import MeterError
import pytest


def test_get_last_meter_read():
    meter = Meter("17baf96d8fdc093b772cf428b74d3151",
                  "bRWWRMk6PCka1MQ%2BzR%2BUYq9eSTJhXpsXlm8c5LG0P3H%2BH5GnREEkURNfqi7HNESpaZxxMafUhDSQoaRDvDC1Aw%3D%3D")
    read = meter.last_gas_read()
    assert 'consumption' in read
    assert 'dollars' in read


def test_get_last_meter_read_consumption():
    meter = Meter("17baf96d8fdc093b772cf428b74d3151",
                  "bRWWRMk6PCka1MQ%2BzR%2BUYq9eSTJhXpsXlm8c5LG0P3H%2BH5GnREEkURNfqi7HNESpaZxxMafUhDSQoaRDvDC1Aw%3D%3D")
    val = meter.last_gas_read_consumption()
    assert isinstance(val, float)


def test_get_last_meter_read_cost():
    meter = Meter("17baf96d8fdc093b772cf428b74d3151",
                  "bRWWRMk6PCka1MQ%2BzR%2BUYq9eSTJhXpsXlm8c5LG0P3H%2BH5GnREEkURNfqi7HNESpaZxxMafUhDSQoaRDvDC1Aw%3D%3D")
    val = meter.last_gas_read_cost()
    assert isinstance(val, float)


def test_invalid_meter():
    with pytest.raises(MeterError) as err:
        meter = Meter("invalid_energize_id", "invalid_session_id")
        read = meter.last_gas_read()
    assert err is not None
