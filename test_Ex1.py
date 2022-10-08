import unittest

from Ex1 import Ex1

import json

from Elevators import Elevator

root1 = "Ex1_input/Ex1_Buildings/B3.json"


class TestEx1(unittest.TestCase):
    calls = []
    rows = []

    ex = Ex1(calls, rows)

    # load json file
    try:
        with open(root1, "r") as f:
            new_e = {}
            my_d = json.load(f)
            ele_d = my_d["_elevators"]

            c = 0
            for item in ele_d:
                e = Elevator(id=item["_id"], speed=int(item["_speed"]), minFloor=item["_minFloor"],
                             maxFloor=item["_maxFloor"], closeTime=item["_closeTime"], openTime=item["_openTime"],
                             startTime=item["_startTime"], stopTime=item["_stopTime"])
                new_e[c] = e
                c += 1
            ex.elevators = new_e

    except IOError as ex:


    fast = ex.faster_elev()

    def test_faster_elev(self):
        
        self.assertEqual(self.fast, 1)

   
