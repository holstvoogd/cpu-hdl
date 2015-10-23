from myhdl import *

def decoder(inst, data, op, selA, selB, selD, en, we, clk):
    """ A instuction decoder for the TPU.

    I/O pins:
    inst : instruction in
    data : immediate data out
    op   : ALU opperation
    selA : rA select
    selB : rB select
    selD : rD select
    en   : enable
    we   : write enable
    clk  : clock

    """

    @always(clk.posedge)
    def logic():
        if en:
            selA.next = inst[8:5]
            selB.next = inst[5:2]
            selD.next = inst[12:9]
            data.next = concat(inst[8:0], inst[8:0])
            op.next   = concat(inst[16:12], inst[8])
            we.next   = not bin(inst[16:12], 4) in ['0111', '1100', '1101']

    return logic
