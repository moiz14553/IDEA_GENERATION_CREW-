
markdown
# 🚀 **Project CrewAI – Idea Generation Crew**

This project implements an **AI Agents Crew Flow** to automate:

✅ Generating innovative project topics  
✅ Brainstorming ideas for the topics  
✅ Describing the project crew structure

using **CrewAI Framework** combined with **LiteLLM Gemini API**.

---

## 📂 **Project Structure**

```

project\_crew/
├── .env
├── main.py
├── project.py
├── crews/
│   └── ideas\_crew/
│       └── idea\_crew\.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
└── requirements.txt

````

---

## 💡 **How It Works**

### `main.py` – Flow Orchestration

1. **generate_topic**  
   Uses Gemini API to generate an innovative project topic suitable for a diverse team.

2. **brainstorm_ideas**  
   Uses Gemini API to brainstorm ideas based on the generated topic.

3. **describe_project_crew**  
   Calls the `IdeaCrew` to describe team members and finalises the flow.

---

### `idea_crew.py` – Agents & Tasks

✅ **Agents Defined**
- `Project Manager`: Generates topics  
- `Idea Brainstormer`: Brainstorms ideas  
- `Crew Describer`: Describes crew structure

✅ **Tasks Defined**
- Each task is linked to its agent with `expected_output`.

✅ **Crew Defined**
- Combines all agents and tasks into a single crew named **Idea Generation Crew** for execution.

---

## ⚙️ **Setup Instructions**

1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd project_crew
````

2. **Create virtual environment and activate**

   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

3. **Add your environment variables**

   Create a `.env` file with your LiteLLM / Gemini API keys:

   ```
   LITELLM_API_KEY=your_api_key_here
   ```

4. **Run the project**

   ```bash
   uv run projectflow
   ```

---

## ✅ **Example Output**

```
STEP 1 topic:
Developing a Personalized Microbiome-Based Wellness Platform

STEP 2 ideas:
- At-home microbiome testing kit integration
- AI-powered analysis and personalized diet plans
- User-friendly reports and benchmarking tools

STEP 3 crew description:
This crew is composed of diverse members with unique skills.

✔️ Flow Finished Successfully
```

---

## 📌 **Dependencies**

Ensure these are included in your `requirements.txt`:

```
crewai==0.102.0
litellm
python-dotenv
uv
```

---

## 🌟 **Future Enhancements**

* Integrate **database storage** for outputs
* Deploy as a **FastAPI microservice**
* Build a **frontend UI** to display flow outputs interactively
* Extend with **task automation for client project proposals**

---

### 🔗 **Credits**

Built using [CrewAI](https://crewai.com) and [LiteLLM](https://github.com/BerriAI/litellm).

---

> **Maintained by:** ABDULREHMAN
> For AI, automation, and backend projects.
