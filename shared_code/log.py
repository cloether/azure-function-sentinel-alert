# coding=utf8
"""log.py
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging


def log_request(req, context):
  """Log HTTP Request.

  Args:
    req (azure.functions.HttpRequest): HTTP Request.
    context (azure.functions.Context): Function context.
  """
  logging.debug(
    "python http trigger function request received: "
    "[%s] (%s/%s) - %s - %s - %s",
    context.invocation_id,
    context.function_directory,
    context.function_name,
    context.retry_context,
    context.trace_context,
    req
  )
