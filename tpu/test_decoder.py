from random import randrange
import unittest
from unittest import TestCase
from myhdl import *

from decoder import decoder

class TestDecoder(TestCase):

    def testDecoder(self):
        """ Test decoding """

        def test(inst, data, op, selA, selB, selD, en, we, clk):
            en.next = True
            # or(RRR)
            inst.next = intbv('0100001001001100')
            yield delay(10)

            self.assertEqual(op,   intbv('01000'))
            self.assertEqual(selA, intbv(2))
            self.assertEqual(selB, intbv(3))
            self.assertEqual(selD, intbv(1))
            self.assertEqual(en,   True)
            self.assertEqual(we,   True)

            inst.next = intbv('1100111010101010')
            yield delay(10)

            self.assertEqual(op,   intbv('11000'))
            self.assertEqual(selD, intbv('111'))
            self.assertEqual(data, intbv('1010101010101010'))
            self.assertEqual(we,   False)

            raise StopSimulation

        def ClkDrv(clk):
            while True:
                clk.next = not clk
                yield delay(5)

        data = Signal( intbv(0) )
        inst = Signal( intbv(0) )
        op   = Signal( intbv(0) )
        selA = Signal( intbv(0) )
        selB = Signal( intbv(0) )
        selD = Signal( intbv(0) )
        en = Signal(bool())
        we = Signal(bool())
        clk = Signal(bool())

        dut = decoder(inst, data, op, selA, selB, selD, en, we, clk)
        check = test(inst, data, op, selA, selB, selD, en, we, clk)
        clkdrv = ClkDrv(clk)

        sim = Simulation(dut, check, clkdrv)
        sim.run()

if __name__ == '__main__':
    unittest.main()

