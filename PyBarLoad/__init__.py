"""
By Prasax And Katsu'hi !

My github : https://www.github.com/Prasax-Dev
"""

import time

class PyBar:
    def Bar(finish:int = None, end_text:str = None):
        i = 0
        count = 0
        finish = finish
        for i in range(finish):
            i += 1
            count += 1
            text = print("■" * i, f'{count} %')
            time.sleep(1)
        if not end_text:
            print("Finished bar !")
        else:
            print(end_text)