import importlib
import concurrent.futures
import time
import os
import subprocess

# -------- Auto Update Section --------
def auto_update():
    try:
        print("🔄 Checking for updates...")
        # বর্তমান ডিরেক্টরি git repo হলে pull করবে
        if os.path.exists(".git"):
            subprocess.run(["git", "pull"], check=True)
        else:
            print("⚠️ No .git folder found, skipping update.")
    except Exception as e:
        print(f"❌ Auto update failed: {e}")
# -------------------------------------


def send_requests(phone_number, amount):
    total_apis = 150
    request_count = 0

    # Dynamically import API modules
    api_modules = [f"api{i}" for i in range(1, total_apis + 1)]
    functions = []

    for api_module in api_modules:
        try:
            module = importlib.import_module(api_module)
            functions.append(module.send_request)
        except ModuleNotFoundError:
            print(f"Module {api_module} not found. Skipping...")

    if not functions:
        print("No API modules loaded. Exiting...")
        return

    print(f"Loaded {len(functions)} APIs.")

    # Send requests in rounds
    while request_count < amount:
        print(f"Starting round {request_count + 1}...")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Use API functions in parallel
            futures = [
                executor.submit(func, phone_number)
                for func in functions
            ]

            for future in concurrent.futures.as_completed(futures):
                try:
                    response = future.result()
                    print(f"Response: {response}")
                except Exception as e:
                    print(f"Error in request: {e}")

        request_count += 1
        time.sleep(1)  # Optional: Add delay between rounds

    print("All requests completed!")


if __name__ == "__main__":
    # প্রথমেই auto update হবে
    auto_update()

    # Input from the user
    phone_number = input("Enter phone number (without country code): ")
    amount = int(input("Enter number of request rounds: "))

    # Validate inputs
    if len(phone_number) != 11 or not phone_number.isdigit():
        print("Invalid phone number. Must be 11 digits.")
    elif amount <= 0:
        print("Amount must be greater than 0.")
    else:
        send_requests(phone_number, amount)
