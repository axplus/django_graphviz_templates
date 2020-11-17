from axplus.base import Component
from axplus.htmlcomponents import Svg

from .shortcuts import viz_render_to_svg


class Digraph(Component):
    def render(self):
        source = viz_render_to_svg(self.props['template'])
        return Svg(
            source
        )
