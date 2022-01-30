from ex1.mapping import RAW_MAPPING, ROLES_TREE


def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here

    categories = []
    for idSort in mapping['categoryIdsSorted']:
        item = mapping['categories'].get(idSort)
        category = {'id': 'category-' + item['id'], 'text': item['name']}
        items = []
        for id in item['roleIds']:
            role = mapping['roles'].get(id)
            if role:
                items.append({'id': role['id'], 'text': role['name']})
        category['items'] = items
        categories.append(category)
    return {'categories': categories}

