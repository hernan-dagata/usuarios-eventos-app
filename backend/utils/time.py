from datetime import datetime
import pytz


COLOMBIA_TZ = pytz.timezone("America/Bogota")


def now_colombia():
    return datetime.now(COLOMBIA_TZ).isoformat()