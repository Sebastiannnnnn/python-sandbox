from jinja2 import Environment, FileSystemLoader
import yaml

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

with open('templates/origins.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    varnish = yaml.load(file)

    for item in file:
        print(item)

template = env.get_template('template.vsl.j2')
output = template.render(varnish)
print(output)

f = open('result.vsl', 'w')
f.write(output)
f.close()
