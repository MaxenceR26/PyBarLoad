"""
By Prasax And Katsu'hi !

Our github : https://www.github.com/Prasax-Dev
            https://www.github.com/Kijusu-Dev
"""

import time

class PyBar:
    def Bar(finish:int = None, end_text:str = None):
        finish = finish
        for i in range(finish):
            i += 1
            print(f"\r{'#'*i}{'-'*(finish-i)}\t||➡ {i}% ||\t", end='')
            time.sleep(1)
        if not end_text:
            print("Finished bar !")
        else:
            print(end_text)

    def LoadingBar(finish:int = None, end_text:str = None):
        finish = finish
        for i in range(finish):
            i += 1
            print(f"\r{'▆' * i}{'-' * (finish - i)}\t||➡ {i}% ||\t", end='')
            time.sleep(1)
        if not end_text:
            print("Finished bar !")
        else:
            print(end_text)

    def StarBar(finish:int = None, end_text:str = None):
        finish = finish
        for i in range(finish):
            i += 1
            print(f"\r{'*' * i}{'-' * (finish - i)}\t||➡ {i}% ||\t", end='')
            time.sleep(1)
        if not end_text:
            print("Finished bar !")
        else:
            print(end_text)

    def PersonalizeBar(finish:int = None, symbol:str = None, end_text:str = None):
        finish = finish
        symbol = symbol
        for i in range(finish):
            i += 1
            print(f"\r{f'{symbol}' * i}{'-' * (finish - i)}\t||➡ {i}% ||\t", end='')
            time.sleep(1)
        if not end_text:
            print("Finished bar !")
        else:
            print(end_text)

    def colors(color: str = None, text: str = None):
        ESCAPE = "\x1b"
        colors = {
            "BLACK": "[30m",
            "RED": "[31m",
            "GREEN": "[32m",
            "YELLOW": "[33m",
            "BLUE": "[34m",
            "PURPLE": "[35m",
            "CYAN": "[36m"
        }
        print(f"{ESCAPE + colors[color] + text}")