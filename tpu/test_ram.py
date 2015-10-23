from random import randrange
import unittest
from unittest import TestCase
from myhdl import *

from ram import ram

class TestTpuRam(TestCase):

    def testRam(self):
        """ Test ram """

        def test(addr, dataI, dataO, we, clk):
            we.next = True
            addr.next = intbv('110101')
            dataI.next = intbv('1000100010001000')
            yield delay(10)

            addr.next = intbv('110111')
            dataI.next = intbv('1001100110011001')
            yield delay(10)

            we.next = False
            addr.next = intbv('110101')
            yield delay(10)
            self.assertEqual(dataO, intbv('1000100010001000'))

            addr.next = intbv('110111')
            yield delay(10)
            self.assertEqual(dataO, intbv('1001100110011001'))

            raise StopSimulation

        def ClkDrv(clk):
            while True:
                clk.next = not clk
                yield delay(5)

        addr  = Signal( intbv(0) )
        dataI = Signal( intbv(0) )
        dataO = Signal( intbv(0) )
        we = Signal(bool())
        clk = Signal(bool())

        dut    = ram(addr, dataI, dataO, we, clk)
        check  = test(addr, dataI, dataO, we, clk)
        clkdrv = ClkDrv(clk)

        sim = Simulation(dut, check, clkdrv)
        sim.run()

if __name__ == '__main__':
        unittest.main()

