import subprocess, sys, os

PROJECT_PATH = r"C:\Users\kisho\PycharmProjects\FrameWork_Playwright"
os.chdir(PROJECT_PATH)

def run_cmd(label, command):
    print(f"\n==============================")
    print(f"🚀 Starting: {label}")
    print("==============================")

    # Run command and stream output live (so we see PyTest logs)
    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"❌ FAILED: {label}")
        sys.exit(result.returncode)

    print(f"✅ PASSED: {label}")

print("🔥 Starting End-to-End test flow...\n")

# ✅ Inquiry Creation Test (1st test)
run_cmd(
    "Inquiry Creation Test",
    [
        "pytest", "-s", "-v",
        "--maxfail=1",
        "--disable-warnings",
        "--exitfirst",
        "TestCases/test_TC001_AInquiryCreationUAECB.py"
    ]
)

print("\n📌 Triggering Order Booking Test execution...")  # 👈 confirmation line

# ✅ Order Booking Test (2nd test)
run_cmd(
    "Order Booking Test",
    [
        "pytest", "-s", "-v",
        "--maxfail=1",
        "--disable-warnings",
        "--exitfirst",
        "--strict-markers",
        "TestCases/test_TC001_OrderBookig.py"
    ]
)

print("\n🎉 ✅ Full workflow completed successfully!")
