from feature_extraction import extract_features

def extract_features(url):
    features = [len(url), 1 if "https" in url else 0]  # Example
    return features
