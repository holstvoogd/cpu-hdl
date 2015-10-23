from myhdl import *

def alu(dataA, dataB, dataI, dataR, weI, weO, op, pc, br, en, clk):
    """ A alu for the TPU.

    I/O pins:
    dataA : dataA In
    dataB : dataB In
    dataI : Immediate data
    dataR : Result data out
    weI   : Write enabled for dataD
    weO   : Write enable out (to reg)
    op    : ALU opperation
    pc    : Program Counter
    br    : Should branch out
    en    : enable
    clk   : clock

    """

    @always(clk.posedge)
    def logic():


    return logic
