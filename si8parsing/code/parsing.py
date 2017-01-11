# from datetime import datetime
from django.utils import timezone
import random
import struct
# import datetime
import os
import logging


def openfilesi8(foldeder, filename):
    logtime = timezone.now()
    # foldeder = 'data/'
    # filename = '010913.SI8'
    with open(foldeder + filename, "rb") as f:
        count_line = 0
        count_si8 = 1
        bufs = []
        while count_si8:
            count_si8 = int.from_bytes(f.read(1), byteorder='big')
            hour = int.from_bytes(f.read(1), byteorder='big')
            minute = int.from_bytes(f.read(1), byteorder='big')
            if minute >= 60:
                minute = 59
            # print("Счетчиков = %d, Время %d:%d" % (count_si8, hour, minute))
            for i in range(1, count_si8 + 1, 1):
                # addr = f.read(1)
                addr = int.from_bytes(f.read(1), byteorder='big')
                data = f.read(4)
                speed = struct.unpack('f', data)[0]
                # print("Счетчик = %d, Скорость=%.2f" % (addr, speed))
                d1 = timezone.datetime.strptime(filename[0:6], '%d%m%y')
                dstart = d1.replace(hour=7, minute=30)
                date = d1.replace(hour=hour, minute=minute)
                if date < dstart:
                    delta = timezone.timedelta(days=1)  # дельта в 1 дня
                    date = date + delta
                if addr != 0:
                    try:
                        # print("Дата = %s, Счетчик = %d, Скорость=%.2f" % (date, addr, speed))
                        count_line += 1
                        # 30-01-1987 13:12
                        datestr = date.strftime('%d-%m-%Y %H:M')
                        buf = {'id_si8': addr, 'value': round(speed, 2), 'now_date': date, 'datestr': datestr}
                        bufs.append(buf)

                        # time.sleep(1)
                    except Exception:
                        pass
                        # print("Error - Дата = %s, Счетчик = %d, Скорость=%.2f" % (date, addr, speed))
                        # print("error")
    # print("Всего полей =  %s" % count_line)
    ss = ('%s - %s' % (logtime.second, timezone.now().second))
    return bufs
    # return {'bufs': bufs, 'counter': count_line}
