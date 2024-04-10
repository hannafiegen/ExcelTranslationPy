import pandas as pd
from googletrans import Translator


translator = Translator()

def translate_text(text, src_lang='de', dest_lang='en'):
    """
    Translate text from src_lang to dest_lang. Handles both words and sentences.
    """
    try:
       
        text = str(text)
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

def translate_excel(file_path, sheet_name):
    """
    Translate all text entries across all columns of an Excel sheet, including column names.
    Handles both individual words and sentences.
    """
   
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
   
    translated_columns = [translate_text(col) for col in df.columns]
    df.columns = translated_columns
    for column in df.columns:
        df[column] = df[column].apply(lambda x: translate_text(x) if isinstance(x, str) else x)
    
    # Write the translated DataFrame to a new Excel file
    output_file = "translated_" + file_path
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Translation completed. Check '{output_file}' for the translated Excel file.")


file_path = "DIN SPEC 91475_digitaler Anhang.xlsx"  # Update this with your Excel file path
sheet_name = "Betriebsdaten"  # Update this with your sheet name
translate_excel(file_path, sheet_name)
