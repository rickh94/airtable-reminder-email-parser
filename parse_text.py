#!/usr/bin/env python2
# TEST DATA: DO NOT COPY
input_data = { 'body': 'this is a test. This is the text to insert.',
        }

# COPY THIS CODE INTO ZAPIER
output = { 'matched': False, 'insert_text': '' }
# replace these values to customize. See README for details.
trigger_phrase = r'(THIS IS A TEST. )' # include a space at the end or the
                                       # found text will start with a space
term_char = r'([^\.]*)' 

import re
if re.search(trigger_phrase, input_data['body'], re.IGNORECASE):
    output['matched'] = True
    long_search = trigger_phrase + r'([^\.]*)'
    tmp = re.search(long_search, input_data['body'], re.IGNORECASE)
    output['insert_text'] = tmp.group(2)
