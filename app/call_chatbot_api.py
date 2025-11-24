import requests

# ✅ Phải dùng HTTPS

HOST = "https://agentic-chatbot-api--ts1krju.mangosea-bfac89e0.southeastasia.azurecontainerapps.io/" #"http://localhost:8001/" #"http://127.0.0.1:8001/" # "https://agentic-chatbot-api.mangosea-bfac89e0.southeastasia.azurecontainerapps.io:8000/"
url = HOST + "chat"

# ✅ Payload đúng format
payload = {
    "userid": "nhan.ngothanh12",
    "question": "cho tôi thông tin về vay mua nhà ở vib"
}

try:
    # ✅ Có timeout để tránh treo
    response = requests.post(url, json=payload, timeout=30)
    print(f"User Question: {payload.get('question')}")
    print(f"Response: {response}")

    if response.status_code == 200:
        data = response.json()
        print("✅ Kết quả trả về:")
        print(f"User Question: {payload.get('question')}")
        print(f"UserID : {data.get('userid')}")
        print(f"Question: {data.get('question')}")
        print(f"Answer  : {data.get('answer')}")
    else:
        print(f"❌ Lỗi {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print("🚫 Lỗi kết nối:", e)
