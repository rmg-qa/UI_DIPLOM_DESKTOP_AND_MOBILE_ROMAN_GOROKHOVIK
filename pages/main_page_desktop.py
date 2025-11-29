from selene import browser, have
import data
from locators.locators_desktop import LocatorsSelectionPillow


class MainPageDesktop:
    @staticmethod
    def select_pillow(locator):
        browser.open(data.URL)
        browser.element(LocatorsSelectionPillow.modal_window).click()
        browser.element(LocatorsSelectionPillow.StepOnePillowFiller.foam_pillow).click()
        browser.element(LocatorsSelectionPillow.StepTwoFormPillow.special).click()
        browser.element(
            locator).click()  # этот локатор используем в параметризации и выбираем 1 из 4 видов положения сна
        browser.element(LocatorsSelectionPillow.StepFourChoiceGender.man).click()
        browser.element(LocatorsSelectionPillow.StepFiveSizePillow.xs_s).click()
        browser.element(LocatorsSelectionPillow.final_result).should(have.text('Результаты подбора'))
