class LocatorsMainPage:
    catalog = '[data-test-header="menu"]'
    global_search = '[type="text"]'
    success_popup = '[data-test-site="success"]'

    class LocatorsBlockSalesHits:
        first_item_button_in_cart = ".//div[contains(@class, 'item__button')]//child::button[@data-sku='1509579']"
        first_item_button_favorite = './/div[contains(@class, "add-to-wishlist")]//child::button[@data-sku="1509579"]'

    class LocatorsSideBarCart:
        result_add_item_in_cart = './/div[contains(@class, "header_block")]'


class LocatorsResultGlobalSearch:
    title_result_search = './/h1[contains(@class, "TitleBlock")]'


class LocatorsSelectionPillow:
    modal_window = './/span[text()="Подборщик подушек"]//parent::div//parent::div[@class]//child::span[text()="Подобрать"]'
    final_result = ".//div[text()='Результаты подбора']"

    class StepOnePillowFiller:
        foam_pillow = ".//div[text()='Подушка из пены']"

    class StepTwoFormPillow:
        special = ".//div[text()='специальная']"

    class StepThreeSleepPosition:
        on_the_side = ".//div[text()='на боку']"
        on_the_back = ".//div[text()='на спине']"
        on_the_stomach = ".//div[text()='на животе']"
        i_change_my_position_in_my_sleep = ".//div[text()='меняю положение во сне']"

    class StepFourChoiceGender:
        man = ".//div[text()='Мужчина']"

    class StepFiveSizePillow:
        xs_s = ".//div[text()='XS/S']"
