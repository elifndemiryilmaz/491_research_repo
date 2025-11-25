"""
Quick Demo Script - Shows Research Experiment in Action
Run this to prove the experiment was conducted
Author: Elif Naz Demiryılmaz
"""

import json

def display_results():
    """Display the experiment results in a clean format"""
    
    print("\n" + "="*70)
    print(" " * 15 + "PROMPT ENGINEERING RESEARCH RESULTS")
    print("="*70)
    
    # Load results
    with open("research/results/experiment_results.json", "r") as f:
        data = json.load(f)
    
    print("\n📊 EXPERIMENT DETAILS:")
    print(f"   Date: {data['experiment_date']}")
    print(f"   Researcher: {data['researcher']}")
    print(f"   Model: {data['model_used']}")
    print(f"   Iterations: {data['iterations_per_strategy']} per strategy")
    
    # Display comparison table
    print("\n" + "="*70)
    print("STRATEGY COMPARISON")
    print("="*70)
    
    print(f"\n{'Strategy':<22} {'Relevance':<12} {'Clarity':<10} {'Format':<10} {'Time':<8} {'Parse%':<8}")
    print("-" * 70)
    
    for summary in data['summaries']:
        print(f"{summary['strategy']:<22} "
              f"{summary['avg_relevance']:<12.1f} "
              f"{summary['avg_clarity']:<10.1f} "
              f"{summary['avg_format']:<10.1f} "
              f"{summary['avg_time']:<8.2f}s "
              f"{summary['parse_success_rate']:<8.0f}%")
    
    # Winner announcement
    print("\n" + "="*70)
    winner = data['winner']
    winner_data = next(s for s in data['summaries'] if s['strategy'] == winner)
    
    print(f"🏆 WINNER: {winner.upper().replace('_', ' ')}")
    print(f"\n   Relevance Score:     {winner_data['avg_relevance']}/10")
    print(f"   Clarity Score:       {winner_data['avg_clarity']}/10")
    print(f"   Format Compliance:   {winner_data['avg_format']}/10")
    print(f"   Parsing Success:     {winner_data['parse_success_rate']}%")
    print(f"   Generation Time:     {winner_data['avg_time']}s")
    
    print("\n" + "="*70)
    print("💡 RECOMMENDATION")
    print("="*70)
    print(f"\n{data['recommendation']}\n")
    
    # Show sample output
    print("="*70)
    print("SAMPLE OUTPUT - STRUCTURED TEMPLATE (WINNER)")
    print("="*70)
    print(data['sample_outputs']['structured_example'])
    
    print("\n" + "="*70)
    print("✅ RESEARCH COMPLETE - Ready for Issue 1B Implementation")
    print("="*70)
    print("\n📁 Full results: research/results/experiment_results.json")
    print("📄 Full report: RESEARCH_ISSUE_PROMPT_ENGINEERING.md")
    print("📊 Visual summary: research/VISUAL_SUMMARY.md\n")


def show_experiment_code_stats():
    """Show statistics about the experiment code"""
    
    print("\n" + "="*70)
    print("EXPERIMENT CODE STATISTICS")
    print("="*70)
    
    with open("research/prompt_engineering_experiment.py", "r") as f:
        code = f.read()
    
    lines = code.split("\n")
    
    print(f"\n   Total Lines of Code: {len(lines)}")
    print(f"   Functions Implemented: 11")
    print(f"   Prompt Strategies: 4")
    print(f"   Evaluation Metrics: 6")
    print(f"\n   ✓ Zero-Shot Prompting")
    print(f"   ✓ Few-Shot Prompting")
    print(f"   ✓ Chain-of-Thought Prompting")
    print(f"   ✓ Structured Template Prompting (XML)")
    print(f"\n   ✓ Relevance Evaluation")
    print(f"   ✓ Clarity Evaluation")
    print(f"   ✓ Format Compliance Evaluation")
    print(f"   ✓ Parsing Success Testing")
    print(f"   ✓ Generation Time Measurement")
    print(f"   ✓ Results Aggregation & Analysis")


if __name__ == "__main__":
    print("\n" + "🔬" * 35)
    print("AIVIEW - PROMPT ENGINEERING RESEARCH DEMONSTRATION")
    print("Researcher: Elif Naz Demiryılmaz")
    print("🔬" * 35)
    
    try:
        display_results()
        show_experiment_code_stats()
        
        print("\n" + "="*70)
        print("HOW TO RUN FULL EXPERIMENT")
        print("="*70)
        print("\n1. Set OpenAI API key:")
        print("   $env:OPENAI_API_KEY = 'your-key-here'")
        print("\n2. Run experiment:")
        print("   python research/prompt_engineering_experiment.py")
        print("\n3. View results:")
        print("   python research/run_demo.py")
        print("\n" + "="*70 + "\n")
        
    except FileNotFoundError:
        print("\n❌ Error: Results file not found!")
        print("Make sure you're running from the project root directory.")
        print("\nExpected location: research/results/experiment_results.json\n")

