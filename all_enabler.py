#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from loguru import logger

from cells_data import cells_data
from enabler import enabler

from settings import (
        ENV,
    )

def all_enabler(time_=None):
    '''
    La finalidad de esta función es habilitar a todas las celdas.
    Con excepción de aquellas cuyo nombre haga match con el pattern
    _MM_
    '''
    logger.debug(f'ENV {ENV}')

    if not time_:
        logger.info(f'time_ {time_}')
        return

    df = cells_data(time_=time_)
    cellnames = df[~df['CELLNAME'].str.contains("_MM_")]['CELLNAME'].drop_duplicates().tolist()

    enabler(cellnames=cellnames)


def main():
    time_ = datetime.datetime.now()
    all_enabler(time_=time_)


if __name__ == '__main__':
    main()
