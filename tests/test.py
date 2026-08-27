import pychannels as p

p.func = """
print("test success")
"""

p.channels.readFunc()

p.channels.assign("space", p.func)

print(p.channels.read("space"))

p.channels.setListen(True)
