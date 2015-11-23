from traceback import print_exc
from assembler import (
  Ior_imm,
  Lsl_imm,
  Mov_imm,
  Store_word,
  )
from display import initialize_screen, ScreenRAMMixin, DISPLAY_START
from risc import ByteAddressed32BitRAM, clock, LEDs, RISC


def HIGH(i):
  return i >> 16


def LOW(i):
  return i & 0xFFFF


def MoveImmediateWordToRegister(reg, word):
  return (
    Mov_imm(reg, HIGH(word)),
    Lsl_imm(reg, reg, 16),
    Ior_imm(reg, reg, LOW(word)),
    )


a = 0
b = 1

program = (
  MoveImmediateWordToRegister(a, 0xaaaaaaaa) +
  MoveImmediateWordToRegister(b, DISPLAY_START) +
  tuple(
    Store_word(a, b, n * 4) for n in range(24575)
    )
  )


class Memory(ScreenRAMMixin, ByteAddressed32BitRAM):
  pass


screen = initialize_screen()
memory = Memory()
memory.set_screen(screen)
risc_cpu = RISC(program, memory)
risc_cpu.io_ports[0] = clock()
risc_cpu.io_ports[4] = LEDs()


def cycle():
  try:
    risc_cpu.cycle()
  except:
    print_exc()
    risc_cpu.dump_ram()
##  risc_cpu.view()


print 'cycle()'
for _ in range(len(program)):
  cycle()
