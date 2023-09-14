# coding=utf8
"""test_sentinel_alert_http_trigger.py
"""
from __future__ import absolute_import, print_function, unicode_literals

# noinspection PyPackageRequirements
import azure.functions as func
import unittest

from sentinel_alert_http_trigger import main


# TODO: create test suite
class TestFunction(unittest.TestCase):
  """Test Case for Azure Function(s).
  """

  def test_sentinel_alert_http_trigger(self):
    """Test Azure Function: sentinel_alert_http_trigger
    """
    # construct a mock http request
    req = func.HttpRequest(
      method="GET",
      body=b"",
      url="/api/sentinel_alert_http_trigger",
      params={"value": "21"}
    )

    # call the azure function
    resp = main(req, func.Context())

    # check the output
    self.assertEqual(resp.get_body(), b"21 * 2 = 42")
