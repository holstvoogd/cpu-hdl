from random import randrange
import unittest
from unittest import TestCase
from myhdl import *

from register import register

class TestTpuRegister(TestCase):

    def testRegister(self):
        """ Test write & read for the all registers """

        def test(dataA, dataB, dataD, selA, selB, selD, en, we, clk):
            registers = {}
            # Write some data
            for i in range(8):
                en.next = True
                we.next = True
                data = randrange(2**16)

                selD.next = int(i)
                dataD.next = data
                registers[i] = hex(data)
                yield delay(10)

            # aaaaand read it back
            for i, data in registers.iteritems():
                we.next = False
                selA.next = i
                selB.next = 7 - i
                yield delay(10)

                self.assertEqual(selA, i)
                self.assertEqual(hex(dataA), data)
                self.assertEqual(selB, 7 - i)
                self.assertEqual(hex(dataB), registers[7 - i])

            # Check we=false -> no change
            i = int(randrange(8))
            data = randrange(2**16)
            selD.next = i
            dataD.next = data
            yield delay(10)

            selA.next= i
            yield delay(10)

            self.assertNotEqual(dataA, data)

            raise StopSimulation

        def ClkDrv(clk):
            while True:
                clk.next = not clk
                yield delay(5)

        dataA = Signal( intbv(0) )
        dataB = Signal( intbv(0) )
        dataD = Signal( intbv(0) )
        selA = Signal( intbv(0) )
        selB = Signal( intbv(0) )
        selD = Signal( intbv(0) )
        en = Signal(bool())
        we = Signal(bool())
        clk = Signal(bool())

        dut = register(dataA, dataB, dataD, selA, selB, selD, en, we, clk)
        check = test(dataA, dataB, dataD, selA, selB, selD, en, we, clk)
        clkdrv = ClkDrv(clk)

        sim = Simulation(dut, check, clkdrv)
        sim.run()

if __name__ == '__main__':
        unittest.main()

