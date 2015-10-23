from myhdl import *

# PC operations
PCU_OP_NOP    = intbv("00")
PCU_OP_INC    = intbv("01")
PCU_OP_ASSIGN = intbv("10")
PCU_OP_RESET  = intbv("11")

def pc_unit(pcI, pcO, op, clk):
    """ A PC unit for the TPU.

    I/O pins:

    pcI   : Program counter input
    op    : Program counter operation
    pcO   : Program counter output
    clk   : clock

    """

    pc = intbv(0)[15:]

    @always(clk.posedge)
    def logic():
        if op != PCU_OP_NOP:
            # noop
            if op == PCU_OP_INC:
                pc.next = pc + 1
            elif op == PCU_OP_ASSIGN
                pc.next = pcI
            elif op == PCU_OP_RESET
                pc.next = intbv(0)
        pcO.next = pc

    return logic
