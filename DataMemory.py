from myhdl import *


@block
def DataMemory(clk, DAddr, DataIn, DataMemR, DataMemW, DataOut, DEBUG=False):

    memory = [Signal(intbv(0)[32:]) for i in range(64)]
    memory[0] = intbv(0x00000009)[32:]
    memory[1] = intbv(0xfffffff8)[32:]
    memory[2] = intbv(0x00000007)[32:]
    memory[3] = intbv(0x00000006)[32:]

    @always(DataMemR, DAddr)
    def read_data():
        if DEBUG:
            print('-> Enter dataMem read data')
            print('DAddr:' + str(DAddr), 'DataIn:' + str(DataIn),
                  'DataMemR:' + str(DataMemR))

        if DataMemR:
            DataOut.next = memory[DAddr]

        if DEBUG:
            print('<- Exit dataMem read data\n')

    @always(clk.negedge)  # , DAddr, DataIn
    def write_data():
        if DEBUG:
            print('-> Enter dataMem write data')
            print('DAddr:' + str(DAddr), 'DataIn:' + str(DataIn),
                  'DataMemW:' + str(DataMemW))

        if DataMemW:
            memory[DAddr].next = DataIn

        if DEBUG:
            print('<- Exit dataMem write data\n')

    return read_data, write_data
