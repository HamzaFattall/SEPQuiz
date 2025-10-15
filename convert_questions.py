#!/usr/bin/env python3
"""
Script to convert quiz questions from text format to JavaScript array format
"""

questions_text = """What is the core definition of risk in security engineering?
a) A weakness that can be exploited.
b) The potential for loss or damage when a threat exploits a vulnerability.
c) Any potential source of harm.
d) The financial impact of a security incident.

In the risk triad, a hacker is an example of a:
a) Vulnerability
b) Threat
c) Impact
d) Asset

An unpatched web server is an example of a:
a) Threat
b) Vulnerability
c) Risk
d) Control

The financial loss from a data breach is an example of:
a) Threat
b) Vulnerability
c) Impact
d) Likelihood

The primary goal of risk management is to:
a) Eliminate all risks.
b) Balance risk reduction with business objectives and costs.
c) Transfer all risks to insurance companies.
d) Document every possible threat.

What is the first step in a typical risk management process?
a) Implement controls
b) Identify assets
c) Understand the business context
d) Perform risk assessment

Which risk assessment methodology uses subjective assessment with qualitative scales like "High, Medium, Low"?
a) Quantitative Risk Assessment
b) Qualitative Risk Assessment
c) Hybrid Risk Assessment
d) Monte Carlo Simulation

Which methodology uses numerical values and mathematical models for objective analysis?
a) Qualitative Risk Assessment
b) Quantitative Risk Assessment
c) Delphi Method
d) Scenario-Based Assessment

The Delphi Method is a qualitative technique that relies on:
a) Statistical analysis of historical data.
b) A panel of experts reaching consensus through multiple survey rounds.
c) Automated threat modeling tools.
d) A single senior executive's opinion.

Scenario-Based Risk Assessment involves:
a) Calculating precise financial losses.
b) Evaluating risks by exploring different hypothetical situations.
c) Using Bayesian networks for probability.
d) Running thousands of random simulations.

In a Risk Matrix (Heat Map), how is the risk score typically calculated?
a) Likelihood + Impact
b) Likelihood × Impact
c) Impact ÷ Likelihood
d) (Likelihood + Impact) ÷ 2

In a risk matrix, a risk with "Likely" probability and "Major" impact would be placed in which category?
a) Low
b) Moderate
c) High
d) Extreme

Monte Carlo Simulations are used for:
a) Qualitative threat analysis.
b) Modeling uncertainty through random sampling and probability distributions.
c) Creating security policies.
d) Implementing access controls.

Bayesian Networks are valuable in risk assessment because they:
a) Provide simple, static risk scores.
b) Can update probability estimates as new data becomes available.
c) Are required by all compliance regimes.
d) Eliminate the need for any data input.

The choice between qualitative and quantitative risk assessment depends on all of the following EXCEPT:
a) The organization's goals
b) The available data and resources
c) The level of precision required
d) The personal preference of the IT manager

Risk assessment is considered a(n) ongoing and iterative process because:
a) It is legally required to be repeated yearly.
b) New threats and information emerge over time.
c) The initial assessment is always wrong.
d) It keeps security teams busy.

The Systematic process of risk management includes all of the following key components EXCEPT:
a) Risk identification
b) Risk analysis and evaluation
c) Risk elimination
d) Risk mitigation

The component "Scoping" in risk assessment refers to:
a) Identifying all possible threats in the world.
b) Defining the boundaries of what is being assessed.
c) Calculating the financial cost of risks.
d) Assigning blame for security failures.

Risk evaluation primarily involves:
a) Implementing firewalls.
b) Assessing the likelihood and impact of risks to determine their significance.
c) Identifying assets.
d) Training employees.

The final step in the risk management process is:
a) Implement Security Controls
b) Develop Security Policies
c) Continuous Improvement
d) Perform Risk Assessment

What does a Hybrid risk assessment methodology combine?
a) Elements of IT and Physical security
b) Elements of qualitative and quantitative approaches
c) Elements of different compliance standards
d) Elements of threat and vulnerability analysis

The output of a risk analysis is used primarily for:
a) Blaming departments for security lapses.
b) Informing decision-makers and prioritizing mitigation efforts.
c) Replacing all old hardware.
d) Hiring more security staff.

The term "gross profits" and "theft losses" in the risk vs. reward example illustrates:
a) The importance of financial metrics in risk decisions.
b) That shareholders don't care about security.
c) That all theft should be stopped regardless of cost.
d) Security always leads to higher profits.

A "Risk Register" is a crucial tool that serves as a:
a) List of approved security software.
b) Central repository for all risk-related information.
c) Record of employee attendance.
d) Database of customer complaints.

The term "Resource Allocation" in risk management strategy refers to:
a) Giving all departments an equal security budget.
b) Ensuring the most significant risks are prioritized with available resources.
c) Spending the entire budget on the latest security products.
d) Allocating resources only to IT departments."""

# Parse questions
questions = []
current_q = {"question": "", "options": []}
for line in questions_text.strip().split('\n'):
    line = line.strip()
    if not line:
        if current_q["question"] and len(current_q["options"]) == 4:
            questions.append(current_q)
            current_q = {"question": "", "options": []}
        continue
    
    if line.startswith(('a)', 'b)', 'c)', 'd)')):
        current_q["options"].append(line[3:].strip())
    else:
        if current_q["question"]:
            current_q["question"] += " " + line
        else:
            current_q["question"] = line

# Add last question
if current_q["question"] and len(current_q["options"]) == 4:
    questions.append(current_q)

# Answer key (all b = index 1)
answer_key = [1] * 150  # According to the answer key provided, all answers are 'b' which is index 1

# Generate JavaScript format
print("Generated", len(questions), "questions")
for i, q in enumerate(questions[:25]):  # First 25
    opts = q["options"]
    ans = answer_key[i]
    print(f"      {{q: '{q['question']}', options: ['{opts[0]}', '{opts[1]}', '{opts[2]}', '{opts[3]}'], answer: {ans}}},")
