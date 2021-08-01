"""
@author: Jim
@project: please_relax
@file: notify.py
@time: 2021/7/30 21:46
@desc:  
    弹出的提醒框
"""

import PySimpleGUI as sg

import config
from relax import Relax


class Notify:

    def __init__(self):
        self.layout = [
            [sg.T("需要休息一下，眼镜要瞎啦~")],
            [sg.B("休息一下", key="relax", focus=True, size=(20, 5))],
            [sg.B("稍后提醒", key="wait"), sg.B("跳过本次", key="skip")]
        ]

    def run(self):
        event, values = sg.Window("强烈提醒", self.layout).read(close=True)
        if event == "wait":
            return config.WAIT_TIME
        elif event == "skip":
            return config.NOTIFY_TIME
        elif event == "relax":
            Relax().run()
            return config.NOTIFY_TIME


if __name__ == '__main__':
    Notify().run()
