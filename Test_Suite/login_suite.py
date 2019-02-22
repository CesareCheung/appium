import unittest
from Test_Case import ts_login_1, ts_login_2, ts_login_3


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTests(loader.loadTestsFromTestCase(ts_login_1.TS_Login))
    # suite.addTests(loader.loadTestsFromTestCase(ts_login_2.TS_Login))
    suite.addTests(loader.loadTestsFromTestCase(ts_login_3.TS_Login))
    return suite
