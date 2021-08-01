"""
@author: Jim
@project: please_relax
@file: relax.py
@time: 2021/7/30 23:07
@desc:  
    正在休息中的提醒框
"""
import PySimpleGUI as sg

import config


class Relax:

    def __init__(self):
        self.relax_second = config.WAIT_TIME
        self.layout = [
            [sg.T("正在休息中..还有:"), sg.T(self.relax_second, key="relax_second"), sg.T("秒")],
            [sg.B("取消休息", key="cancel")]
        ]

    def run(self):

        w = sg.Window("休息一下", self.layout)
        while True:
            if self.relax_second == 0:
                break

            event, values = w.read(timeout=1000)

            if event == "cancel":
                break

            self.relax_second -= 1
            w["relax_second"].update(self.relax_second)

        w.close()


if __name__ == '__main__':
    Relax().run()
