# PyChannels

PyChannels is a lightweight Python library for connecting inputs and triggers to executable Python code.

## The Channel Concept

A **Channel** is a link between a keybind (the key used to start the code) and a Container (the code).

```text
Keybind ───── Channel ───── Container
 "space"                    Python code
