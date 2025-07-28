from pdf_processor import PDFProcessor
import os

def main():
    input_dir = '/app/input'
    output_dir = '/app/output'
    
    processor = PDFProcessor()
    processor.process_pdfs_in_directory(input_dir, output_dir)

if __name__ == "__main__":
    main()