from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    with open('news/templatetags/filter_words.txt', 'r', encoding='UTF-8') as file:
        file = file.readlines()[0].split()
        if isinstance(value, str):
            for word in file:
                value = value.replace(word, '**Censor**')
            return str(value)
        else:
            raise ValueError(f'Нельзя применять метод censor не к строке')