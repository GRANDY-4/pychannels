import pychannels as p
import time

func = """print("True")"""

p.mouse.onClick(func)
p.mouse.listen = True
p.mouse.update()

while True:
    time.sleep(0.1)
