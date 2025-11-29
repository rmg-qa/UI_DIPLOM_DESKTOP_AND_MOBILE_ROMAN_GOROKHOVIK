class MobileMainPage:
    confirm_location_moscow = ".//button[text()='Да, верно']"
    confirm_cookie_files = "[class='js-cookie-data-warning__close']"
    burger_menu = '[title="Меню"]'
    choice_category_new_year = ".//span[text()='Новый год' and contains(@class, 'style_text')]"
    choice_subcategory_new_year_trees = ".//span[text()='Новогодние ёлки']"

    class MobileFooterMainPage:
        drop_down_about_company = './/h6[contains(@class, "List_title__") and text() = "О компании"]'
        principles_and_mission = '[href="/about/"]'


class MobileAboutCompany:
    title_first_screen = '[class="ab-first-banner-text"]'


class MobileProductsPage:
    title_category_new_year_trees = ".//h1[text()='Елки ']"
    first_product_on_the_list = './/div[contains(@class, "ProductGrid_gridI")][1]'


class MobileCart:
    button_add_product_in_cart = '[data-test-card="add_basket"]'
    button_delete_product_in_cart = '[data-name="IconBin"]'
    button_confirm_delete = ".//button[@type='button' and text()='Удалить']"


class MobileSiteNotifications:
    add_product_in_cart = ".//div[text()='Товар добавлен в корзину']"
    banner_advertisement = ".//div[text()='×']"
    delete_product_in_cart = ".//div[text()='Товар удален из корзины']"
