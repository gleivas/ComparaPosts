from behave import *
from pages.setting_page.variaveis import *
from helpers.browser import *


#o post dado é escolhido no arquivo das variaveis, portanto esse step ele só passa
@given('um post')
def step_impl(context):
    pass


#abre o navegador, vai até a url do twitter e procura o post pela tag desejada atribuindo-a a uma variavel
@when('verificamos se ele esta no twitter')
def step_impl(context):
    navegando = Navegar()
    navegando.visitar(url_twitter)
    context.resultado_twitter = navegando.acha_post(tag_twitter, post)


#vai até a url do blog, procura o post pela tag desejada atribuindo-a a uma variavel e fecha o navegador
@when('verificamos se ele esta no blog')
def step_impl(context):
    navegando = Navegar()
    navegando.visitar(url_blog)
    context.resultado_blog = navegando.acha_post(tag_blog, post)
    navegando.fechar()


#se as variaveis atribuidas nos steps anteriores forem ambas verdadeiras o teste passará
@then('o teste passara se estiver nos dois')
def step_impl(context):
    assert context.resultado_twitter is True and context.resultado_blog is True
