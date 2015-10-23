from myhdl import *

def register(dataA, dataB, dataD, selA, selB, selD, en, we, clk, WORD_SIZE = 16, COUNT = 8):
    """ A basic register file for the TPU.

    I/O pins:
    clk   : clock
    en    : enable
    dataA : rA data out
    dataB : rB data out
    dataD : rD data in
    selA  : rA select
    selB  : rB select
    selD  : rD select
    we    : write enable

    """

    registers = [Signal(intbv(0)[WORD_SIZE:]) for i in range(COUNT)]

    @always(clk.posedge)
    def logic():
        if en:
            dataA.next = registers[int(selA)]
            dataB.next = registers[int(selB)]
            if we:
                registers[int(selD)].next = dataD

    return logic
