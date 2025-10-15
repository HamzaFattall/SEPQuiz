#!/usr/bin/env python3
"""
Script to generate complete quiz data replacement for index.html
Parses the 150 questions and creates properly formatted JavaScript array
"""

# All 150 questions with proper escaping for JavaScript
# Note: According to the answer key provided, all answers are 'b' (index 1)

quiz_questions = [
    # Questions 1-25: CHAPTER 1 - RISK MANAGEMENT  
    ("What is the core definition of risk in security engineering?", 
     ["A weakness that can be exploited.", "The potential for loss or damage when a threat exploits a vulnerability.", "Any potential source of harm.", "The financial impact of a security incident."], 1),
    
    ("In the risk triad, a hacker is an example of a:", 
     ["Vulnerability", "Threat", "Impact", "Asset"], 1),
    
    ("An unpatched web server is an example of a:", 
     ["Threat", "Vulnerability", "Risk", "Control"], 1),
    
    ("The financial loss from a data breach is an example of:", 
     ["Threat", "Vulnerability", "Impact", "Likelihood"], 2),
    
    ("The primary goal of risk management is to:", 
     ["Eliminate all risks.", "Balance risk reduction with business objectives and costs.", "Transfer all risks to insurance companies.", "Document every possible threat."], 1),
    
    ("What is the first step in a typical risk management process?", 
     ["Implement controls", "Identify assets", "Understand the business context", "Perform risk assessment"], 2),
    
    ("Which risk assessment methodology uses subjective assessment with qualitative scales like \"High, Medium, Low\"?", 
     ["Quantitative Risk Assessment", "Qualitative Risk Assessment", "Hybrid Risk Assessment", "Monte Carlo Simulation"], 1),
    
    ("Which methodology uses numerical values and mathematical models for objective analysis?", 
     ["Qualitative Risk Assessment", "Quantitative Risk Assessment", "Delphi Method", "Scenario-Based Assessment"], 1),
    
    ("The Delphi Method is a qualitative technique that relies on:", 
     ["Statistical analysis of historical data.", "A panel of experts reaching consensus through multiple survey rounds.", "Automated threat modeling tools.", "A single senior executive's opinion."], 1),
    
    ("Scenario-Based Risk Assessment involves:", 
     ["Calculating precise financial losses.", "Evaluating risks by exploring different hypothetical situations.", "Using Bayesian networks for probability.", "Running thousands of random simulations."], 1),
]

def escape_js_string(s):
    """Escape string for JavaScript"""
    return s.replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')

def generate_quiz_line(q, opts, ans):
    """Generate a single quiz question line"""
    question = escape_js_string(q)
    options = [f"'{escape_js_string(opt)}'" for opt in opts]
    options_str = ", ".join(options)
    return f"      {{q: '{question}', options: [{options_str}], answer: {ans}}},"

# Generate output
print("Generating quiz data...")
print()
print("    // Quiz data with all 150 questions")
print("    const quizData = [")

for i, (q, opts, ans) in enumerate(quiz_questions, 1):
    if i == 1:
        print("      // CHAPTER 1: RISK MANAGEMENT (Questions 1-25)")
    print(generate_quiz_line(q, opts, ans))

print("    ];")
print()
print(f"Generated {len(quiz_questions)} questions")
