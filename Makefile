FUNCTIONS_APP_NAME="sentinel-alert-func"
FUNCTION_NAME="sentinel-alert-func"

func-new-python:
	func new --language python

func-new-python-http-trigger:
	func new -t HttpTrigger -n HttpTrigger -a anonymous

func-init-python:
	func init --language python

func-init-python-docker:
	func init --worker-runtime python --docker

func-logs:
	func azure functionapp logstream "$(FUNCTIONS_APP_NAME)" --browser

func-start:
	func start

fetch-app-settings:
	func azure functionapp fetch-app-settings "$(FUNCTIONS_APP_NAME)"

func-deploy:
	func azure functionapp publish "$(FUNCTIONS_APP_NAME)"
