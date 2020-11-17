import logging

from django.http import HttpResponse
from django.template import loader
from graphviz import Source

logger = logging.getLogger(__name__)


def viz_render_to_svg(template_path, *args, engine='dot', **kwargs):
    # engine = kwargs.pop('engine', 'dot')
    logger.debug(f'load dot template at {template_path}')
    dot_source = loader.render_to_string(template_path, *args, **kwargs)
    logger.debug(f'result dot_source={dot_source}', dot_source)
    src = Source(dot_source, format='svg', engine=engine)
    return src.pipe()


def viz_render_to_svg_response(template_path, *args, **kwargs):
    svg_source = viz_render_to_svg(template_path, *args, **kwargs)
    return HttpResponse(svg_source, content_type='image/svg+xml')
