import keyboard as k
import inspect
import mouse as m

keybinds = {}
triggersl = {}
listen = False
func = None


class channels:
    def assign(key, func):
        context = inspect.currentframe().f_back.f_globals
        keybinds[key] = (func, context)

    def unassign(key):
        if key in keybinds:
            del keybinds[key]

    def read(key):
        if key not in keybinds:
            raise KeyError(f"Key '{key}' does not exist")

        return keybinds[key][0]

    def listen(exclude=None):
        global listen

        if exclude is None:
            exclude = []

        while listen == True:
            event = k.read_event()

            if event.event_type == "down":
                if event.name in keybinds:
                    if event.name not in exclude:
                        if keybinds[event.name] is not None:
                            code, context = keybinds[event.name]
                            exec(code, context)

    def setListen(bl, exclude=None):
        global listen

        listen = bl

        if exclude is None:
            exclude = []

        if bl == True:
            channels.listen(exclude)

    def waitFor(key):
        if key not in keybinds:
            raise KeyError(f"Key '{key}' does not exist")

        if keybinds[key] is None:
            return

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
        if name not in triggersl:
            raise KeyError(f"Trigger '{name}' does not exist")

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
        if name not in triggersl:
            raise KeyError(f"Trigger '{name}' does not exist")

        return triggersl[name][0]


class DEPENDENTTOOLS:
    def runSavedClickCode(prm):
        if prm is not None:
            exec(prm)


class mouse:
    listen = False
    clickCode = None
    clickHook = None

    def onClick(func):
        mouse.clickCode = func

    def update():
        if mouse.listen and mouse.clickHook is None:
            mouse.clickHook = m.on_click(
                lambda event: DEPENDENTTOOLS.runSavedClickCode(mouse.clickCode)
            )

        elif not mouse.listen and mouse.clickHook is not None:
            m.unhook(mouse.clickHook)
            mouse.clickHook = None
