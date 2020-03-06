from .directives import MarkdownToHtml


def setup(app):
    app.add_directive("md2html", MarkdownToHtml)
