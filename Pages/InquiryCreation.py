import pytest
from IPython.lib.latextools import latex_to_png_mpl
from playwright.sync_api import Page
from DataDrivenFromExcelSheet.DataDrivenForWeB import CreateinquiryExecutionData

print(CreateinquiryExecutionData())

class InquiryCreationlocaters:

    def __init__(self, page: Page):
        self.page = page

    #Locators
        self.InquiryLhn = '//span[text()="Inquiries"]'
        self.Create_Inquiry = '//span[text()="Create Inquiry"]'
        self.Name = '//input[@id="shipperMasterName"]'
        self.Truck = '//input[@id="truckType"]'
        self.Sub = '//input[@id="subTruckType"]'
        self.Commodity = '//input[@id="commodityType"]'
        self.Weight = '//input[@id="weightPerTruck"]'
        self.InquiryRecived_Calender = '//input[@id="inquiryReceivedDateTime"]'
        self.InquryRecived_Dateandtime = '//td[@title="2025-11-02"]'
        self.OK = '//span[text()="OK"]'
        self.Source = '//input[@id="inquirySource"]'
        self.From_City = '//input[@id="city_0"]'
        self.Source_Address = '(//input[@placeholder="Search Places..."])[1]'
        self.To_City = '//input[@id="city_1"]'
        self.DestAddress = '(//input[@placeholder="Search Places..."])[2]'
        self.MoveDateCalender = '//input[@id="fromDate_0"]'
        self.MoveDateandTime = '(//td[@title="2025-11-27"])[2]'
        self.MoveDateandTimeOK = '(//span[text()="OK"])[2]'
        self.NoTruck = '//input[@id="count_0"]'
        self.RatePerTruck = '//input[@id="ratePerUnit_0"]'
        self.Submit = '//span[text()="Submit"]'
        self.Success = '//a[@class="inquiry-number"]/span'

    # ---------- Actions ----------
    def CreateInquirDownArrow(self):
        self.page.locator(self.InquiryLhn).click()

    def CreateInquiry(self):
        self.page.locator(self.Create_Inquiry).click()

    def Shipper_Name(self,getdata):
        # Shipper_Names = getdata["shippername"]
        # self.page.locator(self.Name).fill("Unilever UAE")
        self.page.locator(self.Name).fill(getdata["shippername"])
        self.page.wait_for_timeout(3000)
        self.page.locator(self.Name).press("ArrowDown")
        self.page.locator(self.Name).press("Enter")

    def TruckType(self,getdata):
        self.page.locator(self.Truck).click()
        # self.page.locator(self.Truck).fill('Flatbed')
        self.page.locator(self.Truck).fill(str(getdata["trucktype"]))
        self.page.wait_for_timeout(2000)
        self.page.locator(self.Truck).press("ArrowDown")
        self.page.locator(self.Truck).press("Enter")

    def Sub_TruckType(self,getdata):
        # self.page.locator(self.Sub).click()
        # self.page.locator(self.Sub).fill('12M')
        self.page.locator(self.Sub).fill(str(getdata["subtrucktype"]))
        self.page.wait_for_timeout(2000)
        self.page.locator(self.Sub).press("ArrowDown")
        self.page.locator(self.Sub).press("Enter")

    def Commodity_Type(self,getdata):
        # self.page.locator(self.Commodity).fill('Air Conditioners & Chiller')
        self.page.locator(self.Commodity).fill(str(getdata["Commodity"]))
        self.page.locator(self.Commodity).press('ArrowDown')
        self.page.locator(self.Commodity).press('Enter')

    def Weight_PerTruck(self,getdata):
        # self.page.locator(self.Weight).fill('10')
        self.page.locator(self.Weight).fill(str(getdata["Weight"]))

    def InquiryRecivedCalender(self):
        self.page.locator(self.InquiryRecived_Calender).click()

    def DateandTime(self):
        self.page.locator(self.InquryRecived_Dateandtime).click()

    def OK_Button(self):
        self.page.locator(self.OK).click()

    def Inquiry_Sources(self):
        self.page.locator(self.Source).press("Enter")
        self.page.locator(self.Source).press("ArrowDown")
        self.page.locator(self.Source).press("Enter")

    def FromCity(self,getdata):
        # self.page.locator(self.From_City).fill('Dubai')
        self.page.locator(self.From_City).fill(str(getdata["FromCity"]))
        self.page.wait_for_timeout(2000)
        self.page.locator(self.From_City).press('ArrowDown')
        self.page.locator(self.From_City).press('Enter')

    def SourceAdress(self,getdata):
        # self.page.locator(self.Source_Address).fill('Dubai')
        self.page.locator(self.Source_Address).fill(str(getdata["FromCity"]))
        self.page.wait_for_timeout(2000)
        self.page.locator(self.Source_Address).press('ArrowDown')
        self.page.locator(self.Source_Address).press('Enter')

    def ToCity(self,getdata):
        # self.page.locator(self.To_City).fill('Dubai')
        self.page.locator(self.To_City).fill(str(getdata["ToCity"]))
        self.page.wait_for_timeout(2000)
        self.page.locator(self.To_City).press('ArrowDown')
        self.page.locator(self.To_City).press('Enter')

    def Dest_Address(self,getdata):
        # self.page.locator(self.DestAddress).fill('Dubai')
        self.page.locator(self.DestAddress).fill(str(getdata["ToCity"]))
        self.page.wait_for_timeout(2000)
        self.page.locator(self.DestAddress).press('ArrowDown')
        self.page.locator(self.DestAddress).press('Enter')

    def MoveDate_Calender(self):
        self.page.locator(self.MoveDateCalender).click()

    def MOveDate_Time(self):
        self.page.locator(self.MoveDateandTime).click()

    def OKbutton(self):
        self.page.locator(self.MoveDateandTimeOK).click()

    def No_Trucks(self,getdata):
        # self.page.locator(self.NoTruck).fill('2')
        self.page.locator(self.NoTruck).fill(str(getdata["NoTruck"]))

    def Rate_Truck(self,getdata):
        # self.page.locator(self.RatePerTruck).fill('100')
        self.page.locator(self.RatePerTruck).fill(str(getdata["Rate"]))

    def Submit_Button(self):
        self.page.locator(self.Submit).click()

    def Success_PopUp(self):
        """Wait for success popup and return its message"""
        try:
            self.page.wait_for_selector(self.Success, timeout=15000)
            popup_text = self.page.locator(self.Success).inner_text().strip()
            print(f"✅ Inquiry popup message: {popup_text}")
            return popup_text
        except Exception as e:
            print(f"❌ Failed to get success popup: {e}")
            return ""

    def Get_Inquiry_Number(self):
        try:
            # ✅ Modify selector based on your UI HTML
            inquiry_element = self.page.locator("//a[@class='inquiry-number']/span")
            self.page.wait_for_timeout(2000)
            inquiry_text = inquiry_element.inner_text().strip()
            print(f"📦 Extracted Inquiry Number: {inquiry_text}")
            return inquiry_text
        except Exception:
            print("⚠️ Inquiry number not found in popup.")
            return None

    @pytest.fixture(params=CreateinquiryExecutionData.getTestdata("CreateInquiryData"))
    def getdata(request):

        return request.param