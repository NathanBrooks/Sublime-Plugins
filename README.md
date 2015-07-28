# Sublime-Plugins
plugins I made for sublime text


#CurSave
saves cursor locations in memory to be loaded at a later time

key binding:
~~~ Json
    { "keys": ["ctrl+shift+y"], "command": "cur_save", "args": {"forward": false} },
    { "keys": ["ctrl+shift+o"], "command": "cur_load" }
~~~

add above to key bindings and the .py to the user package directory. 

The forward argument will determine if a selected area will use the front or the back end of the selection for the point to add.
