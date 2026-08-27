import keyboard as k
import inspect

keybinds = {}
triggersl = {}
listen = None
func = None

class channels:
    def assign(key, func):
        context = inspect.currentframe().f_back.f_globals
        keybinds[key] = (func, context)
    
    def unassign(key):
        keybinds[key] = None
    
    def read(key):
        return keybinds[key][0]

    def listen():
        global listen
        while listen == True:
            event = k.read_event()

            if event.event_type == "down":
                if event.name in keybinds:
                    code, context = keybinds[event.name]
                    exec(code, context)

    def setListen(bl):
        global listen
        listen = bl
        channels.listen()

    def waitFor(key):
        k.wait(key)
        code, context = keybinds[key]
        exec(code, context)

    def readFunc():
        return func

    def clear():
        global keybinds
        keybinds = {}

class triggers:
    def assign(name, code):
        context = inspect.currentframe().f_back.f_globals
        triggersl[name] = (code, context)

    def read(name):
        return triggersl[name][0]

    def trigger(name):
        if name not in triggersl:
            raise KeyError(f"Trigger '{name}' does not exist")

        if triggersl[name] is None:
            return

        code, context = triggersl[name]
        exec(code, context)

    def unassign(name):
        if name in triggersl:
            del triggersl[name]

    def clear():
        global triggersl
        triggersl = {}

    def returnValue(name):
        return exec(triggersl[name])
