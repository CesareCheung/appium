import HTMLReport
import unittest
from Test_Suite import login_suite

suite = unittest.TestSuite()
suite.addTests(login_suite.get_suite())

HTMLReport.TestRunner(
    report_file_name="index",
    description="XXXXXX",
    title="XXXXX",
    thread_count=2
).run(suite)
