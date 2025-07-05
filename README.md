

```markdown
# 🚀 Project Crew Idea Generator

This project uses **CrewAI agents and flows** to generate innovative project topics, brainstorm ideas, and describe the project crew structure automatically.

---

## 📂 **Project Structure**

```

project\_crew/
├── src/
│   └── project\_crew/
│       ├── main.py
│       └── crews/
│           └── ideas\_crew/
│               └── idea\_crew\.py
├── .env
├── requirements.txt
└── README.md

````

---

## 💡 **What it does**

✅ **Generates an innovative project topic**  
✅ **Brainstorms ideas for the generated topic**  
✅ **Describes the crew members with their roles and skills**

It integrates:

- **CrewAI framework** for agent orchestration  
- **LiteLLM + Gemini API** for text generation  
- **Python dotenv** for environment configuration

---

## ⚙️ **How to Run**

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Create a `.env` file and add your API keys:

```env
OPENAI_API_KEY=your_api_key_here
```

4. **Run the project**

```bash
uv run projectflow
```

---

## 📝 **Main Components**

### `main.py`

* Defines the **Flow class `Project`**
* Contains steps:

  * `generate_topic()`: Calls Gemini to generate a topic
  * `brainstorm_ideas()`: Brainstorms ideas for the topic
  * `describe_project_crew()`: Kicks off the `IdeaCrew` to describe crew members

---

### `idea_crew.py`

* Defines **CrewAI agents**:

  * Project Manager
  * Crew Describer
  * Idea Brainstormer
* Defines **tasks** for each agent
* Creates a **Crew** to run all tasks sequentially

---

## 🖼️ **Sample Output**

![Project Output Screenshot](C:\Users\3TEE\OneDrive\Pictures\Screenshots)

---

## 🙌 **Author**

* **Name:** ABDUL REHMAN
* **Role:** AI Developer | CrewAI Learner

---

## ⭐ **Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

---

### 🔗 **Connect**

* [LinkedIn](https://www.linkedin.com/in/abdul-rehman-1333a3290/)
* [GitHub](https://github.com/moiz14553)

---



---

Let me know if you need:

- `.gitignore` for Python + VSCode  
- License file template  
- GitHub repository description draft for professional upload today.
```
