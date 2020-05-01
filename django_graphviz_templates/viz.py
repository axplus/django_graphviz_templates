import logging

from django.http import HttpResponse
from django.template import loader
from graphviz import Source

logger = logging.getLogger(__name__)


def viz_render_to_svg(*args, **kwargs):
    engine = kwargs.pop('engine', 'dot')
    dot_source = loader.render_to_string(*args, **kwargs)
    logger.debug('dot_source=%s', dot_source)
    src = Source(dot_source, format='svg', engine=engine)
    return src.pipe()


def viz_render_to_svg_response(*args, **kwargs):
    svg_source = viz_render_to_svg(*args, **kwargs)
    return HttpResponse(svg_source, content_type='image/svg+xml')
