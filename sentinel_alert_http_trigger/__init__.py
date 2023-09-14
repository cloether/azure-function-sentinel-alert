# coding=utf8
"""__init__.py
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

import azure.functions as func  # noqa

# use absolute import to resolve shared_code module
from shared_code import log


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
  """Azure Function Entry Point.

  Args:
    req (azure.functions.HttpRequest): HTTP Request.
    context (azure.functions.Context): Function context.

  Returns:
    func.HttpResponse: HTTP Response.
  """
  logging.info('[%s] az-function main called', context.function_name)

  log.log_request(req, context)

  name = req.params.get('name')
  if not name or name is None:
    try:
      req_body = req.get_json()
    except ValueError:
      logging.exception("error occurred while attempting to load request body")
    else:
      name = req_body.get('name')

  if name:
    return func.HttpResponse(
      f"hello, {name}. http triggered function executed successfully"
    )

  return func.HttpResponse(
    "http triggered function executed successfully. "
    "pass a name in the query string or in the request body "
    "for a personalized response",
    status_code=200
  )
