import inspect


def introspection_info(obj):
    return_dict = dict()
    return_dict['type'] = type(obj)
    return_dict['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
    return_dict['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    return_dict['module'] = inspect.getmodule(introspection_info)
    return return_dict


number_info = introspection_info(42)
print(number_info)
