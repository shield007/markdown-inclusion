# Markdown inclusion plugin

This is plugin to extend python markdown and allow it include other markdown files. 

## Example use

The following example will include a remote markdown file into this file.

```markdown
# foo bar

This is a test

!{https://raw.githubusercontent.com/ARMmbed/BLEIntros/master/Docs/InDepth/Eddvents.md}!
```

# Development

To test the plugin and setup an development enviorment, execute the following command:

```bash
python ./setup.py develop
```

Their is a test.py script that can then be excuted to perform a basic test of the plugin.