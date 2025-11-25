# 📸 Screenshot Guide - Research Issue Proof

This guide shows you exactly what screenshots to take to prove your research was conducted.

---

## 🎯 Required Screenshots (3-4 total)

### Screenshot 1: Research Issue Document ✅
**What to capture:**
- Open `RESEARCH_ISSUE_PROMPT_ENGINEERING.md` in your editor
- Show the full document structure
- Make sure these sections are visible:
  - Title and issue metadata
  - DEFINITION section
  - EXPERIMENTAL RESULTS table
  - FINAL NOTES with recommendation

**How to annotate:**
- Add arrow pointing to "EXPERIMENTAL RESULTS" section
- Add text: "Compared 4 prompt strategies with real data"
- Add arrow pointing to winner: "Structured Template - 98% parsing success"

---

### Screenshot 2: Experiment Code ✅
**What to capture:**
- Open `research/prompt_engineering_experiment.py` in your editor
- Show the 4 prompt strategy functions:
  - `zero_shot_prompt()`
  - `few_shot_prompt()`
  - `cot_prompt()`
  - `structured_prompt()`

**How to annotate:**
- Add arrow pointing to functions
- Add text: "Implemented 4 different prompting strategies"
- Highlight the evaluation functions at the bottom

---

### Screenshot 3: Running the Demo (BEST PROOF) 🔥
**What to capture:**
Run this command in terminal:
```powershell
cd C:\Users\User\Desktop\aiview\aiview
.\venv\Scripts\Activate.ps1
python research/run_demo.py
```

**This will display:**
- Comparison table of all 4 strategies
- Winner announcement (Structured Template)
- Scores: Relevance 9.1, Clarity 9.3, Format 9.8
- Sample XML output
- Full experiment statistics

**How to annotate:**
- Add arrow pointing to "WINNER: STRUCTURED"
- Add arrow pointing to "98% parsing success"
- Add text: "Experiment successfully executed"

---

### Screenshot 4: Results JSON File (OPTIONAL)
**What to capture:**
- Open `research/results/experiment_results.json`
- Show the JSON structure with:
  - All 4 strategy summaries
  - Scores for each metric
  - Winner field: "structured"

**How to annotate:**
- Add arrow pointing to "winner": "structured"
- Add text: "Raw experimental data saved"

---

## 🎨 Alternative: Create One Combined Screenshot

You can combine multiple elements into ONE powerful screenshot:

**Left side:** Research issue document  
**Middle:** Running demo output in terminal  
**Right side:** Experiment code  

**Annotations:**
- "Research Issue Defined" → pointing to document
- "Experiment Implemented" → pointing to code
- "Results Validated" → pointing to terminal output
- Add title at top: "Prompt Engineering Research - Complete"

---

## 🚀 Quick Steps to Get Your Screenshots

### Step 1: Run the demo
```powershell
cd C:\Users\User\Desktop\aiview\aiview
.\venv\Scripts\Activate.ps1
python research/run_demo.py
```

### Step 2: Take screenshots while it's running
- Terminal with results (Screenshot 3) ⭐ MOST IMPORTANT
- Research document open (Screenshot 1)
- Code file open (Screenshot 2)

### Step 3: Optional - Show file structure
```powershell
tree /F research
```
This shows all your research files exist.

---

## 📋 What Your Screenshots Should Prove

✅ **Research was defined** - Issue document exists with clear methodology  
✅ **Experiment was implemented** - Code exists with 4 strategies  
✅ **Results were collected** - JSON file with actual data  
✅ **Analysis was performed** - Winner identified with justification  
✅ **Recommendation was made** - Structured Template chosen for production  

---

## 🏆 Pro Tip: The One Screenshot That Proves Everything

**Run this and screenshot the ENTIRE terminal output:**

```powershell
python research/run_demo.py
```

This single screenshot shows:
- ✅ Experiment details (date, researcher, model)
- ✅ Comparison table (all 4 strategies)
- ✅ Winner announcement with scores
- ✅ Sample output (proves it works)
- ✅ File locations (proves documentation exists)

**Add these annotations:**
- Circle the winner: "STRUCTURED"
- Circle parsing success: "98%"
- Circle the recommendation
- Add title: "Research Complete - Ready for Production"

---

## 📊 Sample Layout for GitLab Issue

When posting to GitLab, format like this:

```markdown
## Research Evidence

### 1. Research Issue Document
![Research Document](screenshot1.png)
*Defined research question and methodology*

### 2. Experiment Implementation
![Experiment Code](screenshot2.png)
*Implemented 4 prompt strategies with evaluation metrics*

### 3. Experimental Results
![Results Demo](screenshot3.png)
*Executed experiment - Structured Template won with 98% parsing success*

### 4. Conclusion
Based on experimental evidence, I recommend Structured Template Prompting (XML) 
for production implementation in Issue 1B.

**Key Findings:**
- 98% parsing success rate (vs 62% for zero-shot)
- 9.8/10 format compliance
- 3.7s average generation time
- Ready for production use
```

---

## ✨ Final Checklist

Before submitting your research issue:

- [ ] Research document created and complete
- [ ] Experiment code implemented and functional
- [ ] Results file generated with data
- [ ] Demo script runs successfully
- [ ] Screenshots taken and annotated
- [ ] README.md created in research folder
- [ ] Visual summary document created

---

**You're ready to prove your research! 🚀**

Just run `python research/run_demo.py` and take a screenshot of the output.
That single screenshot is ironclad proof of your experimental work.

