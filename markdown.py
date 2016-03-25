"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
 4. convert #, ##, and ### to h1, h2, and h3 tags
 5. convert > to blockquote
 
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  line = re.sub(r'#(.*)', r'<h1>\1</h1>',line)
  return line

def convertH2(line):
  line = re.sub(r'<h1>#(.*)</h1>', r'<h2>\1</h2>',line)
  return line

def convertH3(line):
  line = re.sub(r'<h2>#(.*)</h2>', r'<h3>\1</h3>',line)
  return line

def convertBlockQuote(line):
  line = re.sub(r'> (.*)', r'\1', line)
  line = re.sub(r'>(.*)',r'\1',line)
  return line

prev_line = ' '
for line in fileinput.input():  
  line = line.rstrip()
  old_line = line
  
  if line[0] == '>' and prev_line[0] != '>':
    print '<blockquote>',
    line = convertBlockQuote(line)
    line = convertStrong(line)
    line = convertEm(line)
    line = convertH1(line)
    line = convertH2(line)
    line = convertH3(line)
    print '<p>' + line + '</p>',
    prev_line = old_line
    continue
    
  if prev_line[0] == '>' and line[0] != '>':
    print '</blockquote>',
    
  line = convertBlockQuote(line)
  line = convertStrong(line)
  line = convertEm(line)
  line = convertH1(line)
  line = convertH2(line)
  line = convertH3(line)
  print '<p>' + line + '</p>', 
  
  prev_line = old_line
  
if prev_line[0] == '>':
  print '</blockquote>'
