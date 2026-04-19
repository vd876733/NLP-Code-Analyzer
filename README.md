# NLP-Based Code Semantic Analyzer 

A sophisticated hybrid tool that combines **Abstract Syntax Tree (AST)** static analysis with **Transformer-based Natural Language Processing** to provide deep insights into Python source code.

##  Key Features
- **Semantic Summarization:** Utilizes the `Salesforce/codet5-small` Transformer model to generate human-readable summaries of complex logic.
- **Static Code Analysis:** Parses Python AST to identify technical debt, including:
  - Long Method detection (25+ lines).
  - Ambiguous variable naming (Single-letter violations).
- **Hybrid Validation Layer:** A custom heuristic engine that prevents AI hallucinations, ensuring professional-grade report output.
- **Resource Optimized:** Designed to run efficiently on standard CPU environments without requiring massive GPU memory.

---

##  Theoretical Framework

### 1. Transformer Architecture (Encoder-Decoder)
The project utilizes a **Transformer** model, specifically **CodeT5**. Unlike older RNN or LSTM models, Transformers use a **Self-Attention Mechanism**. This allows the model to weigh the importance of different parts of the code simultaneously. 

* **The Encoder:** Processes the input Python code and represents it as a high-dimensional vector space (latent space).
* **The Decoder:** Generates English text by predicting the next token based on the encoder's output and previously generated words.

### 2. Abstract Syntax Trees (AST)
For "Code Smell" detection, the system uses **Static Analysis** via AST. Instead of reading the code as plain text, the `ast` module parses it into a tree structure where each node represents a linguistic construct (like a `FunctionDef` or `Assign`). This allows the tool to calculate "depth" and identify "Ambiguous Identifiers" without executing the code.

### 3. Decoding Strategies: Greedy vs. Beam Search
During summary generation, the model must choose the most likely next word. 
* **Greedy Search:** Picks the word with the highest immediate probability. While fast, it can lead to repetitive "loops."
* **Beam Search:** Explores multiple "beams" (paths) simultaneously and chooses the path with the highest overall sequence probability.
* **Repetition Penalty:** We implemented a penalty factor to discount tokens that have already appeared, forcing the model to remain descriptive.

---

## 🛠️ Technical Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12+ |
| **NLP Model** | Salesforce CodeT5-Small (HuggingFace) |
| **Core Libraries** | `transformers`, `torch`, `ast` |
| **Version Control** | Git with specialized `.gitignore` |

---

##  Installation & Setup

1. **Clone the Repository:**
   ```powershell
   git clone [https://github.com/vd876733/NLP-Code-Analyzer.git](https://github.com/vd876733/NLP-Code-Analyzer.git)
   cd NLP-Code-Analyzer

Create a Virtual Environment:

PowerShell
python -m venv nlp_env_stable
.\nlp_env_stable\Scripts\activate
Install Dependencies:

PowerShell
pip install torch transformers
 Usage Example
Run the analyzer on any Python file (e.g., test.py):

PowerShell
python main.py test.py
Sample Output:

Summary: This project implements a DataProcessor class focused on mathematical analysis. The code features recursive logic for factorial calculations and complex data processing using trigonometric and square root functions.

Code Smells:

Long Method: 'process_and_analyze_complex_dataset_with_logic' (26 lines)

Ambiguous Variable Name: 'a'

 Project Challenges Solved
Git Bloat: Successfully managed repository size by excluding 200MB+ PyTorch binaries using specialized .gitignore rules.

Model Hallucination: Solved "Repetition Loops" in small Transformer models by implementing a Regex-based validation fallback.

Semantic Gap: Bridged the gap between computer instructions and human intent through fine-tuned prompting and attention steering.

 Author
Your Name NLP & Software Engineering Student


### Final Steps to Finish:
1.  **Open Notepad** (or VS Code).
2.  **Paste** the code above.
3.  **Save as** `README.md` (make sure it's not `README.md.txt`).
4.  **Push to GitHub:**
    ```powershell
    git add README.md
    git commit -m "Complete documentation with theoretical framework"
    git push origin main
    ```

You are now 100% ready for your submission and presentation! Good luck!
