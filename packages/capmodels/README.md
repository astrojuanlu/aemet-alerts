# capmodels

pydantic-xml models to validate CAP (Common Alerting Protocol) files:

https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.html

Not tested against the standard, just some specific files.

## Usage

```python
from pathlib import Path

from capmodels import Alert

cap_filepath = Path(".../data.xml")

Alert.from_xml(cap_filepath.read_text())

print(Alert)
```

## Alternatives

- [capparselib](https://pypi.org/project/capparselib/) scalar elements are XML types, difficult to handle

```
In [4]: from capparselib.parsers import CAPParser

In [5]: with open("data/Z_CAP_C_LEMM_20241101204544_AFAZ690804PRP10223.xml") as fh:
   ...:     data = CAPParser(fh.read())
   ...: 

...

In [8]: data.as_dict()[0]["cap_id"]  # Looks like a string but...
Out[8]: '2.49.0.0.724.0.ES.20241101204544.690804PRP102231730493944'

In [9]: type(data.as_dict()[0]["cap_id"])
Out[9]: lxml.objectify.StringElement
```

- [cap-tools](https://pypi.org/project/cap-tools/) dates XML types, difficult to handle

```
In [13]: from cap_tools.models import Alert

In [14]: from xsdata.formats.dataclass.parsers import XmlParser

In [15]: parser = XmlParser()

In [16]: alert = parser.parse("data/Z_CAP_C_LEMM_20241101204544_AFAZ690804PRP10223.xml", Alert)

...
In [19]: type(alert.identifier)  # At least this is a string...
Out[19]: str

In [20]: alert.sent  # But this is not
Out[20]: XmlDateTime(2024, 11, 1, 20, 45, 44, 0, 0)
```

Other alternatives I haven't tried:

- [cap2geojson](https://pypi.org/project/cap2geojson/) too specific (although I will want to extract the shape at some point)
- [capparser](https://pypi.org/project/capparser/) not a fan of the API
- [capvalidator](https://pypi.org/project/capvalidator/) not a fan of the API
