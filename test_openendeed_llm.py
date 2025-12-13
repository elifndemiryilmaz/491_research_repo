"""
Mock version - Shows Issue 2A output format without calling OpenAI API
Use this if you have connection issues
"""
from app.ai.schemas.text_evaluation_schemas import (
    TextEvaluationResult,
    DimensionScore,
    EvaluationDimension
)
from datetime import datetime

def show_mock_evaluation():
    """Display mock evaluation results to demonstrate Issue 2A functionality"""
    
    print("="*80)
    print("ISSUE 2A: Core LLM Text Evaluation Engine - PROOF OF FUNCTIONALITY")
    print("(Mock Data - Demonstrates Output Format)")
    print("="*80)
    
    print("\n" + "-"*80)
    print("TEST CASE: Email Simulation Evaluation")
    print("-"*80)
    
    question = "Write an email to a customer who received a damaged product"
    response = """Dear Valued Customer,

I sincerely apologize for the inconvenience you experienced with your recent order. 
I understand how frustrating it must be to receive a damaged product.

I have immediately initiated a full refund to your original payment method, which 
should appear within 3-5 business days. Additionally, I'd like to offer you a 20% 
discount code for your next purchase.

If you'd prefer a replacement instead, please let me know and I'll arrange expedited 
shipping at no cost.

Thank you for your patience and understanding.

Best regards,
Customer Service Team"""
    
    print(f"\n📋 Question:\n{question}")
    print(f"\n📝 Candidate Response:\n{response}")
    
    print("\n" + "-"*80)
    print("EVALUATING WITH LLM... (Mock Result)")
    print("-"*80)
    
    # Create mock evaluation result
    dimension_scores = [
        DimensionScore(
            dimension=EvaluationDimension.EMPATHY,
            score=88.0,
            justification="The response demonstrates strong empathy by acknowledging the customer's frustration and showing understanding of their situation.",
            strengths=[
                "Sincere apology provided immediately",
                "Acknowledged customer emotions explicitly ('I understand how frustrating')",
                "Offered multiple solutions showing care"
            ],
            improvements=[
                "Could personalize by using customer's name if available",
                "Could acknowledge specific details about the damage"
            ]
        ),
        DimensionScore(
            dimension=EvaluationDimension.CLARITY,
            score=92.0,
            justification="The message is well-structured, easy to understand, and clearly communicates all necessary information.",
            strengths=[
                "Logical flow from apology to solution to next steps",
                "Clear timeline provided (3-5 business days)",
                "Specific action items mentioned"
            ],
            improvements=[
                "Could include contact information for follow-up questions"
            ]
        ),
        DimensionScore(
            dimension=EvaluationDimension.PROFESSIONALISM,
            score=90.0,
            justification="The tone is appropriately professional while remaining warm and customer-focused.",
            strengths=[
                "Professional greeting and closing",
                "Courteous language throughout",
                "Maintains professional tone while being empathetic"
            ],
            improvements=[
                "Could add a case reference number for tracking"
            ]
        ),
        DimensionScore(
            dimension=EvaluationDimension.PROBLEM_SOLVING,
            score=85.0,
            justification="The response provides concrete solutions and alternatives, addressing the customer's concern effectively.",
            strengths=[
                "Immediate refund initiated (proactive)",
                "Additional compensation offered (20% discount)",
                "Alternative solution provided (replacement option)"
            ],
            improvements=[
                "Could explain steps being taken to prevent future occurrences",
                "Could provide estimated delivery time for replacement option"
            ]
        )
    ]
    
    overall_score = 88.8
    
    # Display results
    print("\n" + "="*80)
    print("EVALUATION RESULTS")
    print("="*80)
    
    print(f"\nOverall Score: {overall_score:.1f}/100")
    print(f"Recommendation: PASS")
    
    print("\nDimensional Scores:")
    print("-"*80)
    for dim_score in dimension_scores:
        print(f"\n🔹 {dim_score.dimension.value.upper()}: {dim_score.score:.1f}/100")
        print(f"   Justification: {dim_score.justification}")
        if dim_score.strengths:
            for strength in dim_score.strengths:
                print(f"      • {strength}")
        if dim_score.improvements:
            print(f"   📝 Improvements:")
            for improvement in dim_score.improvements:
                print(f"      • {improvement}")
    
    print("\n💬 Overall Feedback:")
    print("-"*80)
    print("Excellent customer service email that effectively addresses the customer's concern ")
    print("with strong empathy, clear communication, and practical solutions. The response is ")
    print("professional, well-structured, and goes beyond simply resolving the issue by offering ")
    print("additional compensation. Minor improvements could include personalization and providing ")
    print("more specific tracking or follow-up information.")
    
    print("\n📊 Evaluation Metadata:")
    print("-"*80)
    print(f"   Model: gpt-4o-mini")
    print(f"   Tokens Used: 1,247 (estimated)")
    print(f"   Time Taken: 4.32s (estimated)")
    
    print("\n" + "="*80)
    print("="*80)
    print("\nNote: This is mock data showing the evaluation format.")
    print("The actual implementation uses GPT-4o-mini for real-time evaluation.")

if __name__ == "__main__":
    show_mock_evaluation()

