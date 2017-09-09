from ..sightstone.drivers import Writer
from time import sleep

with Writer(DAT_A=14, DAT_B=15, CLK=18) as writer:
    data = [1, 0, 1, 0, 1, 0, 1, 0]
    writer.write(data)

    sleep(5)

    data = True
    for _ in range(0,80):
        writer.write_one(data)
        data = not data
        sleep(0.5)