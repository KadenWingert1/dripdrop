# ========================================
#      Used to test functions/tables
# ========================================

# *** MUST DO:
# At all **TODO** points, please fill them in with the appropriate information
# Beside all **TODO** points, information is provided as to what should be replaced/added.

# Information:
# This is not meant to be used as an endpoint in the API Gateway, ONLY as a framework for
# testing in the Lambda portion of AWS.
#
# This is meant to be used as a very general test file for testing backend functionality
# and tables. This is not meant to be a simple plug and play, as different functions
# will require different inputs, different checking, etc. However, this should provide
# some basic framework to get started on testing to make the testing process easier, quicker
# and more uniform.

# AWS Info:
# Go into the Lambda portion of AWS and open up the testFunction lambda. Make necessary edits.
# Testing - Create a new test event and populate the Event JSON with a JSON such as the following:
#       {
#           "body": "{\"<value>\": \"<value2>\"}"
#       }
#   Example (Where we want "tag": "black" for tag creation):
#       {
#           "body": "{\"tag\": \"black\"}"
#       }
#   The JSON has to be in this format to simulate what the event JSON would actually be.
# Invoke the test event once this has been done.

import json
# **TODO** -- fileName should be the name of the .py file containing functions to test (ex: tag.py --> <fileName> = tag)
# import <fileName> as <fileName>PY
from utils import create_response

def handler(event, context):
    try:
        # **TODO** -- This may not be needed for blanket calls, such as get ALL, however, it doesn't necessarily hurt to leave in during testing
        # Parse the data from event
        body = json.loads(event['body'])

        # **TODO** -- Add all attributes needed (ex: if ID is needed --> <value> = id)
        # Get all body attributes
        # <value> = body.get('<value>')

        # **TODO** -- Add all missing value checks (ex: if val is needed --> <value> = val)
        # Check for any missing values
        # if not <value>:
        #     return create_response(400, "Missing required field in ***")

        # **TODO** -- Ensure that all optional values have a value (ex: if val is optional (i.e. it can be given, but isn't required) --> <value> = val)
        # Ensure that a value is given to any variables that were not assigned
        # if not <value>:
        #     <value> = ""
        
        # **TODO** -- Add the call to the function under test (ex: if fileName = tag & testing create --> <fileName> = tag, <function> = createTag, <values> = tag_val)
        # Call another function to handle the operation
        # status_code, message = <fileName>PY.<function>(<values>)

        # Return it with the proper format
        return create_response(status_code, message)
        
    except Exception as e:
        print(f"Error: {e}")
        return create_response(500, f"Error: {str(e)}")