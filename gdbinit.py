from gdb import *
import sys
import os

class Bindog(Command):
  def __init__(self):
    super(Bindog, self).__init__("bindog", COMMAND_USER)

    # https://stackoverflow.com/questions/15514593/importerror-no-module-named-when-trying-to-run-python-script
    sys.path.append(os.path.expanduser(os.path.dirname(__file__)))
  
  def invoke(self, arg, from_tty):
    exec(open(arg + '.py').read())

Bindog()
