from bs4 import BeautifulSoup
import re



# Function to clean HTML and extract text, tags, and attributes
def extract_features_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Extract text
    text = re.sub(r'<.*?>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    features.append(text)

    # Extract tags and attributes
    for tag in soup.find_all(True):
        features.append(f"<{tag.name}>")
        for attr, value in tag.attrs.items():
            features.append(f"{attr}={value}")
    
    return ' '.join(features)

# Clean and extract features
#cleaned_data = [extract_features_from_html(item["html"]) for item in labeled_data]

# Display cleaned data for verification
#for data in cleaned_data:
 #   print(data)
