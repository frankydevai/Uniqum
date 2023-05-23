import pdfkit

def convert_pdf_to_html(pdf_file_path, output_html_path):
    """
    Converts a PDF file to HTML using pdfkit library.
    :param pdf_file_path: Path to the PDF file.
    :param output_html_path: Path to save the HTML output file.
    """
    try:
        options = {
            'encoding': 'utf-8',
        }
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_file(pdf_file_path, output_html_path, configuration=config)

        print('Conversion complete. HTML file saved at:', output_html_path)
    except Exception as e:
        print('Error occurred during conversion:', str(e))

# Example usage
pdf_file = 'Apple.pdf'
output_html_file = 'output.html'
convert_pdf_to_html(pdf_file, output_html_file)
