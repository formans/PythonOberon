import sys
import ORPX, ORSX


text = open('Amodule.Mod.txt').read()
try:
  ORPX.Compile(text)
except:
  print >> sys.stderr
  print >> sys.stderr, '-' * 40
  print >> sys.stderr, 'Error near', ORSX._pos
  print >> sys.stderr, text[ORSX._pos - 20:ORSX._pos],
  print >> sys.stderr, '^^Err^^',
  print >> sys.stderr, text[ORSX._pos:ORSX._pos + 20]
  print >> sys.stderr, '-' * 40
  raise
