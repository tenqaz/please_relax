"""
@author: Jim
@project: please_relax
@file: main.py
@time: 2021/7/30 21:36
@desc:

"""
import logging
import time

import pyautogui as pag

import config
from notify import Notify


def check_position_run(ret_time):
    """ 检查鼠标位置来判断时间

    如果鼠标静止不动，则停止计时

    """
    end_time = time.time() + ret_time
    x, y = pag.position()
    while time.time() < end_time:
        time.sleep(config.LEAVE_WAIT_TIME)

        after_x, after_y = pag.position()
        if after_x == x and after_y == y:
            end_time += config.LEAVE_WAIT_TIME
        else:
            x, y = after_x, after_y


def main():
    time.sleep(config.NOTIFY_TIME)

    while True:
        ret_time = Notify().run()
        if ret_time is None:
            break

        check_position_run(ret_time)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
