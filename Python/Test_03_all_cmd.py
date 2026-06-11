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
from Hall_box import HallBox      # класс из предыдущего ответа
from serial.tools import list_ports

def main():

    ports = [port.device for port in list_ports.comports()]
    print(ports)
    com_port = input("Enter COM port num: ");
    com_port = int(com_port)
    
    box = HallBox(com_port)

    # Таблица тестов: (команда, ожидаемый код ошибки или None, если ошибки не должно быть)
    test_table = [
        # Блок с перестановками букв A,B,C,D
        ("ABCD", None),
        ("ABDC", None),
        ("ACBD", None),
        ("ACDB", None),
        ("ADBC", None),
        ("ADCB", None),
        ("BACD", None),
        ("BADC", None),
        ("BCAD", None),
        ("BCDA", None),
        ("BDAC", None),
        ("BDCA", None),
        ("CABD", None),
        ("CADB", None),
        ("CBAD", None),
        ("CBDA", None),
        ("CDAB", None),
        ("CDBA", None),
        ("DABC", None),
        ("DACB", None),
        ("DBAC", None),
        ("DBCA", None),
        ("DCAB", None),
        ("DCBA", None),

        # Блок с цифрами 1,2,3,4
        ("1234", None),
        ("1243", None),
        ("1324", None),
        ("1342", None),
        ("1423", None),
        ("1432", None),
        ("2134", None),
        ("2143", None),
        ("2314", None),
        ("2341", None),
        ("2413", None),
        ("2431", None),
        ("3124", None),
        ("3142", None),
        ("3214", None),
        ("3241", None),
        ("3412", None),
        ("3421", None),
        ("4123", None),
        ("4132", None),
        ("4213", None),
        ("4231", None),
        ("4312", None),
        ("4321", None),

        # Один 'X' на каждой позиции
        ("XBCD", None),
        ("AXCD", None),
        ("ABXD", None),
        ("ABCX", None),

        # Два 'X'
        ("XXCD", None),
        ("XBXD", None),
        ("XBCX", None),
        ("AXXD", None),
        ("AXCX", None),
        ("ABXX", None),

        # Три 'X'
        ("XXXD", None),
        ("XXCX", None),
        ("XBXX", None),
        ("AXXX", None),

        # Четыре 'X'
        ("XXXX", None),

        # Комбинации цифр и X
        ("X234", None),
        ("1X34", None),
        ("12X4", None),
        ("123X", None),
        ("XX34", None),
        ("X2X4", None),
        ("X23X", None),
        ("1XX4", None),
        ("1X3X", None),
        ("12XX", None),
        ("XXX4", None),
        ("XX3X", None),
        ("X2XX", None),
        ("1XXX", None),
        ("XXXX", None),

        # Ошибка 301 – недопустимый символ (цифра или буква не A,B,C,D)
        ("1BCD", 301),
        ("2BDC", 301),
        ("3CBD", 301),
        ("4CDB", 301),
        ("A2BC", 301),
        ("AD12", 301),
        ("B4CD", 301),
        ("B3DC", 301),
        ("B212", 301),
        ("43AC", 301),
        ("BD2A", 301),

        # Ошибка 302 – символ повторяется (не 'X')
        ("2243", 302),
        ("3324", 302),
        ("4342", 302),
        ("1223", 302),
        ("1412", 302),
        ("2434", 302),
        ("2343", 302),
        ("2212", 302),
        ("4313", 302),
        ("2421", 302),
        # Спецсимволы / и . (также ошибка 301)
        ("//.*", 301),
        ("4317", 301),
        ("0223", 301),

        # Повторяющиеся буквы (302)
        ("CACD", 302),
        ("CADD", 302),
        ("ABAD", 302),
        ("CBBA", 302),
        ("CDCB", 302),
        ("CBBA", 302),
        ("DABA", 302),
        ("AACB", 302),
        ("DCAC", 302),
        ("DBBC", 302),

        # Повторяющиеся цифры (302)
        ("3134", 302),
        ("3144", 302),
        ("1214", 302),
        ("3221", 302),
        ("3411", 302),
        ("3221", 302),
        ("4121", 302),
        ("1132", 302),
        ("4313", 302),
        ("4223", 302),

        # Неправильная длина (200)
        ("A", 200),
        ("AB", 200),
        ("ABC", 200),
        ("CBCDE", 200),
        ("ABCDD", 200),
        ("", 200),
        ("rgddj", 200),

        # Неправильные звёздные команды (ошибки 103, 102, 101)
        ("*IDN??", 103),
        ("*", 103),
        ("*12", 103),
        ("*12345", 103),
        ("*1234567", 103),
        ("*1234", 102),
        ("*IDD?", 102),
        ("*    ", 102),
        ("*ABCD", 102),
        ("*123", 101),
        ("*RSS", 101),
        ("*   ", 101),
        ("*ABC", 101),
    ]

    n = len(test_table)
    status_arr = [False] * n
    results = []          # будет хранить (cmd, expected, got_err_no) для вывода в случае ошибок

    try:
        for i, (cmd, expected) in enumerate(test_table, start=1):
            print(f"{i}/{n} : {cmd}")
            _, err_no, _ = box.set_relay(cmd)

            # Формируем строковое представление для вывода (пусто -> [])
            err_no_str = str(err_no) if err_no is not None else '[]'
            exp_str = str(expected) if expected is not None else '[]'
            print(f"    <{err_no_str}> = <{exp_str}>")

            # Логика сравнения: оба пустые -> успех, иначе числовое совпадение
            if err_no is None and expected is None:
                status = True
            else:
                status = (err_no == expected)

            status_arr[i-1] = status
            results.append((cmd, expected, err_no))

            if status:
                print("    PASS")
            else:
                print("    FAIL")

    except Exception as e:
        box.close()
        warnings.warn('\nDevice is closed in error section')
        raise

    box.close()
    print('\nDevice is closed')

    # Итоговый отчёт
    if any(not s for s in status_arr):
        print("\nFailed tests:")
        for idx, (cmd, expected, got) in enumerate(results):
            if not status_arr[idx]:
                exp_str = str(expected) if expected is not None else '[]'
                got_str = str(got) if got is not None else '[]'
                print(f"  {cmd}  expected:{exp_str}  got:{got_str}")
    else:
        print("All tests passed.")

if __name__ == '__main__':
    main()