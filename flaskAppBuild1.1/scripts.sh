#! bin/bash

flask --app server --debug run

curl -X GET -i -w '\n' localhost:5000