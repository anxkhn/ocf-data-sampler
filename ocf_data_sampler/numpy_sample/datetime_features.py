"""Functions to create trigonometric date and time inputs"""

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def _get_date_time_in_pi(
    dt: pd.DatetimeIndex,
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Change the datetimes, into time and date scaled in radians
    """

    day_of_year = dt.dayofyear
    minute_of_day = dt.minute + dt.hour * 60

    # converting into positions on sin-cos circle
    time_in_pi = (2 * np.pi) * (minute_of_day / (24 * 60))
    date_in_pi = (2 * np.pi) * (day_of_year / 365)

    return date_in_pi, time_in_pi


def make_datetime_numpy_dict(datetimes: pd.DatetimeIndex) -> dict:
    """ Make dictionary of datetime features"""

    if datetimes.empty:
        raise ValueError("Input datetimes is empty for 'make_datetime_numpy_dict' function")

    time_numpy_sample = {}

    date_in_pi, time_in_pi = _get_date_time_in_pi(datetimes)

    # Store
    time_numpy_sample["date_sin"] = np.sin(date_in_pi)
    time_numpy_sample["date_cos"] = np.cos(date_in_pi)
    time_numpy_sample["time_sin"] = np.sin(time_in_pi)
    time_numpy_sample["time_cos"] = np.cos(time_in_pi)

    return time_numpy_sample
