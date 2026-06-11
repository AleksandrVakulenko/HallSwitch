# Date: 2026.06.10
# Author: Aleksandr Vakulenko
# 
# This code was generated using DeepSeek and is an 
# automated translation of the corresponding 
# MATLAB R2021b code into Python.
# 
# Licensed after GNU GPL v3
# 

import warnings
from Hall_box import HallBox      # Предполагается, что класс сохранён в файле hall_box.py
from serial.tools import list_ports

def main():
    ports = [port.device for port in list_ports.comports()]
    print(ports)
    com_port = input("Enter COM port num: ");
    com_port = int(com_port)
    
    box = HallBox(com_port)
    cmd = "ABCD"

    try:
        print('Set relay:')
        err_status, err_no, err_comment = box.set_relay(cmd)

        if err_status:
            print(f'ERROR {err_no}:')
            print(err_comment)
        else:
            print('No errors')

    except Exception as e:
        # Закрываем устройство при любой ошибке времени выполнения
        box.close()
        warnings.warn('\nDevice is closed in error section')
        raise   # перевыброс исходного исключения

    # Сюда попадаем только если ошибок не было
    box.close()
    print('\nDevice is closed')

if __name__ == '__main__':
    main()