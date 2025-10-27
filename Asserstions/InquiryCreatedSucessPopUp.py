from TestCases.test_TC001_InquiryCreationUAECB import test_CreateInquiryUAECB
from TestCases.test_TC001_BiddingProcessForUAECB import test_MobileLogin

def test_MasterFlow():
    popup_text = test_CreateInquiryUAECB()
    print(f"🔎 Popup text received: [{popup_text}]")

    # ✅ Check success condition
    if popup_text and "inquiry details" in popup_text.lower():
        print("✅ Inquiry created successfully. Proceeding to mobile login test...")
        test_MobileLogin()
    else:
        print("❌ Inquiry creation failed. Skipping mobile login test.")
