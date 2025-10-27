from appium import webdriver
from appium.options.android import UiAutomator2Options


class InitiateMobileDevice:
    driver = None

    @staticmethod
    def start_session():
        """Start the Appium session and return driver."""
        capabilities = {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": "emulator-5554",  # Change if using real device
            "appium:app": "C:\\Users\\kisho\\Downloads\\Loadboard_Android_1.0.60_QA.apk",
            "appium:noReset": True
        }

        print("🚀 Starting Appium session...")
        options = UiAutomator2Options().load_capabilities(capabilities)

        InitiateMobileDevice.driver = webdriver.Remote(
            "http://127.0.0.1:4723/wd/hub", options=options
        )

        print("✅ App launched successfully.")
        return InitiateMobileDevice.driver

    @staticmethod
    def close_session():
        """Close the Appium session."""
        if InitiateMobileDevice.driver:
            InitiateMobileDevice.driver.quit()
            print("✅ Appium session closed successfully.")
