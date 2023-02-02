from datetime import date
import allure
from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages.practice_form import PracticePage

practice_form = PracticePage()


@allure.title("Successful fill form")
def test_practice_form():
    user = User(
        first_name='Chev',
        last_name='Chelios',
        email='ChevChelios@gmail.com',
        phone='1234567890',
        address='Moscow',
        birthday=date(1989, 10, 12),
        gender='Male',
        subject='Economics',
        hobbies='Music',
        image='1.png',
        state='NCR',
        city='Delhi')
    with allure.step('Open registrations form'):
        practice_form.open()
    with allure.step('Fill form'):
        practice_form.fill(user).submit()
    with allure.step('Check from results'):
        practice_form.assert_results_registration(user)
