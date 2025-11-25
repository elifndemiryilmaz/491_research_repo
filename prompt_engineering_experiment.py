"""
Prompt Engineering Research Experiment
Compares 4 strategies for interview question generation

Author: Elif Naz Demiryılmaz
Date: November 25, 2025

Methodology based on:
- Brown et al. (2020): Few-shot learning [NeurIPS]
- Wei et al. (2022): Chain-of-thought prompting [NeurIPS]
- Liu et al. (2023): Survey of prompting methods [ACM Computing Surveys]
- Beurer-Kellner et al. (2023): Structured prompting [PLDI]

References:
[1] Brown, T., et al. (2020). Language Models are Few-Shot Learners. NeurIPS.
[2] Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning. NeurIPS.
[3] Liu, P., et al. (2023). Pre-train, Prompt, and Predict. ACM Computing Surveys.
[6] Beurer-Kellner, L., et al. (2023). Prompting Is Programming. PLDI.
"""

import asyncio
import json
import time
from typing import List, Dict
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))

# Test job description
JOB_DESCRIPTION = """
Senior Backend Engineer
Required Skills: Python, FastAPI, PostgreSQL, MongoDB, REST API design
Experience: 5+ years
"""

# ============================================================================
# STRATEGY 1: ZERO-SHOT PROMPTING
# Based on: Kojima et al. (2022) - Large Language Models are Zero-Shot Reasoners
# Description: Direct instruction without examples or reasoning steps
# ============================================================================

def zero_shot_prompt(job_desc: str) -> str:
    """Zero-shot prompting: Direct task instruction without examples [4]"""
    return f"""Generate 5 technical interview questions for this job:

{job_desc}

Generate diverse questions covering technical skills, problem-solving, and system design."""


# ============================================================================
# STRATEGY 2: FEW-SHOT PROMPTING
# Based on: Brown et al. (2020) - Language Models are Few-Shot Learners
# Description: Provides 2-3 examples to guide the model's output format
# ============================================================================

def few_shot_prompt(job_desc: str) -> str:
    """Few-shot prompting: Learning from examples [1]"""
    return f"""Generate 5 technical interview questions for this job:

{job_desc}

Here are examples of good questions:

Example 1:
Question: "Explain the difference between synchronous and asynchronous programming in Python."
Type: Technical
Difficulty: Mid

Example 2:
Question: "How would you design a REST API for a high-traffic e-commerce platform?"
Type: System Design
Difficulty: Senior

Now generate 5 similar questions for the job above."""


# ============================================================================
# STRATEGY 3: CHAIN-OF-THOUGHT PROMPTING
# Based on: Wei et al. (2022) - Chain-of-Thought Prompting Elicits Reasoning
# Description: Asks model to show reasoning before generating output
# ============================================================================

def cot_prompt(job_desc: str) -> str:
    """Chain-of-thought prompting: Explicit reasoning steps [2]"""
    return f"""Generate 5 technical interview questions for this job:

{job_desc}

Before generating questions, think step-by-step:
1. What are the key skills required?
2. What experience level is needed?
3. What question types would be most revealing?

Then generate 5 questions based on your analysis."""


# ============================================================================
# STRATEGY 4: STRUCTURED TEMPLATE PROMPTING (XML)
# Based on: Beurer-Kellner et al. (2023) - Prompting Is Programming
# Description: Enforces strict output format using XML schema
# ============================================================================

def structured_prompt(job_desc: str) -> str:
    """Structured template prompting: XML-enforced format [6]"""
    return f"""Generate 5 technical interview questions for this job:

{job_desc}

You MUST respond in this EXACT XML format:

<questions>
  <question>
    <id>1</id>
    <text>What is the time complexity of binary search?</text>
    <type>technical</type>
    <difficulty>mid</difficulty>
    <category>algorithms</category>
  </question>
  <question>
    <id>2</id>
    <text>Describe your experience with microservices architecture</text>
    <type>behavioral</type>
    <difficulty>senior</difficulty>
    <category>system_design</category>
  </question>
</questions>

Generate 5 questions following this XML structure EXACTLY."""


# ============================================================================
# EVALUATION FUNCTIONS
# ============================================================================

def evaluate_relevance(question: str, job_desc: str) -> float:
    """Score relevance to job description (0-10)"""
    keywords = ["python", "fastapi", "postgresql", "mongodb", "rest", "api", "backend"]
    question_lower = question.lower()
    matches = sum(1 for kw in keywords if kw in question_lower)
    return min(10, matches * 1.5)


def evaluate_clarity(question: str) -> float:
    """Score question clarity (0-10)"""
    # Simple heuristics: length, question mark, clear structure
    has_question_mark = "?" in question
    good_length = 20 < len(question.split()) < 100
    no_jargon_overload = question.count("(") < 3
    
    score = 5.0
    if has_question_mark: score += 2
    if good_length: score += 2
    if no_jargon_overload: score += 1
    
    return min(10, score)


def evaluate_format_compliance(response: str, strategy: str) -> float:
    """Score format compliance (0-10)"""
    if strategy == "structured":
        # Check XML structure
        has_xml_tags = "<questions>" in response and "</questions>" in response
        has_question_tags = response.count("<question>") >= 3
        return 10 if (has_xml_tags and has_question_tags) else 3
    else:
        # For others, just check if it looks like questions
        has_numbers = any(str(i) in response for i in range(1, 6))
        has_questions = response.count("?") >= 3
        return 8 if (has_numbers and has_questions) else 5


def try_parse_response(response: str, strategy: str) -> bool:
    """Test if response can be parsed successfully"""
    try:
        if strategy == "structured":
            # Try to parse XML
            return "<questions>" in response and response.count("<question>") >= 3
        else:
            # For others, check if we can extract question-like patterns
            return response.count("?") >= 3 and len(response) > 100
    except Exception:
        return False


# ============================================================================
# EXPERIMENT RUNNER
# ============================================================================

def run_strategy_test(strategy_name: str, prompt_func, iterations: int = 3):
    """Run test for one strategy"""
    print(f"\n{'='*60}")
    print(f"Testing Strategy: {strategy_name.upper()}")
    print(f"{'='*60}")
    
    results = []
    
    for i in range(iterations):
        print(f"\nIteration {i+1}/{iterations}...")
        
        # Generate prompt
        prompt = prompt_func(JOB_DESCRIPTION)
        
        # Measure generation time
        start_time = time.time()
        
        try:
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert technical interviewer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            generation_time = time.time() - start_time
            content = response.choices[0].message.content
            
            # Evaluate response
            # Extract first question for evaluation (simplified)
            first_question = content.split("\n")[0]
            
            relevance = evaluate_relevance(content, JOB_DESCRIPTION)
            clarity = evaluate_clarity(first_question)
            format_compliance = evaluate_format_compliance(content, strategy_name)
            can_parse = try_parse_response(content, strategy_name)
            
            result = {
                "iteration": i + 1,
                "relevance": relevance,
                "clarity": clarity,
                "format_compliance": format_compliance,
                "generation_time": round(generation_time, 2),
                "parsing_success": can_parse,
                "response_length": len(content),
                "sample_output": content[:200] + "..."  # First 200 chars
            }
            
            results.append(result)
            
            print(f"  ✓ Relevance: {relevance:.1f}/10")
            print(f"  ✓ Clarity: {clarity:.1f}/10")
            print(f"  ✓ Format: {format_compliance:.1f}/10")
            print(f"  ✓ Time: {generation_time:.2f}s")
            print(f"  ✓ Parseable: {'Yes' if can_parse else 'No'}")
            
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            results.append({"error": str(e)})
    
    # Calculate averages
    valid_results = [r for r in results if "error" not in r]
    
    if valid_results:
        avg_relevance = sum(r["relevance"] for r in valid_results) / len(valid_results)
        avg_clarity = sum(r["clarity"] for r in valid_results) / len(valid_results)
        avg_format = sum(r["format_compliance"] for r in valid_results) / len(valid_results)
        avg_time = sum(r["generation_time"] for r in valid_results) / len(valid_results)
        parse_success_rate = sum(1 for r in valid_results if r["parsing_success"]) / len(valid_results) * 100
        
        print(f"\n{'-'*60}")
        print(f"AVERAGE RESULTS - {strategy_name.upper()}")
        print(f"{'-'*60}")
        print(f"Relevance:         {avg_relevance:.1f}/10")
        print(f"Clarity:           {avg_clarity:.1f}/10")
        print(f"Format Compliance: {avg_format:.1f}/10")
        print(f"Generation Time:   {avg_time:.2f}s")
        print(f"Parsing Success:   {parse_success_rate:.0f}%")
        
        summary = {
            "strategy": strategy_name,
            "avg_relevance": round(avg_relevance, 2),
            "avg_clarity": round(avg_clarity, 2),
            "avg_format": round(avg_format, 2),
            "avg_time": round(avg_time, 2),
            "parse_success_rate": round(parse_success_rate, 0),
            "total_iterations": iterations,
            "successful_iterations": len(valid_results)
        }
        
        return summary, results
    
    return None, results


# ============================================================================
# MAIN EXPERIMENT
# ============================================================================

def main():
    print("\n" + "="*60)
    print("PROMPT ENGINEERING RESEARCH EXPERIMENT")
    print("Comparing 4 Strategies for Interview Question Generation")
    print("="*60)
    
    strategies = [
        ("zero_shot", zero_shot_prompt),
        ("few_shot", few_shot_prompt),
        ("chain_of_thought", cot_prompt),
        ("structured", structured_prompt)
    ]
    
    all_summaries = []
    all_results = {}
    
    for strategy_name, prompt_func in strategies:
        summary, results = run_strategy_test(strategy_name, prompt_func, iterations=3)
        
        if summary:
            all_summaries.append(summary)
        all_results[strategy_name] = results
        
        time.sleep(2)  # Rate limiting
    
    # Final comparison
    print("\n\n" + "="*60)
    print("FINAL COMPARISON")
    print("="*60)
    print(f"\n{'Strategy':<20} {'Relevance':<12} {'Clarity':<10} {'Format':<10} {'Time':<8} {'Parse%':<8}")
    print("-" * 68)
    
    for summary in all_summaries:
        print(f"{summary['strategy']:<20} "
              f"{summary['avg_relevance']:<12.1f} "
              f"{summary['avg_clarity']:<10.1f} "
              f"{summary['avg_format']:<10.1f} "
              f"{summary['avg_time']:<8.2f}s "
              f"{summary['parse_success_rate']:<8.0f}%")
    
    # Determine winner
    print("\n" + "="*60)
    best_strategy = max(all_summaries, 
                       key=lambda x: (x['avg_format'] * 0.4 + 
                                     x['avg_relevance'] * 0.3 + 
                                     x['avg_clarity'] * 0.2 + 
                                     x['parse_success_rate'] * 0.1))
    
    print(f"🏆 RECOMMENDED STRATEGY: {best_strategy['strategy'].upper()}")
    print(f"   Overall Score: {best_strategy['avg_format'] * 0.4 + best_strategy['avg_relevance'] * 0.3:.1f}")
    print("="*60)
    
    # Save results
    with open("research/results/experiment_results.json", "w") as f:
        json.dump({
            "summaries": all_summaries,
            "detailed_results": all_results,
            "winner": best_strategy['strategy']
        }, f, indent=2)
    
    print("\n✓ Results saved to research/results/experiment_results.json")


if __name__ == "__main__":
    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  WARNING: OPENAI_API_KEY not set!")
        print("Set it with: $env:OPENAI_API_KEY = 'your-key-here'")
        print("\nRunning in DEMO MODE with simulated results...\n")
        
        # Demo mode - show what the experiment would do
        print("="*60)
        print("DEMO MODE - Simulated Results")
        print("="*60)
        print("\nThis experiment would test 4 prompt strategies:")
        print("  1. Zero-Shot Prompting")
        print("  2. Few-Shot Prompting")
        print("  3. Chain-of-Thought Prompting")
        print("  4. Structured Template Prompting (XML)")
        print("\nEach strategy would be tested 3 times with real OpenAI API calls.")
        print("\nTo run real experiment: Set OPENAI_API_KEY and run again.")
    else:
        main()

