from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain
from sample_data import *

def run_pipeline(resume):

    print("\n==============================")
    print("Processing Resume")
    print("==============================")

    # Step 1: Extraction
    extracted = extract_chain(resume)
    extracted = str(extracted)
    print("\n Extracted Data:\n", extracted)

    # Step 2: Matching
    matched = match_chain(extracted, job_description)
    matched = str(matched)
    print("\n Match Result:\n", matched)

    # Step 3: Scoring
    score = score_chain(matched)
    score = str(score).strip()
    print("\n Score:\n", score)

    # Step 4: Explanation
    explanation = explain_chain(score, matched)
    explanation = str(explanation)
    print("\n Explanation:\n", explanation)


# Run all test cases
if __name__ == "__main__":
    print("\n STRONG CANDIDATE")
    run_pipeline(strong_resume)

    print("\n AVERAGE CANDIDATE")
    run_pipeline(average_resume)

    print("\n WEAK CANDIDATE")
    run_pipeline(weak_resume)