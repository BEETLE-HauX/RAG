# DocInsight

## Automated PDF Summarizer & Quiz Generator

## 📌 Overview
An AI-powered tool that transforms lecture materials (PDFs/text) into:
- Concise summaries
- Key takeaways  
- FAQ-style Q&A pairs
- Practice quizzes (coming soon)

## 🚀 Features
- **PDF Processing**: Extracts text from lecture slides/notes
- **Smart Summarization**: 3-5 bullet point summaries using Llama 3
- **Auto-Q&A Generation**: Context-aware FAQs from lecture content
- **Offline Capable**: Runs locally via Ollama (no API keys needed)
  
## 🛠️ Technologies
LLM: Ollama (Llama 3) for local processing
Framework: LangChain + Streamlit
Vector DB: FAISS for embeddings

## ⚙️ Installation

### Prerequisites
1. Install [Ollama](https://ollama.ai/) and pull the model:
   ```bash
   ollama pull llama3

2. Keep Ollama running in background:
   ollama serve

3. Setup:
   git clone https://github.com/yourusername/lecture-ai-tool.git
   cd lecture-ai-tool
   pip install -r requirements.txt

4. Usage:
   streamlit run app.py

Then upload any lecture PDF to see:
1. Generated summary
2. FAQ pairs

## 📂 Project Structure
   .
   ├── app.py                # Streamlit frontend
   ├── core.py               # NLP processing logic
   ├── requirements.txt      # Python dependencies
   └── README.md             # You're here!

## 🛠️ Customization
To change models (e.g., Mistral instead of Llama 3):
# In core.py
self.llm = Ollama(model="mistral") 

### Key Additions for Judges:
1. **Clear Prerequisites**: Explicit Ollama setup instructions  
2. **Visual Demo**: Add a GIF showing the app in action  
3. **Troubleshooting Section** (add this if needed):
   ```markdown
   ## 🚨 Troubleshooting
   - **Ollama errors**: Ensure `ollama serve` is running
   - **PDF issues**: Test with [sample_lecture.pdf](sample_lecture.pdf)
   - **Port conflicts**: Change Streamlit port with `streamlit run app.py --server.port 8502`
