import yaml

def to_yaml(object):
    return yaml.dump(object)

def from_yaml(yaml_string):
    return yaml.safe_load(yaml_string)

yaml_string = to_yaml({
    'course_code': 'PAS',
    'title': 'Python App Security',
    'date': 'today'
})

parsed_yaml = from_yaml(yaml_string)

print(parsed_yaml)