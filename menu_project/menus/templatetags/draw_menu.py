from collections import defaultdict
from django import template
from django.urls import reverse, NoReverseMatch
from django.utils.safestring import mark_safe
from menus.models import Menu, MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Render a tree menu based on the given name.
    Only one DB query is made to fetch the whole menu.
    """
    request = context.get("request")
    current_path = request.path if request else ""

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return f"<!-- Menu '{menu_name}' not found -->"

    items = list(MenuItem.objects.filter(menu=menu).select_related("parent"))

    tree = build_tree(items)
    active_ids = find_active_path(items, current_path)
    html = render_menu(tree, active_ids)
    return mark_safe(html)


def build_tree(items):
    """
    Build a tree structure: {parent_id: [children]}.
    """
    tree = defaultdict(list)
    for item in items:
        parent_id = item.parent.id if item.parent else None
        tree[parent_id].append(item)
    return tree


def find_active_path(items, current_path):
    """
    Find the currently active menu item based on the current path,
    and collect all its ancestor IDs for expansion.
    """
    active_ids = set()
    matched_item = None

    for item in items:
        resolved_url = ""
        if item.named_url:
            try:
                resolved_url = reverse(item.named_url)
            except NoReverseMatch:
                continue
        elif item.url:
            resolved_url = item.url

        if resolved_url and resolved_url == current_path:
            matched_item = item
            break

    while matched_item:
        active_ids.add(matched_item.id)
        matched_item = matched_item.parent

    return active_ids


def render_menu(tree, active_ids, parent_id=None):
    """
    Recursively render the tree menu as HTML.
    Only active branches and the first level below them are expanded.
    """
    html = ""
    items = tree.get(parent_id, [])

    if not items:
        return ""

    html += "<ul>"
    for item in items:
        is_active = item.id in active_ids
        has_children = tree.get(item.id)
        css_class = "active" if is_active else ""

        url = "#"
        if item.named_url:
            try:
                url = reverse(item.named_url)
            except NoReverseMatch:
                url = "#"
        elif item.url:
            url = item.url or "#"

        html += f'<li class="{css_class}">'
        html += f'<a href="{url}">{item.title}</a>'

        if is_active and has_children:
            html += render_menu(tree, active_ids, parent_id=item.id)

        html += "</li>"
    html += "</ul>"

    return html
