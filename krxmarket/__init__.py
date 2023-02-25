# -*- coding: utf-8 -*-
import logging


from .common.types import KrxCorp

from .krx.api import (
    get_krx_all,
    get_stock_market_list,
    get_trading_halt_list
)

__all__ = (
    "KrxCorp",
    "get_krx_all",
    "get_stock_market_list",
    "get_trading_halt_list"
)


# Attach a NullHandler to the top level logger by default
# https://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library

logging.getLogger("krxmarket").addHandler(logging.NullHandler())