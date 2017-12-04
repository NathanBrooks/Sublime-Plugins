# Sublime-Plugins
plugins I made for sublime text


#CurSave
saves cursor locations in memory to be loaded at a later time

key binding:
~~~ Json
    { "keys": ["ctrl+shift+y"], "command": "cur_save", "args": {"forward": false} },
    { "keys": ["ctrl+shift+o"], "command": "cur_load", "args": {"dropCursor": true} }
~~~

add above to key bindings and the .py to the user package directory. 

The _forward_ argument will determine if a selected area will use the front or the back end of the selection for the point to add.

The _dropCursor_ argument for loading will determine if you keep the the current active cursors before loading in the saved ones.

#DateConversion

key binding:
~~~ Json
    { "keys": ["ctrl+alt+k"], "command": "unix_time_convert" }
~~~

add above to key bindings and the .py to the user package directory
