import pandas as pd

faq_data = {
    "question": [
        "How to reset my password?",
        "What is the refund policy?",
        "How do I contact support?"
    ],
    "answer": [
        "Click 'Forgot Password' on the login page.",
        "Refunds are processed within 7 business days.",
        "Email support@yourcompany.com or call +91-1234567890."
    ]
}

df = pd.DataFrame(faq_data)
df.to_csv("data/product_faq.csv", index=False)
print("Synthetic CSV created at data/product_faq.csv")
