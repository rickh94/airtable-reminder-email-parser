#!/usr/bin/env python2
my_input = { 'body': 'this is a test. This is the text to insert.' }
output = { 'test_worked': False, 'insert_text': '' }
import re
# if input.get('body') and re.match(r'THIS IS A TEST.', input['body'], re.IGNORECASE):
if re.match(r'THIS IS A TEST.', my_input['body'], re.IGNORECASE):
    output['test_worked'] = True
    tmp = re.search(r'(THIS IS A TEST.)([^\.]*)', my_input['body'], re.IGNORECASE)
    output['insert_text'] = tmp.group(2)
