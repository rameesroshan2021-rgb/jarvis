import os

import eel

eel.init('www')

os.system('start msedge.exe --app="c:\\Company\\Jarvis\\www\\index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)