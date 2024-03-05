# Copyright 2024 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import unittest

from dash import dash_table

import employee_scheduling
import utils
from app import disp_initial_sched


class TestDemo(unittest.TestCase):
    # Check that initial schedule created is the right size
    def test_initial_sched(self):
        num_employees = 12

        sched_df = disp_initial_sched(num_employees, None).data

        self.assertEqual(len(sched_df), num_employees)

    # Check that CQM created has the right number of variables
    def test_cqm(self):
        num_employees = 12

        sched_df = disp_initial_sched(num_employees, None).data
        shifts = list(sched_df[0].keys())
        shifts.remove("Employee")
        availability = utils.availability_to_dict(sched_df, shifts)

        cqm = employee_scheduling.build_cqm(
            availability, shifts, 1, 6, 5, 16, True, False, 6
        )

        self.assertEqual(len(cqm.variables), num_employees * len(shifts))

    def test_samples(self):
        shifts = [str(i + 1) for i in range(5)]

        # Make every employee available for every shift
        availability = {
            "A-Mgr": [1] * 5,
            "B-Mgr": [1] * 5,
            "C": [1] * 5,
            "D": [1] * 5,
            "E": [1] * 5,
            "E-Tr": [1] * 5,
        }

        cqm = employee_scheduling.build_cqm(
            availability, shifts, 1, 6, 5, 16, True, False, 6
        )

        feasible_sample = {
            "A-Mgr_1": 0.0,
            "A-Mgr_2": 0.0,
            "A-Mgr_3": 1.0,
            "A-Mgr_4": 1.0,
            "A-Mgr_5": 1.0,
            "B-Mgr_1": 1.0,
            "B-Mgr_2": 1.0,
            "B-Mgr_3": 0.0,
            "B-Mgr_4": 0.0,
            "B-Mgr_5": 0.0,
            "C_1": 1.0,
            "C_2": 1.0,
            "C_3": 1.0,
            "C_4": 1.0,
            "C_5": 1.0,
            "D_1": 1.0,
            "D_2": 1.0,
            "D_3": 1.0,
            "D_4": 1.0,
            "D_5": 1.0,
            "E-Tr_1": 1.0,
            "E-Tr_2": 1.0,
            "E-Tr_3": 1.0,
            "E-Tr_4": 1.0,
            "E-Tr_5": 1.0,
            "E_1": 1.0,
            "E_2": 1.0,
            "E_3": 1.0,
            "E_4": 1.0,
            "E_5": 1.0,
        }

        infeasible_sample = {
            "A-Mgr_1": 1.0,
            "A-Mgr_2": 1.0,
            "A-Mgr_3": 1.0,
            "A-Mgr_4": 1.0,
            "A-Mgr_5": 1.0,
            "B-Mgr_1": 1.0,
            "B-Mgr_2": 1.0,
            "B-Mgr_3": 1.0,
            "B-Mgr_4": 1.0,
            "B-Mgr_5": 1.0,
            "C_1": 1.0,
            "C_2": 1.0,
            "C_3": 1.0,
            "C_4": 1.0,
            "C_5": 1.0,
            "D_1": 1.0,
            "D_2": 1.0,
            "D_3": 1.0,
            "D_4": 1.0,
            "D_5": 1.0,
            "E-Tr_1": 1.0,
            "E-Tr_2": 1.0,
            "E-Tr_3": 1.0,
            "E-Tr_4": 1.0,
            "E-Tr_5": 1.0,
            "E_1": 1.0,
            "E_2": 1.0,
            "E_3": 1.0,
            "E_4": 1.0,
            "E_5": 1.0,
        }

        self.assertTrue(cqm.check_feasible(feasible_sample))
        self.assertFalse(cqm.check_feasible(infeasible_sample))

    def test_build_from_sample(self):
        shifts = [str(i + 1) for i in range(5)]
        employees = ["A-Mgr", "B-Mgr", "C", "D", "E", "E-Tr"]

        # Make every employee available for every shift
        availability = {
            "A-Mgr": [1] * 5,
            "B-Mgr": [1] * 5,
            "C": [1] * 5,
            "D": [1] * 5,
            "E": [1] * 5,
            "E-Tr": [1] * 5,
        }

        sample = {
            "A-Mgr_1": 0.0,
            "A-Mgr_2": 0.0,
            "A-Mgr_3": 1.0,
            "A-Mgr_4": 1.0,
            "A-Mgr_5": 1.0,
            "B-Mgr_1": 1.0,
            "B-Mgr_2": 1.0,
            "B-Mgr_3": 0.0,
            "B-Mgr_4": 0.0,
            "B-Mgr_5": 0.0,
            "C_1": 1.0,
            "C_2": 1.0,
            "C_3": 1.0,
            "C_4": 1.0,
            "C_5": 1.0,
            "D_1": 1.0,
            "D_2": 1.0,
            "D_3": 1.0,
            "D_4": 1.0,
            "D_5": 1.0,
            "E-Tr_1": 1.0,
            "E-Tr_2": 1.0,
            "E-Tr_3": 1.0,
            "E-Tr_4": 1.0,
            "E-Tr_5": 1.0,
            "E_1": 1.0,
            "E_2": 1.0,
            "E_3": 1.0,
            "E_4": 1.0,
            "E_5": 1.0,
        }

        disp_datatable = utils.display_schedule(
            utils.build_schedule_from_sample(sample, shifts, employees),
            availability,
            12,
            2023,
        )

        # This should verify we don't have any issues in the object created for display from a sample
        self.assertEqual(type(disp_datatable), dash_table.DataTable)
