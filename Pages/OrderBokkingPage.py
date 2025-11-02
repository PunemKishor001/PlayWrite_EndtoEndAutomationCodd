import pytest
from playwright.sync_api import Page
from DataDrivenFromExcelSheet.InqNumber_Store import read_inquiry_from_excel


class OrderBooing:
    def __init__(self, page: Page):
        self.page = page

    # Locators
        self.InquiryLhn = '//span[text()="Inquiries"]'
        self.ViewInqLhn = '//span[text()="View Inquiries"]'
        self.Filter = '//span[text()="Filters"]'
        self.EnterInqNo = '//input[@placeholder="Enter Inquiry ID"]'
        self.ApplyButton = '//span[text()="Apply"]'
        self.View_Detais = '//span[text() = "View Details"]'
        self.SourcingDownArrow = '//span[text()="Sourcing"]'
        self.ExpandingFullTrucksection = '//td[text()="Full Truck"]'
        self.TruckCount = '(//div[contains(@class,"ant-input-number-input-wrap")]//input)[1]'
        self.DeclareWinner = '//span[text()="Declare Winner"]'


    def CreateInquirDownArrow(self):
        self.page.locator(self.InquiryLhn).click()

    def CreateViewInquirDownArrow(self):
        self.page.locator(self.ViewInqLhn).click()

    def Filter_Button(self):
        self.page.locator(self.Filter).click()

    def Inq_no(self,inquiry_number):
        self.page.locator(self.EnterInqNo).fill(inquiry_number)

    def Apply(self):
        self.page.locator(self.ApplyButton).click()

    def View(self):
        self.page.locator(self.View_Detais).click()

    def Sourcing_DownArrow(self):
        self.page.locator(self.SourcingDownArrow).click()

    def Exapnd_Section(self):
        self.page.locator(self.ExpandingFullTrucksection).click()

    def EnterTruckCunt(self):
        self.page.locator(self.TruckCount).fill("2")

    def Declare_Winner(self):
        self.page.locator(self.DeclareWinner).click()


