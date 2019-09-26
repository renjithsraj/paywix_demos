from django import  template

register = template.Library()

# Category listing tags for side nav bs
@register.inclusion_tag('tags/stripe_payment_form.html', takes_context=True)
def side_category_tag(context, data):
    return {'data': data}

