import os
from gdb import *
from datetime import datetime
from pathlib import Path

class CommandFactory:
  breakpoints = []

  def __init__(self, executable):
    self.executable = executable

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    dirpath = '/tmp/' + self.executable + '.' + now
    inpath  = dirpath + '/stdin'
    outpath = dirpath + '/stdout'

    os.makedirs(dirpath)
    Path(inpath).touch()
    Path(outpath).touch()
    self.stdin  = open(inpath, 'w+b')
    self.stdout = open(outpath, 'rb')

    execute('set resolve-heap-via-heuristic on')
    # Delete all existing breakpoints
    execute('delete')

  def run(self):
    execute('run ' + self.executable + ' < ' + self.stdin.name + ' > ' + self.stdout.name)

  def b(self, spec):
    self.breakpoints.append(Breakpoint(spec))

  def c(self):
    execute('continue')

  def recv(self):
    return self.stdout.read()

  def send(self, bs):
    self.stdin.write(bs)
    self.stdin.flush()

  def sendline(self, text):
    self.send(text + b'\n')
