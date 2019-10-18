This is a utility package to interact with a PSE&G gas meter

Pseg calls the API of the PSE&G gas meter to return the current energy usage.

It requires the meter's energize id and a session id.
You can find this information as cookies after logging into your PSE&G customer account at https://pseg.com/.

Example usage:

```
from pseg import Meter

meter = Meter("17baf96d8fdc0abcded2cf428b74d3151", "bRWWRMk6PCka1MQ%2BabcedpaZxxMafUhDSQoaRDvDC1Aw%3D%3D")
gas_consumption_therms = meter.last_gas_consumption_read()
```
