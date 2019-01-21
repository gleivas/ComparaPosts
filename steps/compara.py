from behave import *

from pages.page_facebook import go_to_facebook, get_facebook_latest_post
from pages.page_twitter import go_to_twitter, assert_text_is_on_twitter


@given(u'que há uma publicação nova no Facebook')
def step_impl(context):
    go_to_facebook(context.browser)
    context.face_post = get_facebook_latest_post(context.browser)


@when(u'acessarmos o Twitter')
def step_impl(context):
    go_to_twitter(context.browser)


@then(u'essa mesma publicação deverá estar no Twitter')
def step_impl(context):
    assert assert_text_is_on_twitter(context.browser, context.face_post), \
        'Não é possível garantir que o post está no Twitter'

print('teste')