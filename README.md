# MovieMate

**MovieMate** is a personal movie and TV show collection tracker with support for adding media, episodes, reviews, and even AI-generated reviews using OpenAI's GPT models.


### Backend Setup (FastAPI)

**clone** the github repository : git clone https://github.com/anugrahs123/moviemate-backend.git

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in `backend/` and add your OpenAI key:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```


---

## Feature List

### ✅ Core Features

- Add and manage **Movies/TV Shows**
- Add and track **Episodes** with progress
- Rate and review on movies/shows
- **AI-Generated Reviews** using OpenAI GPT based on user notes
- Recommended movies and shows based on user rating on different genre
- Filter/sort list by genre, platform, or status
- Clean and responsive UI using Material UI

### 📚 Technical Stack

- **Frontend:** React, Vite, TypeScript, Material UI
- **Backend:** FastAPI, SQLite, OpenAI API

---

