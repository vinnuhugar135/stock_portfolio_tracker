import os
import tempfile
import unittest

import stock_tracker as st


class TestTracker(unittest.TestCase):
    def setUp(self):
        self.portfolio = [
            {"stock": "AAPL", "quantity": 10, "price": 180, "value": 1800},
            {"stock": "TSLA", "quantity": 5, "price": 250, "value": 1250},
        ]

    def test_total(self):
        self.assertEqual(st.calculate_total(self.portfolio), 3050)

    def test_empty_total(self):
        self.assertEqual(st.calculate_total([]), 0)

    def test_save_txt_and_csv(self):
        with tempfile.TemporaryDirectory() as d:
            t, c = os.path.join(d, "p.txt"), os.path.join(d, "p.csv")
            st.save_to_txt(self.portfolio, 3050, t)
            st.save_to_csv(self.portfolio, 3050, c)
            self.assertIn("3,050.00", open(t).read())
            self.assertIn("TOTAL", open(c).read())


if __name__ == "__main__":
    unittest.main()
