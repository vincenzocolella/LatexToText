import re
import string


def clean_latex(filepath):
    # Extract text from LaTeX document
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
        
        # Remove everything between \newtcblisting{code}[1]{ and }
        pattern5 = r'\\newtcblisting\{code\}\[1\]\{[\s\S]*?\}'
        text = re.sub(pattern5, '', text, flags=re.DOTALL)
        
        # Remove everything between '% ' and '\n'
        pattern5 = r'(%).*?(\n)'
        text = re.sub(pattern5, r'\2', text)
        
        # Remove everything between '{' and '}'
        pattern3 = r'({).*?(})'
        text = re.sub(pattern3, r'\1\2', text)
        
        # Remove everything between '[' and ']'
        pattern7 = r'(\[).*?(\])'
        text = re.sub(pattern7, r'\1\2', text)
        
        # Remove everything between '%\' and '}'
        pattern1 = r'(%\\).*?(})'
        text = re.sub(pattern1, r'\1\2', text)
        
        # Remove everything between '\', '{' and '}'
        pattern2 = r'(\\).*?({).*?(})'
        text = re.sub(pattern2, r'\1\2\3', text)
        

        
        # Remove everything between '%\' and '\n'
        pattern4 = r'(%\\).*?(\n)'
        text = re.sub(pattern4, r'\2', text)
        
        
        # Remove everything between '\begin{comment}' and '\end{comment}'
        pattern6 = r'\\begin\{comment\}.*?\\end\{comment\}'
        text = re.sub(pattern6, '', text)
    
        # Remove LaTeX commands
        text = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^\}]*\})?', '', text)

        # Remove special characters
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)


    return text
    

if __name__ == '__main__':
    import argparse
    import os
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='path to LaTeX document')
    args = parser.parse_args()

    input_filepath = args.filepath
    output_filepath = os.path.join(os.path.dirname(input_filepath), 'output.txt')

    text = clean_latex(input_filepath)

    with open(output_filepath, 'w') as f:
        f.write(text)

    print(f"Plain text version of {input_filepath} saved to {output_filepath}")