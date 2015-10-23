from myhdl import *

def control_unit(state, aluop, reset, clk):
    """ A pipeline control unit for the TPU.

    I/O pins:

    state : state output [decode, regread, alu, regwrite]
    aluop : current ALU opperation
    reset : Reset cpu
    clk   : clock

    """

    @always(clk.posedge)
    def logic():


    return logic
