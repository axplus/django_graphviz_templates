from django_graphviz_templates.shortcuts import viz_render_to_svg_response


def index(request):
    name = request.GET.get('name', 'yijie')
    return viz_render_to_svg_response('index.dot', {'name': name})
