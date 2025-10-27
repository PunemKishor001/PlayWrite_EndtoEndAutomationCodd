from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BiddingToOrder:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    Permissions =(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[1]")
    Country_Code = (By.ID,"com.trukkeruae.trukker_vender:id/tvCC")
    CountryDail_Code = (By.ID,"com.trukkeruae.trukker_vender:id/etSearchCountry")
    SelectingCode = (By.ID,"com.trukkeruae.trukker_vender:id/llCountryCode")
    Number = (By.ID,"com.trukkeruae.trukker_vender:id/etMobileNumber")
    Continue = (By.ID,"com.trukkeruae.trukker_vender:id/btContinue")
    OTP = (By.ID,"com.trukkeruae.trukker_vender:id/otpView")
    OTP_CONtinue = (By.ID,"com.trukkeruae.trukker_vender:id/btContinue")
    App_Permissions = (By.ID,"com.android.permissioncontroller:id/permission_allow_button")

    def App_Permission(self):
        PerMission_Button = self.driver.find_element(*BiddingToOrder.Permissions)
        PerMission_Button.click()
        return PerMission_Button

    def CountryCode(self):
        CountryCodeButton = self.driver.find_element(*BiddingToOrder.Country_Code)
        CountryCodeButton.click()
        return CountryCodeButton

    def CountryDailCode(self):
        DailsCode = self.driver.find_element(*BiddingToOrder.CountryDail_Code)
        DailsCode.send_keys("971")
        return DailsCode

    def Selecting_Code(self):
        CodeSelection = self.driver.find_element(*BiddingToOrder.SelectingCode)
        CodeSelection.click()
        return CodeSelection

    def MobileNumber(self):
        Mobile_Number = self.driver.find_element(*BiddingToOrder.Number)
        Mobile_Number.send_keys("568965355")
        return Mobile_Number

    def ContinueButton(self):
        Continue_Button = self.driver.find_element(*BiddingToOrder.Continue)
        Continue_Button.click()
        return Continue_Button

    def OTP_EnterS(self):
        OtpEnters = self.driver.find_element(*BiddingToOrder.OTP)
        OtpEnters.send_keys("123456")
        return OtpEnters

    def OTPContinuE(self):
        Continues = self.driver.find_element(*BiddingToOrder.OTP_CONtinue)
        Continues.click()
        return Continues

    def AllowPermission(self):
        AppPermission = self.driver.find_element(*BiddingToOrder.App_Permissions)
        AppPermission.click()
        return AppPermission