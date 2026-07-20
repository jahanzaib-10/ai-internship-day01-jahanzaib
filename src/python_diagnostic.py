# Task 1: Student Performance Analyzer
def calculate_student_statistics(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list of scores.")
    if len(scores) == 0:
        raise ValueError("The score list cannot be empty.")
        
    total_students = len(scores)
    valid_scores = []
    
    for s in scores:
        if not isinstance(s, (int, float)):
            raise TypeError(f"Invalid data type found: {s}. Scores must be numbers.")
        if s < 0 or s > 100:
            raise ValueError(f"Score {s} is outside the valid range (0-100).")
        valid_scores.append(s)
        
    avg_score = sum(valid_scores) / total_students
    highest = max(valid_scores)
    lowest = min(valid_scores)
    
    passed = 0
    failed = 0
    for s in valid_scores:
        if s >= 50:
            passed += 1
        else:
            failed += 1
            
    return {
        "Total students": total_students,
        "Average score": avg_score,
        "Highest score": highest,
        "Lowest score": lowest,
        "Passed": passed,
        "Failed": failed
    }


# Task 2: Grade Classification
def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
        
    if 85 <= score <= 100:
        return 'A'
    elif 70 <= score <= 84:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    else:
        return 'F'


# Task 3: Word Frequency Counter
def count_words(text):
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    
    text_lower = text.lower()
    
    for p in ['.', ',', '!', '?', ';', ':', '-']:
        text_lower = text_lower.replace(p, '')
        
    words = text_lower.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_words[:3]
    
    return word_count, top_three


# Task 4: Data Cleaning Exercise
def clean_student_data(student_records):
    if not isinstance(student_records, list):
        raise TypeError("Student records must be a list of dictionaries.")
        
    cleaned_records = []
    valid_scores = []
    
    for record in student_records:
        if not isinstance(record, dict):
            continue
            
        name = record.get("name")
        score = record.get("score")
        
        if not name or score is None:
            continue
            
        if isinstance(score, (int, float)) and (0 <= score <= 100):
            cleaned_records.append(record)
            valid_scores.append(score)
            
    avg_valid_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    
    return cleaned_records, avg_valid_score


# Task 5: Error Handling & Main Interactive Execution
if __name__ == "__main__":
    print("=== AI Internship: Python Diagnostic Program ===\n")
    
    try:
        # Task 1 & Task 2 User Input
        user_input = input("Enter student scores separated by commas (e.g., 78, 45, 89, 56): ")
        
        if user_input.strip() == "":
            scores = [78, 45, 89, 56, 32, 67, 91, 49]
            print("No input provided. Using default scores:", scores)
        else:
            scores = [float(s.strip()) for s in user_input.split(",")]
            
        # Task 1 Execution
        stats = calculate_student_statistics(scores)
        print("\n--- Task 1: Student Statistics Result ---")
        for key, value in stats.items():
            print(f"{key}: {value}")
            
        # Task 2 Execution: Assigning grades to EVERY user-entered score
        print("\n--- Task 2: Grade Classification for Entered Scores ---")
        for s in scores:
            grade = assign_grade(s)
            print(f"Score: {s} -> Assigned Grade: {grade}")
            
        # Task 3 Execution
        print("\n--------------------------------------------------")
        user_text = input("Enter a sentence for Word Frequency Counter: ")
        
        if not user_text.strip():
            user_text = "Artificial intelligence is changing the world. Intelligence systems are becoming more powerful, and artificial intelligence is being used in many industries."
            print("Using default text for Word Frequency...")
            
        full_dict, top_three = count_words(user_text)
        
        print("\n--- Task 3: Word Frequency Results ---")
        print("1. Full Word Frequency Dictionary:")
        print(full_dict)
        
        print("\n2. Three Most Frequent Words:")
        for w, freq in top_three:
            print(f"   Word: '{w}' -> Frequency: {freq}")
            
        # Task 4 Execution
        print("\n--------------------------------------------------")
        print("--- Task 4: Data Cleaning Exercise ---")
        student_records = [
            {"name": "Ali", "score": 78},
            {"name": "Sara", "score": None},
            {"name": "Ahmed", "score": 92},
            {"name": "", "score": 65},
            {"name": "Zainab", "score": 110},
            {"name": "Usman", "score": 48}
        ]
        
        cleaned, avg_valid = clean_student_data(student_records)
        print("Cleaned Records:", cleaned)
        print(f"Average Valid Score: {avg_valid:.2f}")
       

    except Exception as e:
        # Task 5: Error Handling Output
        print(f"\n[Task 5 Error Caught]: {e}")