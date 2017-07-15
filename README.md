# Airtable Reminder Email Parser
A python script for Zapier to work with incoming emails (gmail service) to
created airtable records. It takes a plain text input (e.g. an email body) and
outputs matched text and a boolean for flow control.

# Input
It takes plain text as 'body' for input. In the case of an email, be sure to
select 'Body Plain' not 'Body HTML.'
# Text Matching
All text is matched after a trigger phrase (trigger\_phrase) up to a
terminating character (term\_char). These are hard-coded but could be
set as inputs in zapier with a little tweaking (watch out for python regex
syntax).
trigger\_phrase default is `THIS IS A TEST.` Replace only this text to
customize the phrase. Leave the r, quotes, and parentheses so that the python
search still works. Not case sensitive.
term_char defaults to a period. Replace only the period to customize it.

# "Zap" Structure
The test zap had the following structure:
1. Gmail: New Email
2. Run Python (This is where the python code goes.\*)
3. Filter: Only continue if (2: Run Python: Matched)
4. Airtable: Create Record. Connect the text of the record to 
2: Run Python: Insert Text (I also put the full text of the email in a note
and the date from the email in a 'created' field. You can pass the date
directly from the email but if you try to do the time as well you can get
timezone issues).

\* It is important to only copy from below "# COPY THIS CODE INTO ZAPIER" or
they input may be overridden which defeats the whole point.
