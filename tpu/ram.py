from myhdl import *

def ram(addr, dataI, dataO, we, clk, WORD_SIZE = 16, ROWS = 64):
    """ A basic RAM module for the TPU.

    I/O pins:
    clk   : clock
    addr  : address
    dataI : data in
    dataO : data out
    we    : write enable

    """

    store = [Signal(intbv(0)[WORD_SIZE:]) for i in range(ROWS)]

    @always(clk.posedge)
    def logic():
        if we:
            store[addr[6:0]].next = dataI
        else:
            dataO.next = store[addr[6:0]]

    return logic
