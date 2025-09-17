"""
Smart Resume Screener - Main Script
Author: Your Name
Date: 2025-09-17
"""

import os
import sys
from modules.extractor import extract_text_from_resume
from modules.preprocess import preprocess_text
from modules.matcher import match_keywords, compute_similarity_score
from modules.report import generate_report

RESUME_FOLDER = "resumes"
JD_FILE = "job_description.txt"
RESULT_FILE = "results.csv"


def main_menu():
    while True:
        print("\n==== Smart Resume Screener ====")
        print("1. Upload Job Description")
        print("2. Process Resumes (PDF/DOC)")
        print("3. Generate Shortlist")
        print("4. Export CSV Report")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            upload_job_description()
        elif choice == '2':
            process_resumes()
        elif choice == '3':
            generate_shortlist()
        elif choice == '4':
            export_report()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

def upload_job_description():
    print("\nPaste the job description below. End input with a blank line:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    with open(JD_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Job description saved to {JD_FILE}.")

def process_resumes():
    print("\nProcessing resumes in 'resumes/' folder...")
    from modules.extractor import extract_text_from_resume
    from modules.preprocess import preprocess_text
    import os
    global resume_data
    resume_data = []
    for fname in os.listdir(RESUME_FOLDER):
        if fname.lower().endswith(('.pdf', '.docx', '.doc')):
            fpath = os.path.join(RESUME_FOLDER, fname)
            try:
                text = extract_text_from_resume(fpath)
                tokens = preprocess_text(text)
                resume_data.append({'file': fname, 'text': text, 'tokens': tokens})
                print(f"Processed: {fname}")
            except Exception as e:
                print(f"Error processing {fname}: {e}")
    print(f"Total resumes processed: {len(resume_data)}")

def generate_shortlist():
    print("\nGenerating shortlist based on JD...")
    from modules.matcher import match_keywords, compute_similarity_score
    global shortlist
    shortlist = []
    if not os.path.exists(JD_FILE):
        print("Job description file not found. Please upload JD first.")
        return
    with open(JD_FILE, 'r', encoding='utf-8') as f:
        jd_text = f.read()
    from modules.preprocess import preprocess_text
    jd_tokens = preprocess_text(jd_text)
    for r in resume_data:
        matched, missing = match_keywords(jd_tokens, r['tokens'])
        score = compute_similarity_score(jd_text, r['text'])
        shortlist.append({
            'name': r['file'].split('.')[0],
            'file': r['file'],
            'score': round(score * 100, 2),
            'matched_keywords': ', '.join(matched),
            'missing_keywords': ', '.join(missing)
        })
    shortlist.sort(key=lambda x: x['score'], reverse=True)
    print("Shortlist generated. Top candidates:")
    for i, cand in enumerate(shortlist[:5]):
        print(f"{i+1}. {cand['name']} - Score: {cand['score']}%")

def export_report():
    print("\nExporting results to CSV...")
    from modules.report import generate_report
    if not shortlist:
        print("No shortlist found. Please generate shortlist first.")
        return
    generate_report(shortlist, RESULT_FILE)

if __name__ == "__main__":
    main_menu()
