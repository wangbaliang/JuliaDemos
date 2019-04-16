#!/usr/bin/env python3
# Time: 2019/4/15 16:35

__author__ = 'wanggangshan@jd.com'


import os
import sys
import time
import pandas as pd

from functools import wraps


_KEYS = ['A' + str(i) for i in range(107)]
_VALUES = ['str'] + ['int8' for i in range(106)]
_DTYPE = dict(zip(_KEYS, _VALUES))


_CSV_PATH_LOG = '_DATA_USE'

with open(_CSV_PATH_LOG, 'r') as f:
    _CSV_PATH = f.read().strip()
# _CSV_PATH = 'data/test.csv'

_CSV_PATH_WRITE = 'test_1g_write.csv'


def log_func_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        use_time = end - start
        print('use time(s): %s\n' % use_time)
        return res
    return wrap


@log_func_time
def log_read_csv(dtype=None):
    print('log read csv ==========================')
    df = pd.read_csv(_CSV_PATH, dtype=dtype)
    print('df shape: %s %s' % df.shape)
    print('use mem(G): %s' % (sys.getsizeof(df)/1024**3))
    return df

@log_func_time
def log_write_csv(df):
    print('write csv ==========================')
    df.to_csv(_CSV_PATH_WRITE, encoding="utf_8", index=False, header=True)

if __name__ == '__main__':
    # Usage: python test_pandas_csv.py [option]
    print('argv: ', sys.argv)
    if len(sys.argv) > 1:
        print('run with dtype\n')
        # run with dtype
        df = log_read_csv(dtype=_DTYPE)
    else:
        print('run with not dtype\n')
        df = log_read_csv()

    log_write_csv(df)
    os.remove(_CSV_PATH_WRITE)
