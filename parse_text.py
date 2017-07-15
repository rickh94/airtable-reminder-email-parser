#!/usr/bin/env python2
# TEST DATA DO NOT COPY
input_data = { 'body': 'this is a test. This is the text to insert.',
        }

# COPY THIS CODE INTO ZAPIER
output = { 'test_worked': False, 'insert_text': '' }
trigger_phrase = r'(THIS IS A TEST.)' # replace this with your desired trigger
                                      # phrase. Not case sensitive. This will
                                      # not end up in the final record. Leave
                                      # the quotes, parentheses, and the r.
term_char = r'([^\.]*)' # The dot is the character that will terminate the text
                        # to be grabbed by the script. Replace the dot with
                        # your desired character.
import re
# if input.get('body') and re.match(r'THIS IS A TEST.', input['body'], re.IGNORECASE):
if re.match(trigger_phrase, input_data['body'], re.IGNORECASE):
    output['test_worked'] = True
    long_search = trigger_phrase + r'([^\.]*)'
    tmp = re.search(long_search, input_data['body'], re.IGNORECASE)
    output['insert_text'] = tmp.group(2)
