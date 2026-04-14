import google.generativeai as genai

genai.configure(api_key="AIzaSyDrdX3m10NxQslzyPNMPHTdS-jwYybDKvk")

models = genai.list_models()

for m in models:
    if "generateContent" in m.supported_generation_methods:
        print(m.name)