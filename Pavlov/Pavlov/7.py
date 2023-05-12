from jinja2 import Template
print(Template("{{ 10 + 3 }}").render())
print(Template("{{ 10 - 3 }}").render())
print(Template("{{ 10 // 3 }}").render())
print(Template("{{ 10 / 3 }}").render())
print(Template("{{ 10 % 3 }}").render())
print(Template("{{ 10 ** 3 }}").render())
print(Template("{{ var }}").render(var="hello"))
print(Template("{{ var['profession'] }}").render(var={'name':'tom', 'age': 25, 'profession': 'Manager' }))