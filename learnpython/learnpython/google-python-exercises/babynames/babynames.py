#! /Users/shaunjayaraj/.pyenv/shims/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import asyncio 
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def add_to_dict(rank, s,dict):
  if s not in dict.keys():
    dict[s] = rank 
  return dict

def get_dict_of_name_rank(match_list):
  result_dict = {}
  for items in match_list:
    add_to_dict(items[0], items[1],result_dict)
    add_to_dict(items[0], items[2],result_dict)
  return result_dict

def concat_file_text(args):
  file_text = ""
  final_result = []
  for filename in args:
    f = open(filename,'r')
    file_text = f.read()
    f.close()
    final_result.extend(extract_names(file_text))
  return final_result

def tuples_to_string(list_of_tuples):
  res = []
  for tup in list_of_tuples:
    res.append(tup[0] + " " + tup[1] + " ")
  return res


def extract_names(file_text):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
 

  match = re.search(r"Popularity in (\d\d\d\d)", file_text)
  date = match.group(1)

  match_list = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_text)

  result_list =[]
  result_list.append((date + " "))
  #match_list = [(3, "a", "b"), (21, "a", "c"), (44, "a", "d"), (11, "a", "z"), (56, "a", "c"), (9, "a", "c")]

  dict = get_dict_of_name_rank(match_list)

  result_list.extend(tuples_to_string(sorted(dict.items())))


  return result_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]


  res = concat_file_text(args)

  if summary == True:
    f = open("./output.txt",'w')
    f.write(''.join(res))
  else:
    print(''.join(res))

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
