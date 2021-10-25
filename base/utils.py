from django.apps.registry import apps

def get_fields(app,model):
    registry_apps = apps
    all_models = registry_apps.all_models[app]
    models = all_models[model]._meta.get_fields()
    attr_list = []
    for x in models:
        attr_list.append(x)
    return attr_list