from PyLTSpice import SimRunner, SpiceEditor, RawRead
import matplotlib.pyplot as plt
import os

asc_file = "/Users/vladroiban/Documents/Inverter/LTSpice/Simulations/Onsemi/ARCP Half Bridge.asc"


last_modified = 0

while(True):
    runner = SimRunner(output_folder='./temp_batch')

    modified = os.path.getmtime(asc_file)

    if modified != last_modified:
        last_modified = modified

        print("Schematic changed — running simulation...")

        netlist = SpiceEditor(asc_file)
        runner.run_now(netlist)

        raw = RawRead("./temp_batch/ARCP Half Bridge_1.raw")

        time = raw.get_trace("time").get_wave()
        vout = raw.get_trace("V(n001)").get_wave()


        plt.plot(time, vout)
        plt.xlabel("Time (s)")
        plt.ylabel("V(n001) (V)")
        plt.grid()
        plt.show()
    input()