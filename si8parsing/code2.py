from django.db import transaction
from .models import Folder, File
import os
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from .code.parsing import openfilesi8
from si8device.models import PollResult, Register
from django.utils import timezone
from celery import shared_task

# вызывать 1  раз в минуту
# ищет в папке файлы с расширением si8,
# если файла с таким хешем нет, то добавляет в базу - модель File
@shared_task
def findfile():
    folders = Folder.objects.filter(enable=True)
    for folder in folders:
        trees = os.walk(folder.path)
        for tree in trees:
            # print(tree)
            for file in tree[2]:
                if file.endswith('.SI8') is True:
                    name = file
                    path = tree[0]+'/'
                    hash = get_hash_md5(path, name)

                    try:
                        File.objects.get(hash=hash)
                    except ObjectDoesNotExist:
                        f = File(name=name, path=path, parsing_status=0, hash=hash)
                        f.save()


def get_hash_md5(path, filename):
    with open(path+filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


# {'value': 51.8, 'now_date': datetime.datetime(2016, 12, 26, 7, 30), 'id_si8': 1}
def parsing_si8(pk=None):
    if id is None:
        files = File.objects.filter(parsing_status=0)
    else:
        files = File.objects.filter(id=pk)
    for file in files:
        try:
            file.parsing_status = 2
            file.save()
            ds = openfilesi8(file.path, file.name)
            for d in ds:
                logtime =timezone.now()
                register_addr = d['id_si8']
                now_date = d['now_date'].strftime('%m/%d/%Y %H:%M')
                value = d['value']
                reg = Register.objects.get(register_addr=register_addr)
                p = PollResult(pollresult_register=reg, pollresult_time=now_date, pollresult_value=value)
                p.save()
                ss = ('%s - %s' % (logtime.second, timezone.now().second))
                pass
            file.parsing_status = 1
            file.save()
        except BaseException as error:
            print('An exception occurred in parsing_si8: {}'.format(error))
