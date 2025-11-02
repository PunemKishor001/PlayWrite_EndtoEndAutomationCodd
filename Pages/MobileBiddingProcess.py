import time
from re import search

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Asserstions.InquiryNumberSearch import InquirySearch

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
    Live_Loads = ("id", "com.trukkeruae.trukker_vender:id/nav_loads")
    BidNow = ("id","com.trukkeruae.trukker_vender:id/btnBid")
    HowMayTruck = ("id","com.trukkeruae.trukker_vender:id/btnIncreaseTruck")
    Enter_Amount = ("id","com.trukkeruae.trukker_vender:id/etBidPrice")
    SubMit_Button = ("id","com.trukkeruae.trukker_vender:id/btSubmit")
    Bid_Continue =("id","com.trukkeruae.trukker_vender:id/btContinueBidOutRange")

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
        Mobile_Number.send_keys("571235732")
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

    def LiveLoad(self):
        LivesLoads = self.driver.find_element(*BiddingToOrder.Live_Loads)
        LivesLoads.click()
        return LivesLoads

    def Search_Inquiry(self,inquiry_number):
        print(f"🔍 Starting inquiry search for: {inquiry_number}")
        Inq_Search = InquirySearch(self.driver)
        Inq_Search.search_and_bid(inquiry_number)

    def Bid_Now(self):
        print("🚛 Starting bid...")

        try:
            # Click Bid Now only
            self.driver.find_element(*BiddingToOrder.BidNow).click()
            time.sleep(1)

            print("✅ Bid Now button clicked")

        except Exception as e:
            print(f"❌ Error clicking Bid Now: {e}")
            raise e


    def HowMany_truck(self):
        HowManysTrucks = self.driver.find_element(*BiddingToOrder.HowMayTruck)
        HowManysTrucks.click()
        return HowManysTrucks

    def EntersAmoutn(self):
        Enters_Amount = self.driver.find_element(*BiddingToOrder.Enter_Amount)
        Enters_Amount.send_keys("30")
        return Enters_Amount

    def SubMit(self):
        SubMitButton = self.driver.find_element(*BiddingToOrder.SubMit_Button)
        SubMitButton.click()
        return SubMitButton

    def BidContinues_Button(self):
        ContinuesBid_Button = self.driver.find_element(*BiddingToOrder.Bid_Continue)
        ContinuesBid_Button.click()
        return ContinuesBid_Button