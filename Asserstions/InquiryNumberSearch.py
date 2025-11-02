from appium.webdriver.common.appiumby import AppiumBy

class InquirySearch:

    def __init__(self, driver):
        self.driver = driver

    def pause(self, sec=2):
        import time
        time.sleep(sec)

    def search_and_bid(self, inquiry_number):
        from Pages.MobileBiddingProcess import BiddingToOrder

        driver = self.driver
        print(f"📦 Searching Inquiry: {inquiry_number}")
        self.pause(2)

        expand_buttons = driver.find_elements(AppiumBy.ID, "com.trukkeruae.trukker_vender:id/ivExpand")

        if not expand_buttons:
            print("❌ No load sections found")
            return

        section_index = 0

        for expand_btn in expand_buttons:
            section_index += 1
            print(f"📂 Opening section {section_index}")
            expand_btn.click()
            self.pause(1)

            # Try clicking See All
            try:
                see_btn = driver.find_element(AppiumBy.ID, "com.trukkeruae.trukker_vender:id/tvSeeAll")
                see_btn.click()
                print(f"✅ Inside section {section_index}")
                self.pause(1.5)
            except:
                print(f"⚠️ No 'See All' in section {section_index}, skipping this section...")
                try:
                    expand_btn.click()  # collapse back
                except:
                    pass
                continue

            # Screen size for swipe scrolling
            size = driver.get_window_size()
            start_x = int(size["width"] * 0.5)
            start_y = int(size["height"] * 0.80)
            end_y = int(size["height"] * 0.20)

            # Scroll inside see all page
            for _ in range(8):
                try:
                    inquiry_ele = driver.find_element(
                        AppiumBy.XPATH, f"//android.widget.TextView[@text='{inquiry_number}']"
                    )
                    inquiry_ele.click()
                    print(f"✅ Inquiry {inquiry_number} found — calling Bid_Now()...")
                    self.pause(1)

                    bid = BiddingToOrder(driver)
                    bid.Bid_Now()  # ✅ final correct call
                    return

                except:
                    driver.swipe(start_x, start_y, start_x, end_y, 800)
                    self.pause(1)

            # Go back
            try:
                driver.find_element(AppiumBy.ID, "com.trukkeruae.trukker_vender:id/ivBack").click()
            except:
                pass

            self.pause(1)

            # Collapse section
            try:
                expand_btn.click()
            except:
                pass

        print("❌ Inquiry not found in any section.")
