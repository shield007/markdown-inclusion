from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

import re
import requests

PATTERN = re.compile(r'!\{(.+)\}')

class InclusionPreprocessor(Preprocessor):
    
    def run(self,lines):
        new_lines = []
        for line in lines:
            m = PATTERN.match(line.strip())
            if m:
                url=m.group(1)
                response = requests.get(url)
                for line in response.text.splitlines(True):
                    new_lines.append(line)
            else:
                new_lines.append(line)
       
        return new_lines

class Inclusion(Extension):
   def extendMarkdown(self, md, md_globals):
       md.preprocessors.add("inclusion",InclusionPreprocessor(md),">normalize_whitespace")