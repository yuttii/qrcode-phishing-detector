# Phishing QR Code Detector

A modular Python web application designed to detect, decode, and analyze QR codes for potential phishing threats and malicious redirects.

## Project Structure

| File | Description |
|---|---|
| `site.py` | Main entry point — Streamlit-based web interface for file uploads and visual feedback |
| `scanner.py` | Processing module handling image conversion, manipulation, and QR code detection |
| `classqreader.py` | Core ML-based `QReader` class for accurate QR code recognition and decoding |
| `test.py` | Unit test suite (`unittest`) verifying scanning behavior and security evaluation logic |
| `requirements.txt` | Full list of required external dependencies |

## Features

- **ML-Powered Detection** — leverages machine learning models to locate and decode QR codes even from low-quality or distorted images
- **Interactive Web UI** — built with Streamlit for instant image upload and analysis
- **Heuristic Security Analysis** — evaluates decoded URLs against common phishing indicators: suspicious keywords, dangerous top-level domains, and unencrypted protocols
- **Automated Testing** — test cases to ensure reliability and catch regressions

## Requirements

- Python 3.8+
- OpenCV
- NumPy
- Streamlit
- QReader dependencies (`qrdet`, `pyzbar`)

## Installation

Clone the repository:

```bash
git clone https://github.com/yuttii/qrcode-phishing-detector.git
cd qrcode-phishing-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit server:

```bash
streamlit run site.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`) in your browser.

## Running Tests

Run the full test suite from the project root:

```bash
python -m unittest discover tests
```

## How It Works

1. **Upload** — the user uploads a QR code image (JPG, JPEG, or PNG) via the Streamlit interface
2. **Decoding** — the image is processed through OpenCV and the ML-backed scanner module to extract the underlying text or URL
3. **Analysis** — the extracted link is checked against risk patterns (deceptive keywords, insecure HTTP, suspicious TLDs, etc.) and a safety verdict is presented to the user
