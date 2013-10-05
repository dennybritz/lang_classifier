#! /usr/bin/env python

import guess_language
import os
import sys

TARGET_DIR = "target/"

if not os.path.exists(TARGET_DIR):
  os.makedirs(TARGET_DIR)

for filename in sys.argv[1:]:
  
  # Detect language
  text = open(filename).read()
  language_code = guess_language.guessLanguage(text)

  # Move file into new directory
  lang_dir = TARGET_DIR + language_code
  if not os.path.exists(lang_dir):
    os.makedirs(lang_dir)
  new_path = "%s/%s" %(lang_dir, os.path.basename(filename))
  os.rename(filename, new_path)

  print "Moved %s to %s" %(filename, new_path)