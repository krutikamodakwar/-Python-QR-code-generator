import qrcode

data = input("Enter text or URL: ")
img = qrcode.make(data)

# Give full path where you want to save
path = "projectresume"

print(f"QR code saved at: {path}")

