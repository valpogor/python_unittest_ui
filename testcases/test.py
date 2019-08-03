import unittest, HtmlTestRunner
from selenium import webdriver
from helpers import utility, webdriver
from pageobjects import strings

class TestCoupons(unittest.TestCase):

    def setUp(self):
        webdriver.driver(self, "FIREFOX")

    def test_verify_coupon_amoxicillin(self):
        utility.verify_coupons(self,'Amoxicillin')

    def test_verify_coupon_avdil(self):
        utility.verify_coupons(self,'Advil')

    def test_verify_coupon_truemetrix(self):
        utility.verify_coupons(self,'True Metrix')

    def test_verify_coupon_vicodin(self):
        utility.verify_coupons(self,'Vicodin')

    def test_verify_coupon_amoxicillin_cust_gen(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_generic, "2")

    def test_verify_coupon_amoxicillin_cust_bottle(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_capsule, "1")

    def test_verify_coupon_amoxicillin_cust_chew(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_capsule, "3")

    def test_verify_coupon_amoxicillin_cust_drop(self):
        utility.verify_coupon_custom(self,'Amoxicillin', strings.option_capsule, "4")

    def test_verify_coupon_amoxicillin_cust_tab(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_capsule, "5")

    def test_verify_coupon_amoxicillin_cust_doz(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_dosage, "1")

    def test_verify_coupon_amoxicillin_cust_20(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_quantity, "1")

    def test_verify_coupon_amoxicillin_cust_21(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_quantity, "2")

    def test_verify_coupon_amoxicillin_cust_28(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_quantity, "3")

    def test_verify_coupon_amoxicillin_cust_60(self):
        utility.verify_coupon_custom(self, 'Amoxicillin', strings.option_quantity, "5")

    def test_verify_coupon_amoxicillin_cust_max(self):
        utility.verify_coupon_custom_quan(self, 'Amoxicillin', "90")

    def test_verify_coupon_advil_cust_gen(self):
        utility.verify_coupon_custom(self, 'Advil', strings.option_generic, "1")

    def test_verify_coupon_advil_cust_gen_motrin(self):
        utility.verify_coupon_custom(self, 'Advil', strings.option_generic, "3")

    def test_verify_coupon_advil_cust_capsule(self):
        utility.verify_coupon_custom(self, 'Advil', strings.option_capsule, "1")

    def test_verify_coupon_advil_cust_20(self):
        utility.verify_coupon_custom(self, 'Advil', strings.option_quantity, "1")

    def test_verify_coupon_advil_cust_100(self):
        utility.verify_coupon_custom(self, 'Advil', strings.option_quantity, "3")

    def test_verify_coupon_advil_cust_500(self):
        utility.verify_coupon_custom(self, 'Advil', strings.option_quantity, "4")

    def test_verify_coupon_advil_cust_1000(self):
        utility.verify_coupon_custom_quan(self, 'Advil', "1000")

    def test_verify_coupon_truemetrix_cust_meter(self):
        utility.verify_coupon_custom(self, 'True Metrix', strings.option_capsule, "1")

    def test_verify_coupon_truemetrix_cust_50(self):
        utility.verify_coupon_custom(self, 'True Metrix', strings.option_quantity, "1")

    def test_verify_coupon_truemetrix_cust_150(self):
        utility.verify_coupon_custom(self, 'True Metrix', strings.option_quantity, "3")

    def test_verify_coupon_truemetrix_cust_200(self):
        utility.verify_coupon_custom(self, 'True Metrix', strings.option_quantity, "4")

    def test_verify_coupon_truemetrix_cust_300(self):
        utility.verify_coupon_custom(self, 'True Metrix', strings.option_quantity, "5")

    def test_verify_coupon_truemetrix_cust_max(self):
        utility.verify_coupon_custom_quan(self, 'True Metrix', "90")

    def test_verify_coupon_vicodin_cust_gen_vicodin(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_generic, "1")

    def test_verify_coupon_vicodin_cust_gen_xodol(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_generic, "3")

    def test_verify_coupon_vicodin_cust_ml(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_capsule, "1")

    def test_verify_coupon_vicodin_cust_doz_5(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_dosage, "1")

    def test_verify_coupon_vicodin_cust_doz7(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_dosage, "2")

    def test_verify_coupon_vicodin_cust_doz10(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_dosage, "3")

    def test_verify_coupon_vicodin_cust_doz2_325(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_dosage, "4")

    def test_verify_coupon_vicodin_cust_doz5_325(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_dosage, "5")

    def test_verify_coupon_vicodin_cust_doz7_325(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_dosage, "6")

    def test_verify_coupon_vicodin_cust_60(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_quantity, "1")

    def test_verify_coupon_vicodin_cust_90(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_quantity, "2")

    def test_verify_coupon_vicodin_cust_150(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_quantity, "4")

    def test_verify_coupon_vicodin_cust_180(self):
        utility.verify_coupon_custom(self, 'Vicodin', strings.option_quantity, "5")

    def test_verify_coupon_vicodin_cust_105(self):
        utility.verify_coupon_custom_quan(self, 'Vicodin', "105")

    def tearDown(self):
        webdriver.closeDriver(self)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/'))
