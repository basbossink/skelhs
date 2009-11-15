from paste.script.templates import var
from paste.script.templates import Template

class Module(Template):
    """Basic Haskell module template"""
    _template_dir = 'tmpl/module'
    summary = "A haskell module with a test environment"
    use_cheetah = True
    vars = [
            var('module_name', 'Module name'),
            var('description', 'One-line description of the module'),
            var('author', 'Author name'),
            var('author_email','Author email')
            ]
