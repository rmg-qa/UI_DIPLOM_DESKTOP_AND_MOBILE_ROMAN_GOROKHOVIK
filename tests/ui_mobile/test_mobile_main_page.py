import time
import allure
from allure import step
from selene import browser, have, be
from locators.locators_web_mobile import MobileMainPage, MobileAboutCompany, MobileProductsPage, MobileCart, \
    MobileSiteNotifications


@allure.epic('Главная страница')
@allure.title('Выбор раздела "Новогодние ёлки" через меню-бургер')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.CRITICAL)
def test_go_to_the_section_new_year_trees(mobile_management):
    with step('Выбираем стандартную геопозицию: город "Москва"'):
        browser.element(MobileMainPage.confirm_location_moscow).should(be.clickable).click()
    with step('Переходим в бургерное меню, в категорию "Новый год", в категорию "Новогодние ёлки и венки"'):
        browser.element(MobileMainPage.burger_menu).should(be.clickable).click()
        browser.element(MobileMainPage.choice_category_new_year).click()
        browser.element(MobileMainPage.choice_subcategory_new_year_trees).click()
        browser.element(MobileProductsPage.title_category_new_year_trees).should(have.text('Елки'))


@allure.epic('Главная страница')
@allure.title('Переход на страницу "О компании" через футер страницы')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.CRITICAL)
def test_go_to_the_page_about_company(mobile_management):
    with step('Выбираем стандартную геопозицию: город "Москва"'):
        browser.element(MobileMainPage.confirm_location_moscow).should(be.clickable).click()
    with step(
            'Скроллим до футера страницы и выбираем выпадающий список "О компании", кликаем на подраздел "Принципы и миссия"'):
        # Скроллим через явное указание пикселей, так как на сайте реализована ленивая загрузка данных
        browser.driver.execute_script("window.scrollBy(0, 40000);")
        time.sleep(2)  # немного заслипаем, так как в процессе скролла блоки прыгают
        browser.driver.execute_script(
            "window.scrollBy(0, 1000);")  # еще раз реализуем скролл, сразу не получается до футера проскроллить
        browser.element(MobileMainPage.MobileFooterMainPage.drop_down_about_company).click()
        browser.element(MobileMainPage.MobileFooterMainPage.principles_and_mission).click()
        browser.element(MobileAboutCompany.title_first_screen).should(have.text('О компании'))


@allure.epic('Главная страница')
@allure.title('Добавляем в корзину новогоднюю ёлку')
@allure.tag('web-mobile')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_in_cart_new_year_tree(mobile_management):
    with step('Выбираем стандартную геопозицию: город "Москва"'):
        browser.element(MobileMainPage.confirm_location_moscow).should(be.clickable).click()
    with step('Переходим в бургерное меню, в категорию "Новый год", в категорию "Новогодние ёлки и венки"'):
        browser.element(MobileMainPage.burger_menu).should(be.clickable).click()
        browser.element(MobileMainPage.choice_category_new_year).click()
        browser.element(MobileMainPage.choice_subcategory_new_year_trees).click()
        browser.element(MobileProductsPage.title_category_new_year_trees).should(have.text('Елки'))
    with step('Переходим в товар новогодней елки, соглашаемся с куки файлами, добавляем елку в корзину'):
        browser.element(MobileProductsPage.first_product_on_the_list).click()
        browser.element(MobileMainPage.confirm_cookie_files).should(be.clickable).click()
        browser.element(MobileCart.button_add_product_in_cart).should(be.clickable).click()
        browser.element(MobileSiteNotifications.add_product_in_cart).should(be.present)
    with step('Удаляем товар из корзины'):
        browser.element(MobileCart.button_delete_product_in_cart).should(be.clickable).click()
    with step('Удаляем рекламный баннер, если он появляется'):
        banner = browser.element(MobileSiteNotifications.banner_advertisement)
        if banner.should(be.visible):
            banner.click()
        else:
            pass
    with step('Продолжаем удаление товара из корзины'):
        browser.element(MobileCart.button_confirm_delete).should(be.visible).click()
        browser.element(MobileSiteNotifications.delete_product_in_cart).should(be.present)
