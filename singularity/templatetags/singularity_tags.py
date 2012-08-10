from django import template

register = template.Library()


class AngularJS(template.Node):
	def __init__(self, bits):
		self.ng = bits

	def render(self, ctx):
		return "{{%s}}" % " ".join(self.ng[1:])

@register.tag()
def ng(parser, token):
	return AngularJS(token.split_contents())
