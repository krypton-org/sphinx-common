from pathlib import Path

from docutils import nodes, statemachine
from docutils.parsers.rst import Directive
from markdown import markdown


class MarkdownToHtml(Directive):
    has_content = True

    def run(self):
        # statemachine hack since I didn't managed
        # to return a valid `raw` node...
        # This could be done much cleaner.
        md = Path(self.content[0]).read_text()
        html = markdown(md, extensions=["fenced_code"])
        # HACK: Replace /docs/ links with /
        # TODO: Proper directive option
        html = html.replace("/docs/", "/")
        lines = statemachine.string2lines(html, 4, convert_whitespace=True)
        lines = ["    " + line for line in lines]
        lines.insert(0, ".. raw:: html")
        lines.insert(1, "")
        self.state_machine.insert_input(lines, "")
        return []
