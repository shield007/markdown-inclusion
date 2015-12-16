import markdown
from markdown_inclusion import Inclusion

#print markdown.markdown('foo bar\n!{https://raw.githubusercontent.com/ARMmbed/BLEIntros/master/Docs/InDepth/Events.md}!', extensions=[Inclusion()])

print markdown.markdown('foo bar\n!{https://raw.githubusercontent.com/ARMmbed/BLEIntros/master/Docs/InDepth/Eddvents.md}!', extensions=[Inclusion()])
