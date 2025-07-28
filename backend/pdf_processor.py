import pdfplumber
import re
from typing import List, Dict, Union
import json
import os

class PDFProcessor:
    def __init__(self):
        self.title = ""
        self.outline = []
        self.heading_patterns = [
            (r'^(?P<h1>^[0-9]+\..+)$', "H1"),
            (r'^(?P<h2>^[0-9]+\.[0-9]+\..+)$', "H2"),
            (r'^(?P<h3>^[0-9]+\.[0-9]+\.[0-9]+\..+)$', "H3"),
            (r'^(?P<h1>^[A-Z][A-Z0-9\s]+[^a-z]$)', "H1"),  # All caps, no lowercase
            (r'^(?P<h2>^[A-Z][a-zA-Z0-9\s]+:$)', "H2"),    # Title case with colon
            (r'^(?P<h1>^[A-Z][a-zA-Z0-9\s]+$)', "H1"),     # Title case
        ]

    def extract_outline(self, pdf_path: str) -> Dict[str, Union[str, List[Dict]]]:
        """Extract title and headings from PDF"""
        with pdfplumber.open(pdf_path) as pdf:
            # Extract title from first page's first line
            first_page = pdf.pages[0]
            first_text = first_page.extract_text()
            if first_text:
                self.title = first_text.split('\n')[0].strip()
            
            # Process each page for headings
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if not text:
                    continue
                
                for line in text.split('\n'):
                    line = line.strip()
                    if not line:
                        continue
                    
                    for pattern, level in self.heading_patterns:
                        match = re.match(pattern, line)
                        if match:
                            self.outline.append({
                                "level": level,
                                "text": line,
                                "page": page_num
                            })
                            break
        
        return {
            "title": self.title,
            "outline": self.outline
        }

    def process_pdfs_in_directory(self, input_dir: str, output_dir: str):
        """Process all PDFs in input directory and save JSONs to output directory"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for filename in os.listdir(input_dir):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(input_dir, filename)
                result = self.extract_outline(pdf_path)
                
                output_filename = os.path.splitext(filename)[0] + '.json'
                output_path = os.path.join(output_dir, output_filename)
                
                with open(output_path, 'w') as f:
                    json.dump(result, f, indent=2)
                
                print(f"Processed {filename} -> {output_filename}")