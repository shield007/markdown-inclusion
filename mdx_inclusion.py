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
                if response.status_code == requests.codes.ok:
                    new_lines.append(response.text)
            else:
                new_lines.append(line)
       
        return new_lines

class Inclusion(Extension):
   def extendMarkdown(self, md, md_globals):
       md.preprocessors.add("inclusion",InclusionPreprocessor(md),">normalize_whitespace")

def makeExtension(*args, **kwargs):
    return Inclusion(*args, **kwargs)
