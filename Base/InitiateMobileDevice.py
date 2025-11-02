import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


class InitiateMobileDevice:
    driver = None

    @staticmethod
    def start_session():
        """Start the Appium session and return driver."""
        # capabilities = {
        #     "platformName": "Android",
        #     "appium:automationName": "UiAutomator2",
        #     "appium:deviceName": "emulator-5554",  # Change if using real device
        #     "appium:app": "C:\\Users\\kisho\\Downloads\\Loadboard_Android_1.0.60_QA.apk",
        #     "appium:noReset": True
        # }
        #
        # print("🚀 Starting Appium session...")
        # options = UiAutomator2Options().load_capabilities(capabilities)

        # --- App Package & APK Path ---
        app_package = "com.trukkeruae.trukker_vender"
        app_path = "C:\\Users\\kisho\\Downloads\\Loadboard_Android_1.0.60_QA.apk"

        # --- Desired Capabilities skeleton (no app yet) ---
        capabilities = {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": "emulator-5554",
            "appium:noReset": False,  # force fresh state
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }

        print("📦 Checking if app is installed...")

        # --- Check and Uninstall App if exists ---
        try:
            temp_driver = webdriver.Remote(
                "http://127.0.0.1:4723/wd/hub",
                UiAutomator2Options().load_capabilities({
                    "platformName": "Android",
                    "appium:automationName": "UiAutomator2",
                    "appium:deviceName": "emulator-5554",
                    "appium:noReset": True
                })
            )

            if temp_driver.is_app_installed(app_package):
                print("🧹 App already installed — uninstalling...")
                temp_driver.remove_app(app_package)
                time.sleep(3)
            else:
                print("✅ App not installed — will install fresh")

            temp_driver.quit()

        except Exception:
            print("⚠️ Device not ready or app not found — continuing fresh")

        # ✅ Add APK to capabilities now
        capabilities["appium:app"] = app_path

        # --- Start Appium session with fresh install ---
        options = UiAutomator2Options().load_capabilities(capabilities)
        print("🚀 Installing & launching app fresh...")

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
