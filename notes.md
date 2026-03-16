# FastAPI Notes

> Notes from CampusX YouTube Playlist on FastAPI.
> Language: Hinglish (Hindi + English mixed explanation).
> New topics are appended below as transcriptions are provided.

---

<!-- New sections will be appended below this line -->

---

## Topic 5: FastAPI Setup & First API (Hello World)

### 1. Installation & Environment Setup

FastAPI project start karne ke liye sabse pehle ek virtual environment banana recommended hai.

**Steps:**
1. Apne project folder mein terminal open karein (e.g., `api-tutorials`).
2. Virtual environment create karein:
   ```bash
   python -m venv fastapi
   ```
3. Virtual environment activate karein:
   - **Windows:** `fastapi\Scripts\activate`
   - **Mac/Linux:** `source fastapi/bin/activate`
4. FastAPI, Uvicorn (server) aur Pydantic install karein:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
   *(Note: Starlette automatically FastAPI ke install hone par as a dependency include ho jata hai.)*

---

### 2. Creating the First API (`main.py`)

Ek nayi file banayein `main.py` aur usme apna pehla FastAPI code likhein:

```python
from fastapi import FastAPI

# 1. FastAPI ka app object create karna
app = FastAPI()

# 2. Endpoint / Route define karna
@app.get("/")
def hello():
    # 3. Logic: response return karna
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "CampusX is an education platform where you can learn AI."}
```

**Code Explanation:**
- `app = FastAPI()`: Yeh hamari API ka main application object hai.
- `@app.get("/")`: Yeh ek **decorator** hai jo route (URL path) define karta hai. Yahan `/` ka matlab home URL hai (e.g., `localhost:8000/`). `get` HTTP method hai jo data read (fetch) karne ke liye use hota hai. Agar server par data bhejna ho toh `post` request hoti hai.
- `def hello()`: Yeh function us specific route par aane wali requests ko handle karega. Is function ko arguments ki zaroorat nahi hai is basic example mein.
- `return {"message": "Hello World"}`: Jab bhi koi is endpoint ko hit karega, toh yeh Python dictionary automatically browser ko response mein JSON (dictionary) format mein pass ho jayegi.

---

### 3. Running the Server with Uvicorn

Code ko run karne ke liye hum Uvicorn server ka use karte hain. Terminal mein yeh command run karein:

```bash
uvicorn main:app --reload
```

**Command Breakdown:**
- `uvicorn`: ASGI server jo humari application ko serve karega.
- `main`: Python file ka naam (jisme code likha hai, bina `.py` ke, yaani `main`).
- `app`: FastAPI ka object jo humne `main.py` mein create kiya hai (`app = FastAPI()`).
- `--reload`: Yeh flag dev environment mein use hota hai. Jab bhi aap apne code mein kuch change karke save karenge (jaise naya `/about` route add karna), server automatically **reload** ho jayega, aur update ke liye aapko manual usko restart karne ki zaroorat nahi padegi.

URL browser pe visit karne ke baad (e.g., `http://127.0.0.1:8000/`), browser pe API ka JSON response dikhega: `{"message": "Hello World"}`. 
URL mein end mein `/about` append karke aap second endpoint ko bhi hit kar sakte hain.

---

### 4. Interactive Auto-Generated Documentation (`/docs`)

FastAPI ka ek sabse best part aur powerful feature uska auto-generated interactive documentation hai.

- **URL:** Jab apka server run kar raha ho, toh aapko URL mein `/docs` append karna hai (e.g., `http://127.0.0.1:8000/docs`).
- **Swagger UI:** Yeh URL aapko ek Swagger UI page pe le jayega jahan FastAPI automatically aapke saare endpoints (abhi ke liye `/` aur `/about`) ko detect kar ke list kar dega.
- **Interactive Testing:** Is dashboard par endpoints expand karne par **"Try it out"** button ka option deta hai. Aap yahin se **"Execute"** click karke bina kisi third-party software (jaise Postman) ke apni API ko interact aur test kar sakte hain. Wahan aapko Response Body mein apna HTTP response aur baaki HTTP headers (status code 200, wagaira) visible honge.

## Topic 4: Introduction to FastAPI & Its Core Philosophy

### 1. Introduction

FastAPI kya hai? "FastAPI is a modern, high-performance web framework for building APIs with Python."
Yeh ek bahut simple aur powerful framework hai jo Python mein scalable, industry-grade APIs banane ke kaam aata hai.

---

### 2. Core Components of FastAPI

FastAPI internally do famous Python libraries ke upar bana hai:

- **Starlette (The Web/Routing Engine):** Jab aap FastAPI mein API banate hain, toh jo HTTP request aati hai, usko Starlette receive karta hai. Endpoints manage karna aur process hone ke baad wapas HTTP response bhejna Starlette ka kaam hai.
- **Pydantic (The Data Validator):** Python mein by default strict type checking nahi hoti. Pydantic ensure karta hai ki API mein aane wala data correct format (jaise string, int, list) mein ho. Data validation aur type checking ka saara heavy-lifting Pydantic karta hai.

---

### 3. Core Philosophy of FastAPI

FastAPI ko banane ke peeche do main objectvies the. Puraane frameworks (jaise Flask) mein performance aur zyada code likhne ka issue hota tha. FastAPI ne ise solve kiya.

#### Philosophy 1: Fast to Run (High Performance)

FastAPI mein bani APIs bahut fast execute hoti hain aur heavily scalable hoti hain. Iska main reason pichle frameworks (Flask) aur FastAPI ke internal architecture mein difference hai:

**Flask Architecture (WSGI - Synchronous):**
- **Web Server:** Gunicorn
- **SGI Protocol:** WSGI (Web Server Gateway Interface)
- **Library:** Werkzeug
- **Problem:** Yeh **synchronous (blocking)** nature ka hota hai. Ek time par ek hi request process hoti hai. Agar ek request process hone mein der lag rahi hai, toh pichhe ki requests ko wait karna padta hai.
- *Analogy:* Ek waiter (Flask) customer se order leta hai, kitchen mein deta hai, aur jab tak khana ban nahi jata, wahi khada rehta hai (blocking). Woh us samay doosre customer ka order nahi le pata.

**FastAPI Architecture (ASGI - Asynchronous):**
- **Web Server:** Uvicorn
- **SGI Protocol:** ASGI (Asynchronous Server Gateway Interface)
- **Library:** Starlette
- **Solution:** Yeh **asynchronous (non-blocking)** nature ka hota hai. Yeh ek sath multiple concurrent requests handle kar sakta hai. FastAPI Python ke `async` aur `await` features ko aggressively use karta hai.
- *Analogy:* Ek waiter (FastAPI) customer se order leta hai, kitchen mein deta hai. Ushe pata hai khana banne mein time lagega, tab tak woh jakar doosre customer ka order le leta hai (non-blocking). Isse flow rukta nahi hai aur multiple customers efficiently serve hote hain.

#### Philosophy 2: Fast to Code (High Productivity)

FastAPI mein developers ko bahut lamba boilerplate code nahi likhna padta. Iske teen bade reasons hain:

1. **Automatic Input Validation:** Pydantic automatically incoming data ko check aur validate kar leta hai, jisse bad data ki wajah se application break nahi hoti.
2. **Auto-generated Interactive Documentation:** Jaise-jaise aap API ka code likhte hain, FastAPI Swagger UI ki madad se documentation khud generate kar deta hai. Us interactive dashboard par aap seedha apne endpoints ko verify aur test kar sakte hain.
3. **Modern Framework Compatibility:** ML/DL libraries (Scikit-learn, PyTorch, TensorFlow), database wrappers (SQLAlchemy), aur deployment tools (Docker, Kubernetes) ke sath FastAPI bahut smoothly integrate ho jata hai.

---

### 4. Important Terms

| Term | Explanation |
|------|-------------|
| **Starlette** | FastAPI ka HTTP requests receive aur send karne wala internal engine |
| **Pydantic** | Python data validation library jo FastAPI mein API data filter karti hai |
| **WSGI** | Web Server Gateway Interface (Older standard - eg. Flask). Synchronous nature ka hota hai. |
| **ASGI** | Asynchronous Server Gateway Interface (Modern standard - eg. FastAPI). Asynchronous aur high-concurrency handle karta hai. |
| **Uvicorn** | Fast and lightweight ASGI web server for Python applications |
| **Async/Await** | Python syntax jiski madad se non-blocking, asynchronous tasks perform kiye jate hain |
| **Concurrency** | Ek sath multiple requests, tasks ya users ko wait karwaye bina serve karna |

---

### 5. FastAPI in ML/AI/RAG

FastAPI machine learning aur AI ke features ke liye ideally suited kyun hai:

- **Handling Heavy ML Inference:** Ek heavy Deep Learning model prediction karne mein 1-2 seconds ka time le sakta hai. Flask mein itna delay poore server ko rok kar dusre users ko hang kar sakta tha (WSGI blocking). FastAPI ka ASGI architecture aur `async/await` ensures ki jab ML model GPU pe compute ho raha ho, tab API doosre users ke nayi requests lete rahe. 
- **RAG Latency Optimization:** Agentic RAG mein Vector DB query (Pinecone), aur LLM generation (OpenAI/Anthropic APIs) mein delay aati hai (network calls). FastAPI inhe *await* kar deta hai taki latency system choke point na ban paye.
- **Pydantic in AI Systems:** Pydantic sirf HTTP data validation hi nahi, bulk LLMs ka structured JSON output enforce karne mein bhi industry standard ban chuka hai (like in LangChain and LlamaIndex). Isliye sikha hua Pydantic AI applications builder ko double fayda deta hai.

---

### 6. Summary

- **FastAPI** ek modern Python framework hai, built on top of **Starlette** aur **Pydantic**.
- Pydantic incoming API requests ka **Data Validation** sambhalta hai.
- Starlette **HTTP requests/responses management** sambhalta hai.
- Flask jaisi puraani library **WSGI aur Synchronous processing** pe run hoti thi, is wajah se slower aur blocking nature ki thi.
- FastAPI **Uvicorn server aur ASGI Protocol** use karta hai jiske wajah se yeh **Asynchronous** (non-blocking) tarike se concurrent requests handle karta hai (just like a smart waiter).
- FastAPI fast isliye hai kyunki woh **Fast to Run** (ASGI+async) aur **Fast to Code** (Auto-documentation + Input Validation) do primary philosophies par design kiya gaya hai.

---

## Topic 1: What is an API?

### 1. Introduction

API ka full form hai **Application Programming Interface**. Jab bhi do alag software systems ko aapas mein baat karni hoti hai, tab API kaam aati hai. Seedha simple bhasha mein bolein toh API ek **connector** hai jo do software pieces ko join karta hai.

Jaise ek website ka front end aur back end - yeh dono alag hote hain. In dono ko API hi connect karti hai.

---

### 2. Core Concepts

#### Front End vs Back End

| Component | Kya hota hai |
|-----------|-------------|
| Front End | Jo user dikhta hai - forms, buttons, search bar, video scroll, etc. |
| Back End | Behind the scenes logic - database se data fetch karna, search algorithm, business rules, etc. |
| API | In dono ke beech ka bridge / connector |

#### Request-Response Flow

Ek typical web request ka flow kuch aisa hota hai:

```
User (Front End)
     |
     |  -- Request --> API
                         |
                         |  -- Request --> Back End (Server)
                                              |
                                         Database se data fetch
                                              |
                         <-- Response -- Back End
                         |
     <-- Response (JSON format) -- API
     |
User ko result dikha diya (Front End)
```

> Example: Udemy website par "AI Agents" search karo. Vo request API ke paas jaati hai. API us request ko back end ko deti hai. Back end database mein search karke result API ko deta hai. API us result ko JSON format mein front end ko return karti hai. Front end display karta hai.

#### Rules, Protocols, and Data Formats

API sirf connect nahi karti - yeh kuch **defined rules** ke andar kaam karti hai:

- **Protocol:** Web APIs generally HTTP/HTTPS protocol use karti hain.
- **Data Format:** Data generally **JSON** (JavaScript Object Notation) format mein transfer hota hai.

---

### 3. Code Example

JSON format ka ek simple example jo API response mein aata hai:

```json
{
  "query": "AI Agents",
  "results": [
    {
      "course_id": 101,
      "title": "AI Agents with LangChain",
      "instructor": "John Doe",
      "price": 499
    },
    {
      "course_id": 102,
      "title": "Agentic RAG Systems",
      "instructor": "Jane Smith",
      "price": 699
    }
  ]
}
```

Yahi structured format front end ko milta hai aur wo isko user ke saamne display karta hai.

---

### 4. Important Terms

| Term | Explanation |
|------|-------------|
| **API** | Application Programming Interface - do softwares ke beech connector |
| **Front End** | User-facing part of an application (UI) |
| **Back End** | Server-side logic and database operations |
| **HTTP/HTTPS** | Protocol jis par web APIs communicate karti hain |
| **JSON** | JavaScript Object Notation - API response ka standard data format |
| **Request** | Client (front end) ki taraf se server ko bheja gaya message |
| **Response** | Server ki taraf se wapas aaya hua data |
| **Protocol** | Ek defined set of rules jiske andar communication hoti hai |

#### Restaurant Analogy (Samajhne ka sabse aasaan tarika)

```
Customer (Front End)   ---->  Waiter (API)  ---->  Kitchen / Chef (Back End)
      ^                                                      |
      |                                                      |
      <-------- Waiter khana lekar aata hai (Response) ------
```

- **Customer** = Front End (aap)
- **Waiter** = API
- **Kitchen/Chef** = Back End
- **Menu Card** = Protocol (kya order kar sakte ho, kya nahi)
- **Plate presentation** = Data Format (kaise data return hoga)

---

### 5. FastAPI in ML/AI/RAG

API concept ML/AI mein bahut fundamental hai:

- **ML Model Serving:** Jab aap ek trained ML model (jaise classification, regression, NLP) ko production mein deploy karte ho, tab FastAPI ke through us model ko ek API ke roop mein expose karte ho. Front end ya koi bhi client us API ko call karke prediction le sakta hai.

- **RAG Pipeline:** Retrieval-Augmented Generation mein bhi multiple components hote hain - vector database, LLM, embedding model. Inhe aapas mein connect karne ke liye APIs use hoti hain. For example:
  ```
  User Query --> FastAPI Endpoint --> Embedding Model --> Vector DB Search --> LLM --> Response
  ```

- **AI Agents:** Agentic systems mein ek agent dusre tools ya services ko API calls ke through access karta hai (tool use / function calling).

- **OpenAI, HuggingFace, Gemini APIs:** Yeh sab third-party APIs hain jo LLMs ko expose karti hain. Aap in APIs ko call karke apni application mein AI capabilities add karte ho - wahi concept jo is lesson mein samjhaya.

---

### 6. Summary

- API ek connector hai jo do software components (front end aur back end) ko communicate karne deta hai.
- Yeh defined **protocols** (HTTP) aur **data formats** (JSON) follow karta hai.
- Best analogy: **Waiter in a restaurant** - customer aur kitchen ke beech mediator.
- ML/AI mein APIs ka role bahut critical hai - model serving, RAG pipelines, aur agentic AI sab APIs par depend karte hain.
- FastAPI is concept ka ek modern, fast, aur Python-friendly implementation hai.

---

## Topic 2: Need for APIs - API Ki Zaroorat Kyun Padi?

### 1. Introduction

Pehle samajhte hain ki **pre-API era** mein websites kaise banti thi, aur phir dekhte hain ki kya problem aayi jiske wajah se APIs ka invention hua. Do badi problems thi jinhe APIs ne solve kiya.

---

### 2. Core Concepts

#### Pre-API Era: Monolithic Architecture

Jab APIs exist nahi karti thi, tab poori website ko ek single application ki tarah banaya jata tha. Iska naam hai **Monolithic Architecture**.

Ek single folder/directory ke andar:
- Front end ka code bhi hota tha
- Back end ka code bhi hota tha

Dono ek doosre se **tightly coupled** hote the - matlab ek mein change aata toh poori application affect hoti thi.

```
[Monolithic Application - single folder]
├── front_end/   (HTML, CSS, JS)
└── back_end/    (Python/Java logic + database calls)
        |
   [Database]
```

> Front end aur back end directly ek doosre se baat karte the bina kisi API ke, kyunki dono ek hi application ka part the.

---

#### Problem 1: Third-Party Data Sharing Impossible Tha

**IRCTC Example:**

Maan lo IRCTC ki website hai jisme ek `fetch_trains(station1, station2, date)` function hai jo database se train information fetch karta hai.

Ab MakeMyTrip, Yatra, Ixigo jaisi companies chahti hain ki unhe bhi yeh train data mile (per-request basis pe revenue model ke saath).

**Options jo kaam nahi karte Monolithic mein:**

| Option | Problem |
|--------|---------|
| Direct database access dena | Dangerous - third party data corrupt kar sakti hai |
| Back end access dena | Back end independent application nahi hai, poori app se tightly coupled hai |

Isliye Monolithic architecture mein **apna data kisi third party ke saath share karna possible nahi tha**. Bahut bada business restriction tha yeh.

#### Problem 2: Multi-Platform Era (Smartphone Revolution)

2008-2012 ke beech smartphone revolution aaya. Suddenly companies ko ek hi data ke liye **teen platforms** ke liye applications banani padi:

| Platform | Technology |
|----------|-----------|
| Website | HTML/CSS/JS |
| Android App | Java / Kotlin |
| iOS App | Swift |

Monolithic approach mein isका matlab tha **teen alag-alag monolithic applications** maintain karna:
- Teen alag databases
- Teen alag back ends
- Teen alag teams - extra cost
- Ek jagah update karo toh baaki dono bhi manually update karo

---

#### Solution: API Architecture (Decoupled Architecture)

Dono problems ka ek hi solution nikla - **Back end ko Front end se decouple karo** aur us back end ko API ke through publicly accessible banao.

```
                    [Single Database]
                           |
                    [Single Back End]
                           |
                      [API Layer]
                    /     |      \
         [Website]  [Android]  [iOS App]
         Front End  App FE      FE
                           |
              [MakeMyTrip / Yatra / Ixigo]
              (Third party consumers)
```

**Do cheezein jo tune ki:**
1. Back end ko front end se **decouple** kar diya - ab dono alag independent applications hain.
2. Back end ko **API ke through internet par publicly visible** bana diya.

> Ab koi bhi (apna front end ya third party) is API ke endpoints ko hit karke data access kar sakta hai - directly database ya back end ko touch kiye bina.

---

#### Endpoints Kya Hote Hain?

API ek **set of endpoints** hoti hai. Endpoint ek special function hota hai jo:
- Internet par publicly available hota hai
- Ek URL ke through access kiya ja sakta hai
- Input leta hai, back end function call karta hai, output JSON mein return karta hai

Example endpoint:
```
GET https://irctc.com/trains?from=Delhi&to=Mumbai&date=2025-03-01
```

Yeh URL hit karte hi:
1. API ka `trains` endpoint trigger hota hai
2. Wo back end ke `fetch_trains()` function ko call karta hai
3. Back end database se data fetch karta hai
4. Result JSON format mein wapas aata hai

---

#### JSON - Universal Data Format Kyun?

MakeMyTrip Java mein bana ho sakta hai, Yatra Python mein, Ixigo PHP mein. API ko response ek aisa format mein dena hoga jo **har programming language samajh sake**.

Isliye **JSON (JavaScript Object Notation)** use hota hai - yeh ek **universal data format** hai.

```json
{
  "from": "Delhi",
  "to": "Mumbai",
  "date": "2025-03-01",
  "trains": [
    {
      "train_no": "12951",
      "name": "Rajdhani Express",
      "departure": "16:55",
      "arrival": "08:35"
    },
    {
      "train_no": "12953",
      "name": "August Kranti Rajdhani",
      "departure": "17:40",
      "arrival": "10:58"
    }
  ]
}
```

> Python dictionary jaisa hi dikhta hai JSON. Java, Python, PHP - sab JSON ko parse aur process kar sakte hain.

---

### 3. Code Example

**Monolithic vs API Architecture comparison:**

```
--- MONOLITHIC (Pre-API) ---

[Frontend Code]  <-- tightly coupled -->  [Backend Code]
                                                |
                                           [Database]

Problem: Sab kuch ek hi application mein band.
Third party access impossible. Multi-platform = teen alag apps.


--- API ARCHITECTURE (Modern) ---

[Website FE] ---|
[Android FE] ---|---> [API Layer] ---> [Backend] ---> [Database]
[iOS FE]     ---|
[MakeMyTrip] ---|

Benefit: Ek backend, ek database, n number of frontends.
```

---

### 4. Important Terms

| Term | Explanation |
|------|-------------|
| **Monolithic Architecture** | Ek hi codebase mein front end + back end dono. Tightly coupled. |
| **Tightly Coupled** | Ek component change karo toh dusra bhi affect hota hai |
| **Decoupling** | Front end aur back end ko alag-alag independent applications mein todna |
| **Endpoint** | API ka ek specific URL/function jo ek particular kaam karta hai |
| **JSON** | JavaScript Object Notation - language-agnostic universal data format |
| **Third Party** | Koi aur company/software jo aapki API consume kare (e.g., MakeMyTrip) |
| **API Layer** | Backend ke aage ek protective interface jo external access manage karta hai |
| **HTTP Protocol** | Web communication ka standard protocol jo API requests/responses mein use hota hai |

---

### 5. FastAPI in ML/AI/RAG

Yahi architecture ML/AI mein exactly same tarah kaam karta hai:

- **ML Model as a Service:** Ek trained model (e.g., sentiment classifier, image detector) ko FastAPI endpoint ke through expose karo. Koi bhi client - chahe web app ho, mobile app ho, ya koi aur service - is endpoint ko call karke predictions le sakta hai. Exactly IRCTC wala model.

  ```
  [React Frontend] ---|
  [Flutter App]    ---|---> [FastAPI Endpoint] ---> [ML Model] ---> Prediction
  [Another API]    ---|
  ```

- **RAG System:** RAG pipeline mein bhi yahi decoupling hoti hai. LLM ek alag service hai, vector database ek alag service hai. FastAPI inhe glue karta hai aur ek single endpoint ke through user ko answer deta hai.

- **AI Agent Tools:** LangChain / LlamaIndex agents mein "tools" basically FastAPI endpoints hote hain. Agent un endpoints ko call karta hai jab zaroorat ho - exactly jaise MakeMyTrip ne IRCTC API call ki.

- **Constraint & Security:** API layer mein aap rate limiting, authentication (API keys), input validation laga sakte ho - exactly jaise IRCTC apni API mein constraints lagata. Yeh back end ko direct exposure se bachata hai.

---

### 6. Summary

- **Pre-API era** mein Monolithic Architecture use hota tha - sab ek hi application mein bundled.
- Monolithic ki 2 badi problems thi:
  1. Third-party data sharing impossible (tightly coupled back end)
  2. Multi-platform (web + android + iOS) ke liye teen alag apps maintain karne padte the
- **Solution:** Back end ko decouple karo aur API layer ke through internet par expose karo.
- Ab **ek database + ek backend + API = n number of frontends** support kar sakta hai.
- **JSON** universal data format hai - koi bhi language parse kar sakti hai.
- **Endpoint** = API ka ek publicly accessible function jiska ek specific URL hota hai.
- FastAPI exactly yahi kaam karta hai ML/AI mein - models aur services ko decoupled endpoints ke through accessible banata hai.

---

## Topic 3: APIs in Machine Learning - ML Model Ko Duniya Tak Kaise Pahunchate Hain?

### 1. Introduction

Software mein APIs ki zaroorat samajhne ke baad, ab samajhte hain ML ke perspective se. ML mein ek fundamental difference hai - yahaan database ki jagah ek **trained ML model** hota hai. Baki architecture bilkul same rehta hai.

Use case: OpenAI ne GPT model train kiya. Ab us model ko monetize karna hai. Solution? API architecture ke through expose karo.

---

### 2. Core Concepts

#### ML Model Ka Lifecycle

```
[Data Collection]
      |
[Model Training]  <-- bahut saara data, compute
      |
[Model Evaluation] <-- accuracy check, validation
      |
[Model Saved - Binary File]  e.g., model.pkl / model.pt / model.bin
      |
[API ke through Deploy] <-- duniya use kar sake
```

Trained model ek **binary file** ke form mein save hota hai (`.pkl`, `.pt`, `.bin`, etc.). Yeh file kisi bhi programming language mein load karke use ki ja sakti hai.

---

#### Pre-API Era: ML Monolithic Architecture

Pehle ML applications bhi monolithic hoti thi:

```
[ML App - single folder]
├── model.pkl          (trained model)
├── backend/
│   └── predict()      (model load karo, prediction lo)
└── frontend/
    └── form           (user input leta hai)
```

- Front end aur back end ek hi application mein tightly coupled the
- ML model ko koi third party access nahi kar sakta tha
- Website + Android + iOS ke liye teen alag apps banana padta

**ChatGPT example:** Jab ChatGPT launch hua, Zomato, Amazon, aur hazaron companies chahti thi ki unhe bhi GPT model ka access mile apne chatbots aur features improve karne ke liye. Monolithic architecture mein yeh possible nahi tha.

---

#### Solution: API Architecture for ML

Bilkul same solution jo software mein tha - back end ko decouple karo aur API layer lagao.

```
                   [Trained ML Model - Binary File]
                              |
                   [Back End - predict() function]
                              |
                         [API Layer]
                    /         |         \
           [Website]    [Android]    [iOS App]
           Front End    App FE       FE
                              |
              [Zomato Chatbot / Amazon / RAG App]
              (Third party ML API consumers)
```

**Full request-response flow:**

```
User types query (e.g., "Explain Transformers")
         |
   Front End (ChatGPT website / Android app)
         |
   API Endpoint hit hota hai (POST /predict)
         |
   Back End ka predict() function call hota hai
         |
   ML Model load hota hai, query pass hoti hai
         |
   Model prediction / response generate karta hai
         |
   JSON format mein response wapas API ko
         |
   API JSON response user ke front end tak
         |
   User ko answer display hota hai
```

---

#### Amazon Recommender System Example

Amazon ne ek powerful **recommender model** banaya jo user ke behavior ke basis pe products suggest karta hai.

Ab yeh model:
- Website par bhi chahiye
- Android app par bhi chahiye
- iOS app par bhi chahiye

**Without API (Monolithic):** Teen alag apps = teen alag models = teen alag teams = 3x kaam.

**With API Architecture:**

```
[Recommender ML Model]
         |
    [Back End]
         |
    [API Layer]
         |
  ----------------
  |       |      |
[Web]  [Android] [iOS]
```

Ek model, ek back end, ek API - teen frontends ke sab sawalon ka jawab JSON mein wapas.

---

### 3. Code Example

**FastAPI mein ek basic ML model serving endpoint:**

```python
from fastapi import FastAPI
import pickle

app = FastAPI()

# Trained model load karo (ek baar)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: dict):
    # User ka input lo
    features = data["features"]

    # Model se prediction lo
    prediction = model.predict([features])

    # JSON format mein return karo
    return {"prediction": prediction[0]}
```

**Request example:**
```json
POST /predict
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Response:**
```json
{
  "prediction": "Iris-setosa"
}
```

Koi bhi client - chahe Java mein bana ho, Swift mein, ya React mein - is endpoint ko call karke prediction le sakta hai.

---

### 4. Important Terms

| Term | Explanation |
|------|-------------|
| **ML Model Serving** | Trained model ko ek API ke through production mein deploy karna |
| **Binary File** | Trained model jo `.pkl`, `.pt`, `.bin` jaise format mein save hota hai |
| **predict() / inference** | Model ko input dekar prediction/output lena |
| **Model Deployment** | Model ko real-world users ke liye accessible banana |
| **POST /predict** | API endpoint jahan input bheja jata hai aur prediction wapas milti hai |
| **JSON Response** | Model ka output jo JSON format mein wapas aata hai - language-agnostic |
| **Third Party Consumer** | Koi aur company/app jo aapkی ML API use kare (e.g., Zomato using GPT API) |

---

### 5. FastAPI in ML/AI/RAG

Yahi topic seedha ML/AI ka core use case hai. Key takeaways:

- **ChatGPT Architecture:** OpenAI ka GPT model back end mein hai. FastAPI-jaise framework API layer banata hai. Koi bhi client - web, mobile, third party - sab usi API se baat karte hain.

- **OpenAI API:** Jab aap `openai.ChatCompletion.create()` call karte ho Python mein, aap basically ek **HTTP API endpoint** hit kar rahe ho jo JSON response deta hai. FastAPI se aap exactly aisa hi apne custom models ke liye bana sakte ho.

- **RAG Applications:** RAG pipeline mein:
  ```
  User Query (POST /ask)
       |
  FastAPI Endpoint
       |
  Embedding Model --> Vector DB Search --> Top-k docs retrieve
       |
  LLM ko docs + query pass karo
       |
  LLM response --> JSON mein wapas user ko
  ```

- **Hugging Face Inference API:** Yeh bhi exactly same architecture hai - unke models FastAPI-jaise framework ke through expose hain, aap endpoints hit karte ho, JSON milta hai.

- **Multi-client ML:** Ek hi trained model ko website, mobile app, aur B2B partners - sab FastAPI ke ek API layer ke through access kar sakte hain.

---

### 6. Summary

- ML mein architecture wahi hai jo software mein - **database ki jagah ML model** aa jata hai.
- Trained model ek binary file mein save hota hai. Back end us file ko load karke predictions deta hai.
- Pehle yeh bhi monolithic tha - third party access impossible, multi-platform hard.
- **Solution:** Model + Back End ke aage **API layer** lagao, sab kuch decouple ho jaata hai.
- **Key difference from software:** Database queries ki jagah model inference hoti hai - baki flow identical.
- FastAPI aaj industry mein ML model serving ka sabse popular aur recommended framework hai.

---

## Topic 6: FastAPI Kya Hai? - Starlette aur Pydantic Ka Role

### 1. Introduction

FastAPI ki **one-line definition:**

> *"FastAPI is a modern, high-performance web framework for building APIs with Python."*

Bahut simple line hai, lekin FastAPI ka poora essence capture karti hai. FastAPI sach mein ek Python framework hai jiski madad se aap bahut **high-performing, industry-grade APIs** Python mein build kar sakte ho.

---

### 2. FastAPI Internally Kaise Bana Hai?

FastAPI internally Python ki **do famous libraries** ke upar bana hua hai:

1. **Starlette**
2. **Pydantic**

FastAPI ke creator ne in dono libraries ko uthaya aur inhein combine karke FastAPI ko build kiya.

---

### 3. Starlette Ka Role - HTTP Request/Response Engine

Jab aap koi bhi API banate ho, tab API ka kaam hota hai:
1. Client/User se **HTTP request receive** karna
2. Us request par **kuch processing perform** karna
3. Palat ke ek **HTTP response generate** karke client ko bhejna

**FastAPI mein yeh poora HTTP layer Starlette handle karta hai.**

- Jab aapki FastAPI application par koi HTTP request aata hai  **Starlette us request ko receive karta hai**
- Jab response wapas bhejna hota hai  **Starlette woh response banake bhejta hai**

> *"Starlette manages how your API receives requests and sends back responses."*

---

### 4. Pydantic Ka Role - Data Validation Library

Python mein by default **strict type checking / type hinting nahi hoti**. Pydantic yeh gap fill karta hai.

**Pydantic ek Data Validation Library hai** - yeh check karta hai ki jo data aapke paas aa raha hai woh sahi format mein hai ya nahi.

#### Practical Example:

Maan lo aapne ek API banai jo:
- Do **station ke naam** (string) leta hai
- Ek **date** leta hai
- Batata hai ki un dono stations ke beech us particular date pe **kaun-kaun si trains chal rahi hain**

Ab API banate waqt aapko khud check karna padta:
-  Kya station ka naam **string format** mein hai?
-  Kya woh station **hamari given list of stations mein** hai ya nahi?
-  Kya date **valid format** mein hai?

Yeh saara **data validation ka kaam** aapko manually likhna padta tha. Lekin agar aap **Pydantic** use karo, toh yeh sara kaam **behind the scenes Pydantic automatically** karke deta hai.

> *"Pydantic is used to check if the data coming into your API is correct and in the right format."*

---

### 5. Important Terms

| Term | Explanation |
|------|-------------|
| **FastAPI** | Modern, high-performance Python web framework for building APIs |
| **Starlette** | FastAPI ka HTTP engine - requests receive karta hai aur responses bhejta hai |
| **Pydantic** | Data validation library - incoming API data ka format aur type check karta hai |
| **HTTP Request** | Client ki taraf se server ko bheja gaya message |
| **HTTP Response** | Server ki taraf se client ko wapas bheja gaya data |
| **Data Validation** | Check karna ki aane wala data sahi type aur format mein hai ya nahi |
| **Type Hinting** | Python mein variable ya function ke expected data type ko annotate karna |

---

### 6. Summary

- **FastAPI** ek modern Python web framework hai jisse aap **high-performance, industry-grade APIs** Python mein bana sakte ho.
- FastAPI internally **do Python libraries** ke upar bana hai:
  1. **Starlette**  HTTP requests receive karta hai aur responses bhejta hai (web/routing engine)
  2. **Pydantic**  Incoming API data ka validation perform karta hai (data validation engine)
- Python mein by default strict type checking nahi hoti - **Pydantic is gap ko fill karta hai**.
- FastAPI mein Pydantic automatically **behind the scenes** data validation karta hai, jisse aapko manually validation code nahi likhna padta.

---

## Topic 7: FastAPI Ki Core Philosophies aur Flask vs FastAPI Architecture

### 1. Introduction

FastAPI se pehle bhi Python mein API banane ke frameworks exist karte the. Toh phir FastAPI ke creators ko yeh zaroorat kyun padi ki ek naya framework banayein?

Iske peeche **do primary reasons** the - aur yahi do problems FastAPI ki **do core philosophies** ban gayi.

---

### 2. Do Problems Jinhe FastAPI Ne Solve Kiya

**Problem 1 - Performance Issue:**
Puraane frameworks (jaise Flask) mein APIs ka response time slow hota tha. Latency issues hote the, jo industry-grade applications ke liye acceptable nahi hai.

**Problem 2 - Zyada Code Likhna Padta Tha:**
Puraane frameworks mein API ka code likhne mein bahut mehnat lagti thi. Boilerplate code bahut zyada hota tha, aur unnecessary code likhna padta tha sirf API ko effectively run karne ke liye.

---

### 3. FastAPI Ki Do Core Philosophies

**Philosophy 1 - Fast to Run:**
FastAPI mein bani APIs bahut fast hoti hain execute hone mein. Woh concurrent users handle kar sakti hain aur latency bahut kam hoti hai.

**Philosophy 2 - Fast to Code:**
FastAPI mein API banana ka process bahut fast hai. Bahut kam lines of code mein bahut achchi API build kar paate ho.

> Yahi wajah hai ki is framework ka naam "FastAPI" rakha gaya - fast to run aur fast to code, dono.

---

### 4. API Ka Internal Information Flow - Web Server + SGI + API Code

Pehle yeh samajhna zaroori hai ki ek API deploy hone ke baad kaam kaise karti hai.

**Example Setup:** Maano humne ek ML model ke liye ek `/predict` endpoint banaya, jo do feature values leke prediction deta hai. Humne is API ko AWS par deploy kar diya.

**Deploy karne ka matlab kya hai?**
Jab aap API ko AWS jaise cloud par deploy karte ho, toh aap essentially **do cheezein** bhejte ho:

1. **API ka Code** - jahan business logic likha hota hai (features lo, model load karo, prediction generate karo, response return karo)
2. **Web Server** - jo AWS ki machines ke ports ke through continuously incoming HTTP requests ko sunne ki koshish karta rehta hai

**Kisi bhi API mein ye do components hote hain:**

| Component | Kaam |
|-----------|------|
| API Code | Business logic implement karna |
| Web Server | Client ke incoming HTTP requests ko process karna |

---

### 5. Full Request-Response Flow

```
Client (Browser / Postman)
        |
        | -- HTTP Request prepare hoti hai (method, endpoint URL,
        |    host, content-type, content-length, feature values, etc.)
        |
   [Web Server]  <-- HTTP request receive karta hai
        |
   [SGI Layer]   <-- HTTP request ko Python-understandable format mein convert karta hai
        |
   [API Code]    <-- Python code feature values extract karta hai, ML model call karta hai
        |
   [ML Model]    <-- Prediction generate karta hai
        |
   [API Code]    <-- Prediction result aata hai (Python format mein)
        |
   [SGI Layer]   <-- Python output ko wapas HTTP response mein convert karta hai
        |           (200 status code, content-type, packaged data)
   [Web Server]  <-- HTTP response client ko wapas bhejta hai
        |
   Client ko prediction milti hai
```

**SGI (Server Gateway Interface) kya hai?**
SGI ek **translator** hai jo Web Server aur API Code ke beech **two-way communication** establish karta hai. Kyunki HTTP request ko Python seedha nahi samajh sakta, SGI HTTP format se Python-understandable format mein convert karta hai aur wapas bhi.

> SGI = Protocol (rules ka set) jo web server aur Python application ke beech communication standardize karta hai.

---

### 6. Flask vs FastAPI - Architecture Comparison

In dono frameworks ke beech **teen key differences** hain:

#### Flask Architecture (WSGI - Synchronous)

| Component | Flask Mein |
|-----------|-----------|
| Web Server | Gunicorn |
| SGI Protocol | WSGI (Web Server Gateway Interface) |
| WSGI Library | Werkzeug |
| API Code Style | Synchronous (normal Python) |

**WSGI ki sabse badi problem:**
WSGI **synchronous** aur **blocking** nature ka hota hai. Iska matlab ek time par ek hi request process ho sakti hai.

Agar 5 clients ne ek saath request bheja, toh:
- WSGI pehle Client 1 ki request process karega
- Jab tak Client 1 ka kaam complete nahi hota, baaki clients wait karenge
- Resources blocked rahenge

**Gunicorn ki bhi same limitation hai** - kyunki yeh WSGI par based hai, isliye synchronous tarike se process karta hai, jo high-concurrency scenarios mein latency aur performance issues create karta hai.

#### FastAPI Architecture (ASGI - Asynchronous)

| Component | FastAPI Mein |
|-----------|-------------|
| Web Server | Uvicorn |
| SGI Protocol | ASGI (Asynchronous Server Gateway Interface) |
| ASGI Library | Starlette |
| API Code Style | Async/Await supported |

**ASGI ka sabse bada advantage:**
ASGI **asynchronous** nature ka hota hai - yeh **concurrent processing** kar sakta hai. Ek saath multiple requests parallel mein process ho sakti hain.

**Uvicorn ka advantage:**
Uvicorn ek high-performance ASGI server hai. Gunicorn ke comparison mein Uvicorn generally preferred hai apni asynchronous capabilities ki wajah se.

---

### 7. Async/Await - FastAPI Mein Concurrency Ka Raaz

FastAPI Python ke `async` aur `await` feature ko aggressively support karta hai, jo is poore pipeline ko asynchronous banata hai.

**Normal (Synchronous) Code ka behavior:**

```
Request 1 aaya --> ML Model ko bheja --> ML Model compute kar raha hai...
(Is beech API ruk jaati hai, koi aur request process nahi hoti)
ML Model ne result diya --> Response bheja --> Ab Request 2 lo
```

**Async/Await wala behavior:**

```
Request 1 aaya --> ML Model ko bheja --> ML Model compute kar raha hai...
(Is beech API doosri request process karti hai)
Request 2 aaya --> handle kiya
ML Model ne Request 1 ka result diya --> Response complete kiya
(Aur yeh process concurrent chalti rehti hai)
```

> Jab aap `await` use karte ho, toh aap basically API ko bol rahe ho: "Yeh operation hone mein time lagega. Tab tak ja aur doosra kaam kar le."

---

### 8. Flask vs FastAPI - Side by Side Summary Table

| Aspect | Flask | FastAPI |
|--------|-------|---------|
| SGI Protocol | WSGI (Synchronous) | ASGI (Asynchronous) |
| SGI Library | Werkzeug | Starlette |
| Web Server | Gunicorn | Uvicorn |
| Processing Nature | Blocking (ek time par ek request) | Non-blocking (concurrent requests) |
| Async Support | Nahi (by default) | Haan (async/await natively) |
| Performance | Moderate (latency issues at scale) | High (low latency, high concurrency) |

---

### 9. Waiter Analogy - Simplest Explanation

**Flask (Synchronous Waiter):**
Customer aaya, waiter ne order liya, kitchen mein diya aur wahan khada ho gaya. Jab tak khana nahi bana, waiter kisi aur customer ke paas nahi gaya. Time waste hua.

**FastAPI (Asynchronous Waiter):**
Customer aaya, waiter ne order liya, kitchen mein diya. Waiter ko pata hai khana banne mein time lagega, so woh doosre customer ka order le aaya. Kitchen mein diya. Pehle wala khana ban chuka tha, uthaya aur pehle customer ko serve kiya. Yeh process asynchronous fashion mein chahta rehta hai.

> Is waiter analogy se clearly samajh aata hai ki FastAPI concurrent requests kyun better handle karta hai Flask se.

---

### 10. Important Terms

| Term | Explanation |
|------|-------------|
| SGI | Server Gateway Interface - web server aur Python app ke beech translator |
| WSGI | Web Server Gateway Interface - purana synchronous protocol, Flask mein use hota hai |
| ASGI | Asynchronous Server Gateway Interface - modern async protocol, FastAPI mein use hota hai |
| Werkzeug | Flask mein WSGI implement karne wali library |
| Starlette | FastAPI mein ASGI implement karne wali library |
| Gunicorn | Flask ka WSGI HTTP web server |
| Uvicorn | FastAPI ka ASGI web server - high performance aur asynchronous |
| Synchronous | Ek request poori hone ke baad hi doosri shuru hoti hai (blocking) |
| Asynchronous | Multiple requests ek saath concurrent mein process ho sakti hain (non-blocking) |
| Async/Await | Python syntax jo non-blocking asynchronous code likhne mein use hota hai |
| Concurrency | Multiple requests ko ek saath handle karna bina wait karwaye |

---

### 11. Summary

- FastAPI do core philosophies par bana hai: **Fast to Run** (high performance, concurrent) aur **Fast to Code** (less boilerplate, faster development).
- Kisi bhi API mein do key components hote hain: **Web Server** (HTTP requests sunna) aur **API Code** (business logic).
- In dono ke beech ek **SGI layer** hoti hai jo HTTP aur Python formats ke beech translation karta hai.
- **Flask** WSGI protocol use karta hai jo **synchronous aur blocking** hai - ek time par ek hi request.
- **FastAPI** ASGI protocol use karta hai (Starlette library ke through) jo **asynchronous** hai - concurrent requests handle kar sakta hai.
- **Uvicorn** (FastAPI) vs **Gunicorn** (Flask) - Uvicorn asynchronous hai, isliye high performance deliver karta hai.
- **Async/Await** Python feature FastAPI ke API code ko bhi asynchronous banata hai, jisse poora pipeline non-blocking ho jaata hai.
- Yahi combination - ASGI + Uvicorn + Starlette + Async/Await - FastAPI ko **Fast to Run** banata hai.

---

## Topic 8: FastAPI - Fast to Code Philosophy (Teen Reasons)

### 1. Introduction

FastAPI ki doosri core philosophy hai - **Fast to Code**.

Iska matlab yeh hai ki FastAPI ke creators ne yeh ensure kiya ki jab bhi koi FastAPI use karke API build kare, usse bahut zyada code nahi likhna padega. Bahut kam code mein bahut kuch achieve ho sake.

Teen major aspects hain jinki wajah se FastAPI mein coding process bahut fast ho jaati hai.

---

### 2. Aspect 1 - Automatic Input Validation (Pydantic Integration)

Python mein by default **strict type checking nahi hoti**. Python ke variables dynamically create hote hain, aur unki values runtime par change ho sakti hain. Ek variable `a` ka value `2` bhi ho sakta hai aur koi string bhi - koi rokta nahi.

Yeh feature achha hai flexibility ke liye, lekin jab aap industry-grade, enterprise-level application bana rahe ho, toh aap chahte ho ki **type-related errors generate na hon**.

**FastAPI ka solution:** FastAPI mein by default **Pydantic ka support** built-in hai.

Jab bhi aap FastAPI mein koi endpoint banate ho, aap wahan specify kar sakte ho ki us endpoint ko jo input mil raha hai woh **kaunse data type ka hona chahiye**. FastAPI aur Pydantic ka yeh integration bahut tightly coupled hai - behind the scenes kaafi kuch FastAPI khud handle kar leta hai, aapko manually validation code nahi likhna padta.

> Aage ke videos mein dikhaaya jaayega ki practically kaise Pydantic se automatic input validation karte hain.

---

### 3. Aspect 2 - Auto-Generated Interactive Documentation

Software development mein sirf code likhna hi kafi nahi hota. Ek solid **documentation** banana bhi utna hi zaroori hai, taaki aapke API ke users yeh samajh sakein:

- Har endpoint ka **purpose kya hai**
- Har endpoint **kaunse format mein data expect** karta hai
- Har endpoint **kaunsa data return** karta hai

Yeh documentation banana khud mein time-consuming kaam hai.

**FastAPI ka solution:** Jaise-jaise aap code likhte jaate ho, FastAPI **automatically documentation generate** karta chala jaata hai. Aapko alag se documentation likhne ki zaroorat nahi padti.

Aur sabse best part yeh hai ki yeh ek **interactive documentation** hoti hai - aap sirf API ke baare mein padh hi nahi sakte, balki directly wahan se **API ke saath interact aur test bhi kar sakte ho** (Swagger UI ke through).

> Is feature ka practical demonstration is video mein aage dikhaaya jaayega.

---

### 4. Aspect 3 - Modern Framework with Seamless Integrations

FastAPI ek **modern framework** hai, jiska matlab hai ki yeh aaj ki popular aur production-grade libraries ke saath bahut seamlessly integrate hota hai. Aapko alag-alag cheezein jodhne ke liye zyada kaam nahi karna padta.

**ML/DL Libraries:**

| Library | Use Case |
|---------|----------|
| Scikit-learn | Classical ML models |
| TensorFlow | Deep Learning |
| PyTorch | Deep Learning / Research |

**Authentication:**
- **OAuth** - Login, authentication aur authorization ke liye seamless integration milta hai.

**Database:**
- **SQLAlchemy** - SQL databases ke saath kaam karne ke liye tight integration.

**Deployment:**
- **Docker** - Containerization ke liye directly compatible.
- **Kubernetes** - Production-scale deployment ke liye integration available hai.

> Yahi wajah hai ki FastAPI sirf API banane ka tool nahi hai - yeh ek complete ecosystem ke saath kaam karta hai jo modern production applications ke liye zaruri hai.

---

### 5. Summary of All Three Aspects

| Aspect | Kya milta hai FastAPI mein |
|--------|---------------------------|
| Automatic Input Validation | Pydantic ka built-in support - type errors automatically handle hote hain |
| Auto-generated Interactive Docs | Code likhte waqt hi documentation ban jaati hai (Swagger UI) |
| Modern Library Integrations | ML, Auth, DB, Deployment tools ke saath seamless compatibility |

---

### 6. Overall FastAPI Summary - Dono Philosophies

FastAPI ki do core philosophies hain aur dono mein yeh shine karta hai:

**Philosophy 1 - Fast to Run (Performance):**
- ASGI protocol (Starlette library ke through) - asynchronous aur concurrent
- Uvicorn web server - high performance
- Async/Await support - non-blocking pipeline

**Philosophy 2 - Fast to Code (Developer Productivity):**
- Pydantic ka automatic input validation
- Auto-generated interactive documentation (Swagger UI)
- Seamless integrations with modern ML, DB, and deployment tools

> In dono philosophies ki wajah se hi is framework ka naam "FastAPI" rakha gaya - fast to run aur fast to code.

---

### 7. Important Terms

| Term | Explanation |
|------|-------------|
| Automatic Input Validation | API endpoint par aane wala data automatically check hona ki woh sahi type mein hai |
| Pydantic | FastAPI ki built-in data validation library |
| Swagger UI | FastAPI ki auto-generated interactive documentation ka interface |
| Interactive Documentation | Documentation jahan se directly API ko test bhi kar sakte hain |
| Boilerplate Code | Unnecessary repetitive code jo sirf framework ko run karne ke liye likhna padta tha |
| SQLAlchemy | Python ka popular ORM (Object Relational Mapper) for database interactions |
| OAuth | Authentication aur authorization ke liye industry-standard protocol |
| Docker | Application ko containers mein package karne ka tool |
| Kubernetes | Containerized applications ko production scale par manage karne ka tool |

---

## Topic 9: FastAPI Installation aur Hello World API - Code Demo

### 1. Setup - Virtual Environment aur Installation

FastAPI project shuru karne ke liye steps:

**Step 1 - Project folder banao aur VS Code mein open karo.**

**Step 2 - Virtual environment create karo:**
```bash
# Windows / Mac:
python -m venv myenv

# Linux (Ubuntu/Debian):
python3 -m venv myenv
```

> **Linux Note:** Linux par `python` command by default available nahi hoti - sirf `python3` hoti hai. Agar `python` use karo toh error aayega: *"Command 'python' not found"*. Linux par hamesha `python3` use karo.

**Step 3 - Virtual environment activate karo:**
- Windows: `myenv\Scripts\activate`
- Mac/Linux: `source myenv/bin/activate`

> **Important:** Ek baar virtual environment activate ho jaane ke baad, andar `python` aur `pip` dono normally kaam karte hain (bina `3` suffix ke) - venv yeh automatically set kar leta hai.

**Step 4 - Required libraries install karo:**
```bash
pip install fastapi uvicorn
```

> Note: Jab aap FastAPI install karte ho, Starlette aur Pydantic automatically as dependencies install ho jaati hain. Aap terminal output mein dekh sakte ho ki yeh sab bhi install ho rahe hote hain.

---

### 2. Pehli API Banana - `main.py`

Ek nayi file banao `main.py` naam se aur yeh code likho:

```python
from fastapi import FastAPI

# Step 1: FastAPI ka app object create karo
app = FastAPI()

# Step 2: Pehla endpoint define karo
@app.get("/")
def hello():
    return {"message": "Hello World"}

# Step 3: Doosra endpoint define karo
@app.get("/about")
def about():
    return {"message": "CampusX is an education platform where you can learn AI."}
```

**Code ka breakdown:**

| Part | Explanation |
|------|-------------|
| `from fastapi import FastAPI` | FastAPI class import karna |
| `app = FastAPI()` | Application ka main object - yeh hamari poori API represent karta hai |
| `@app.get("/")` | Decorator jo ek route define karta hai - yahan `/` home URL hai, `get` HTTP method hai |
| `def hello()` | Is route par aane wali request ko handle karne wala function |
| `return {"message": "Hello World"}` | Python dictionary - FastAPI automatically ise JSON mein convert karke response deta hai |

**GET vs POST - Basic Samajh:**
- **GET request** - Jab aap server se koi data fetch/read karna chahte ho
- **POST request** - Jab aap server par koi data bhejna chahte ho

Abhi hum server se data la ke dekhna chahte hain, isliye GET use kar rahe hain.

---

### 3. Server Run Karna - Uvicorn Command

```bash
uvicorn main:app --reload
```

**Command ka breakdown:**

| Part | Explanation |
|------|-------------|
| `uvicorn` | ASGI server jo hamari application serve karega |
| `main` | Python file ka naam (bina `.py` ke) |
| `app` | FastAPI object ka naam jo `main.py` mein define kiya hai |
| `--reload` | Dev mode flag - code save karte hi server automatically reload ho jaata hai |

Command run karne ke baad Uvicorn ek local URL par HTTP requests sunne lagta hai (e.g., `http://127.0.0.1:8000`).

**`--reload` ka fayda:**
Jab bhi aap code mein koi change karke save karte ho, server khud restart ho jaata hai. Manually restart karne ki zaroorat nahi padti.

---

### 4. Endpoints Access Karna

| URL | Kaunsa Endpoint Hit Hoga |
|-----|--------------------------|
| `http://127.0.0.1:8000/` | `hello()` function - `{"message": "Hello World"}` |
| `http://127.0.0.1:8000/about` | `about()` function - `{"message": "CampusX is..."}` |

URL mein `/` laga ho ya na ho, home route ke liye dono equivalent hote hain.

---

### 5. Auto-Generated Interactive Documentation - `/docs`

FastAPI ka ek standout feature - running server ke URL mein `/docs` append karo:

```
http://127.0.0.1:8000/docs
```

Yahan aapko **Swagger UI** ka ek page milega jahan:

- Aapke saare endpoints automatically listed hote hain (abhi `/` aur `/about`)
- Har endpoint ka type (GET/POST), parameters, aur return format clearly dikh ta hai
- **"Try it out"** button se aap directly wahan se API ko test kar sakte ho bina Postman jaise kisi third-party software ke
- **"Execute"** button click karne par response body, status code (200), server info, content-length - sab kuch wahan dikh jaata hai

> Jaise-jaise aap naaye endpoints add karte jaate ho, `/docs` page automatically unhe uthaa leta hai. Koi extra documentation likhne ki zaroorat nahi.

---

### 6. Summary

- FastAPI project ke liye virtual environment banana aur usme `fastapi`, `uvicorn`, `pydantic` install karna recommended hai. Starlette automatically aa jaata hai.
- `main.py` mein `FastAPI()` object banao, phir `@app.get("/route")` decorator se endpoints define karo.
- Har endpoint ke liye ek Python function likhte hain jo dictionary return karta hai - FastAPI use JSON mein convert kar deta hai.
- Server run karne ke liye: `uvicorn main:app --reload`
- `--reload` flag dev environment mein code changes par automatic server restart deta hai.
- `http://127.0.0.1:8000/docs` par jaake auto-generated interactive Swagger documentation milti hai jahan se seedha API test bhi kar sakte ho.

---

## Topic 7: Project Overview - Doctor's Clinic Patient Management API

### 1. Problem Statement

Doctor ke clinic mein aaj bhi ek bahut common practice hai - woh ek **printed letterhead pe pen se prescription likhte hain**. Isme patient ka naam, city, age, gender, height, weight, BMI aur davaon ke naam hote hain. Doctor patient se kehte hain ki agli baar clinic (follow-up visit) par yeh document lekar आना.

**Problems with this offline approach:**

| Problem | Kisko affect karta hai |
|---------|----------------------|
| Papers mislace ho sakte hain | Patient aur Doctor dono |
| Doctor ki apni copy bhi kho sakti hai | Doctor |
| Years tak documents ek file mein maintain karna mushkil hai | Patient |
| Koi bhi central, searchable record nahi hota | Healthcare system |

---

### 2. Solution - Online Patient Management App

Ek **startup idea** hai: is poori offline system ko **online** le aana.

**Plan:** Doctor ko ek app de do. Us app ke through doctor:
- Har patient ka ek **digital profile** maintain kar sake
- Profile mein: Patient Name, City, Age, Gender, Height, Weight, BMI (aur aage jaake aur bhi medical information)

> **Note:** Is basic-level project mein hum Height, Weight aur BMI tak hi limited rahenge. But concept extensible hai - bahut saari aur cheezein add ki ja sakti hain.

---

### 3. Hamara Kaam - API Develop Karna

Hum **front-end application nahi bana rahe**. Front end banana front-end developers ka kaam hai.

**Hum as Back-End Engineers ek API develop karenge** jo ke following features provide karegi:

#### Data Storage

- **Ideally:** Patient records ek **Database** mein store hone chahiye.
- **Is basic project mein:** Hum ek **JSON file** use karenge storage ke liye.
- Method bilkul same rehega - sirf database ki jagah JSON file hai.

#### CRUD Operations (5 Endpoints)

| # | Endpoint | Kaam | HTTP Method |
|---|----------|------|-------------|
| 1 | Create Patient | Doctor form fill karega, data is endpoint ko milega, JSON file mein naya patient add hoga | `POST` |
| 2 | View All Patients | JSON file ke saare records list honge | `GET` |
| 3 | View Single Patient | Ek particular patient ID (e.g., P001, P005, P010) ka profile dekhna | `GET` |
| 4 | Update Patient | Kisi existing patient ka record modify karna (e.g., weight change hua toh BMI automatically recalculate hoga) | `PUT` |
| 5 | Delete Patient | Kisi patient ko database se remove karna | `DELETE` |

> **Smart Feature:** Jab bhi doctor patient ka weight update karega, back end **automatically BMI recalculate** kar dega.

---

### 4. Summary

- **Problem:** Doctor-patient records abhi offline hain - papers mislace hote hain, management mushkil hai.
- **Solution:** Ek online app jo doctor ko digital patient profiles create aur manage karne deti hai.
- **Humara role:** Back-end engineers ke taur par hum is app ka **API layer develop karenge**.
- **Storage:** Database ki jagah pehle **JSON file** use karenge (concept same rahega).
- **API mein 5 endpoints honge:** Create, View All, View One, Update, Delete - yahi **CRUD operations** hain.
- Future mein yeh API use karke koi bhi doctor-facing web/mobile app bana sakta hai.

---

## Topic 8: HTTP Methods - CRUD aur Web Communication

### 1. Introduction

FastAPI mein aage badhne se pehle ek ek **bahut zaroori concept** samajhna chahiye: **HTTP Methods**. Puri playlist mein aap inhe baar baar dekhoge. Toh aao ek simple, fundamental level se start karte hain.

---

### 2. Static vs Dynamic Software

Pehle samajhte hain ki software ki duniya mein **do types of software** hote hain - based on **user interaction**:

| Type | Matlab | Examples |
|------|--------|---------|
| **Static Software** | User sirf information receive karta hai. Bahut kam interaction hoti hai. One-way communication. | Calendar, Clock |
| **Dynamic Software** | User actively interact karta hai. Two-way communication hoti hai. | MS Excel, MS Word, PowerPoint |

> **Analogy:** Calendar ek **noticeboard** ki tarah hai - aap sirf padhte ho. MS Excel ek **whiteboard** ki tarah hai - aap likhte, mitaate, aur badlte bhi ho.

```
Static Software:
  User ──── reads ──── Software
  (One-way communication only)

Dynamic Software:
  User ──────────── Software
  (Two-way: user sends data, software responds)
```

Hum **sirf dynamic software** ke baare mein aage baat karenge.

---

### 3. CRUD - Sirf 4 Types of Interactions

Aap kisi bhi dynamic software ke saath **sirf 4 types ke interactions** kar sakte ho. Isse kaha jata hai **CRUD**:

| Letter | Operation | Matlab |
|--------|-----------|--------|
| **C** | **Create** | Kuch naya banana (new data add karna) |
| **R** | **Retrieve** | Kuch existing dekhna / fetch karna |
| **U** | **Update** | Kuch existing mein changes karna |
| **D** | **Delete** | Kuch existing mitana |

#### MS Excel se samjho:

```
MS Excel ke saath kya-kya kar sakte ho?
├── Nayi cells mein data enter karo        ── CREATE
├── Existing cells ka data dekho           ── RETRIEVE
├── Existing cells ka data badlo           ── UPDATE
└── Existing cells ko hata do              ── DELETE
```

#### Instagram se samjho:

```
Instagram par kya-kya karte ho?
├── Naya post upload karo, comment likho   ── CREATE
├── Feed scroll karo, profile dekho        ── RETRIEVE
├── Apna profile edit karo, comment edit   ── UPDATE
└── Post delete karo, comment delete karo  ── DELETE
```

#### Zomato se samjho:

```
Zomato par kya-kya karte ho?
├── Naya order place karo                  ── CREATE
├── Past orders dekho                      ── RETRIEVE
├── Delivery address update karo           ── UPDATE
└── Koi address delete karo               ── DELETE
```

> **Key Insight:** Duniya ki koi bhi dynamic website/software lo - saare interactions CRUD ke andar fit ho jaate hain. Koi 5th type nahi hoti.

---

### 4. Websites Bhi Software Hain

Ek important clarification: **Websites bhi ek type ka software hi hain**. Fark bas yeh hai:

| | Normal Software (e.g., MS Excel) | Website |
|-|----------------------------------|---------|
| **Install kahan?** | Aapki machine par | Ek doosri machine par (Server) |
| **Use kahan?** | Usi machine par | Doosri machine par (Client) |
| **Communication** | Local (direct) | Internet ke through (HTTP protocol) |

```
Normal Software:
  [Your Machine]
  Install ── Use (same machine)

Website:
  [Server Machine]       [Client Machine]
     (installed) ─HTTP─ (accessed by you)
```

**Server** = Woh machine jahan website installed hai.  
**Client** = Aapki machine jahan se aap website access karte ho.

Isliye websites mein bhi CRUD operations same hoti hain - bas yeh internet ke through, **HTTP protocol** ke zariye hoti hain.

---

### 5. HTTP Methods - CRUD ko HTTP mein Represent Karna

Jab CRUD operations **internet (HTTP) ke through** hoti hain, toh server ko pata hona chahiye ki client **kis type ka interaction** karna chahta hai. Isliye **HTTP Request mein ek "verb" (word) add kiya jaata hai** - ise **HTTP Method** kehte hain.

| CRUD Operation | HTTP Method (Verb) | Matlab |
|---------------|-------------------|--------|
| **Create** | `POST` | Naya data bhejna / create karna |
| **Retrieve** | `GET` | Data fetch/read karna |
| **Update** | `PUT` | Existing data modify karna |
| **Delete** | `DELETE` | Data delete karna |

> **Note:** `GET` aur `POST` sabse zyada commonly use hote hain. `PUT` aur `DELETE` thoda kam, lekin APIs mein ye sab equally important hain.

---

### 6. Flowchart - End-to-End HTTP CRUD Flow

```
User (Client) kuch karna chahta hai
           │
           
   Kaunsa operation?
  ┌────────┬────────┬────────┐
  │        │        │        │
GET      POST      PUT    DELETE
  │        │        │        │
Retrieve  Create  Update  Delete
  │        │        │        │
  └────────┴────────┴────────┘
           │
           
  HTTP Request banta hai
  [Method: GET/POST/PUT/DELETE]
  [URL: endpoint address]
  [Body: data (sirf POST/PUT mein)]
           │
           
     Server pe pahuncha
           │
           
  Server operation perform karta hai
  (DB se read / DB mein write / etc.)
           │
           
  HTTP Response wapas client ko
  [Status Code: 200 OK / 201 Created / 404 Not Found]
  [Body: JSON data]
           │
           
  User ko result dikhta hai
```

---

### 7. Restaurant Analogy - HTTP Methods ko Samjho

Ek restaurant ka scene imagine karo:

```
┌──────────────┬──────────────────────────────────┬────────────┐
│ Aap kya karo │ Restaurant Analogy               │ HTTP Method│
├──────────────┼──────────────────────────────────┼────────────┤
│ Naya order   │ Waiter ko naya order dena        │ POST       │
│ Menu dekhna  │ Menu card maangna                │ GET        │
│ Order badlna │ "Paneer ki jagah dal do" bolna   │ PUT        │
│ Order cancel │ "Yeh order cancel kar do" bolna  │ DELETE     │
└──────────────┴──────────────────────────────────┴────────────┘
```

**Waiter** = API  
**Menu Card** = Available Endpoints  
**Kitchen** = Server/Backend  
**Food** = JSON Response

---

### 8. Hamara Project - HTTP Methods Ka Use

Patient Management API mein hum exact same pattern follow karenge:

| Endpoint | CRUD | HTTP Method | Kaam |
|----------|------|-------------|------|
| `/patients` (create) | Create | `POST` | Naya patient add karo |
| `/patients` (view all) | Retrieve | `GET` | Saare patients list karo |
| `/patients/{id}` (view one) | Retrieve | `GET` | Ek specific patient dekho |
| `/patients/{id}` (update) | Update | `PUT` | Patient ka record update karo |
| `/patients/{id}` (delete) | Delete | `DELETE` | Patient ko remove karo |

---

### 9. Important Terms

| Term | Explanation |
|------|-------------|
| **HTTP Method** | HTTP request mein bheja gaya "verb" jo batata hai ki kaunsa CRUD operation chahiye |
| **GET** | Retrieve / read operation. Data fetch karna. Request body nahi hota. |
| **POST** | Create operation. Naya data server ko bhejna. Request body mein data hota hai. |
| **PUT** | Update operation. Existing resource ko modify karna. Body mein updated data hota hai. |
| **DELETE** | Delete operation. Server se koi resource hatana. |
| **CRUD** | Create, Retrieve, Update, Delete - kisi bhi dynamic software ke 4 fundamental operations |
| **Static Software** | Kam interaction wala software (e.g., Calendar, Clock) |
| **Dynamic Software** | Zyada interaction wala software (e.g., MS Excel, Instagram) |
| **Client** | Woh machine/app jahan se request aati hai (aapka browser) |
| **Server** | Woh machine jahan website/API installed hai aur request process hoti hai |
| **HTTP Protocol** | Internet par client-server communication ka standard protocol |
| **Status Code** | Server ka response code (200=OK, 201=Created, 404=Not Found, 500=Server Error) |

---

### 10. FastAPI in ML/AI/RAG

HTTP Methods ML systems mein bhi wahi kaam karte hain:

```
ML API Example:
├── POST /train        ── Naya model train karo (Create)
├── GET  /predict      ── Prediction lo (Retrieve)
├── PUT  /model/config ── Model hyperparams update karo (Update)
└── DELETE /model/{id} ── Purana model delete karo (Delete)
```

- **RAG system mein:** `POST /ask` endpoint user ka query receive karta hai (body mein), document search karta hai, LLM se answer generate karta hai, aur JSON response bhejta hai.
- **Model Deployment mein:** `GET /predict?input=...` ya `POST /predict` (body mein features) - dono common patterns hain.
- **Pydantic + POST:** Jab form data aata hai POST request mein, Pydantic uski strict validation karta hai - galat type aaya toh auto-reject.

---

### 11. Summary

- Software 2 types ke hote hain: **Static** (kam interaction) aur **Dynamic** (zyada interaction).
- Kisi bhi dynamic software mein sirf **4 types ke interactions** hote hain: **CRUD** (Create, Retrieve, Update, Delete).
- Websites bhi software hain - fark bas yeh hai ki woh **internet (HTTP) ke through** access hoti hain.
- CRUD operations ko HTTP pe express karne ke liye **HTTP Methods (Verbs)** use hoti hain:
  - `POST`  Create
  - `GET`  Retrieve
  - `PUT`  Update
  - `DELETE`  Delete
- FastAPI mein har endpoint par aap in methods mein se ek assign karte ho (`@app.get()`, `@app.post()`, etc.)
- Hamara Patient Management API bhi inheen 4 methods use karega apne 5 endpoints mein.

---

## Topic 9: HTTP Methods - Real World Browser Demo

### 1. Introduction

Theory ke baad ab dekhte hain ki **real websites par HTTP methods actually kaise kaam karti hain**. Browser ka built-in **DevTools (Inspect  Network tab)** use karke hum behind-the-scenes HTTP requests dekh sakte hain.

> **Setup:** Browser mein kisi bhi page par `Right Click  Inspect  Network tab` open karo. Ab jo bhi HTTP requests server ko jayengi, woh yahan list hoti jaayengi.

---

### 2. Demo 1 - GET Request (Retrieve/View)

**Scenario:** CampusX website par "Courses" page access karna.

Yeh clearly ek **Retrieve** type ka interaction hai - hum kuch **view** karna chahte hain, kuch **bhej** nahi rahe.

**Observation in Network Tab:**
```
Request URL    : https://campusx.in/store
Request Method : GET        
```

**Explanation:**
- Browser ne mere liye ek `GET` HTTP request server ko bheja.
- Server ne courses ka data wapas bheja.
- `GET`  Retrieve  "Mujhe kuch data chahiye, server please do."
- `GET` request mein **koi body nahi hoti** - sirf URL se hi server ko pata chalta hai kya chahiye.

---

### 3. Demo 2 - POST Request (Create/Send Data)

**Scenario:** CampusX website par Login form fill karke submit karna (email + password).

Yeh **Create/Send** type ka interaction hai - hum kuch **data server ko bhej** rahe hain.

**Observation in Network Tab:**
```
Request URL    : https://campusx.in/authenticate
Request Method : POST       
```

**Explanation:**
- Form submit karte hi browser ne ek `POST` HTTP request server ko bheja.
- `POST` request ke **body** mein email aur password tha.
- Server ne credentials check kiye aur response diya.
- `POST`  Create/Send  "Main server ko kuch data de raha hoon."

---

### 4. GET vs POST - Key Difference

```
GET Request:
┌──────────────────────────────┐
│  GET /courses HTTP/1.1       │   Method + URL
│  Host: campusx.in            │   Headers
│  (No body)                   │    Body nahi hoti
└──────────────────────────────┘
Server: "Theek hai, courses ka data lo."

POST Request:
┌──────────────────────────────┐
│  POST /authenticate HTTP/1.1 │   Method + URL
│  Host: campusx.in            │   Headers
│                              │
│  {                           │    Body hoti hai
│    "email": "x@gmail.com",  │
│    "password": "****"        │
│  }                           │
└──────────────────────────────┘
Server: "Credentials check karta hoon..."
```

| | GET | POST |
|--|-----|------|
| **CRUD Type** | Retrieve | Create |
| **Data kahan?** | URL mein (query params) | Request Body mein |
| **Use case** | Page/data fetch karna | Form submit, login, naya record create karna |
| **Secure?** | Less (data URL mein dikhta hai) | More (data body mein hidden hota hai) |

---

### 5. Practical Takeaway - Aage Project Mein

Hamara pehla endpoint banenge **GET `/patients`** - jo saare patients ka data retrieve karega.

```python
# FastAPI mein GET endpoint kuch aisa dikhega:
@app.get("/patients")
def get_all_patients():
    # patients.json se data read karo
    return data
```

- **Method:** `GET` (kyunki hum data retrieve kar rahe hain)
- **URL:** `/patients`
- **Body:** Koi nahi (GET mein body nahi hoti)
- **Response:** JSON format mein saare patients ka data

---

### 6. Summary

- Browser ka **Network tab** (DevTools) se aap real websites par actual HTTP methods dekh sakte ho.
- **Page/data view karna**  `GET` request (e.g., courses page dekhna)
- **Form submit / data bhejna**  `POST` request (e.g., login form)
- `GET` requests mein **body nahi hoti** - data URL se specify hota hai.
- `POST` requests mein **body hoti hai** - data securely body mein travel karta hai.
- Hamara pehla project endpoint: **`GET /patients`** - saare patients ka data retrieve karna.

---

## Topic 10: Path Parameters aur Query Parameters - Dynamic URL Segments

### 1. Introduction

Is video mein do bahut important concepts cover ho rahe hain: **Path Parameters** aur **Query Parameters**. Yeh dono FastAPI mein extensively use hote hain. Pehle Path Parameters samajhte hain.

---

### 2. Path Parameters - Kya Hain?

**Definition:**

> *"Path Parameters are dynamic segments of a URL path used to identify a specific resource."*

Seedha bhasha mein - Path Parameters URL ke woh hisse hain jo **change ho sakte hain**, aur unka kaam hai ki woh server par pade hue bahut saare resources mein se **ek specific resource ko locate** karein.

---

### 3. Example Se Samjho

Last video mein humne ek endpoint banaya tha:

```
GET http://localhost:8000/view
```

Is endpoint par hit karte hi **saare patients ka data** ek saath load hoke dikhta tha.

**Ab ek naya sawaal:** Agar mujhe saare patients ka data nahi chahiye, balki **sirf ek specific patient** ka data chahiye (e.g., Patient #3), toh kya karein?

**Answer:** URL mein ek chhota sa modification karo:

```
GET http://localhost:8000/view/3
```

Yahan pe yeh `3` ek **dynamic part** hai - ise hi **Path Parameter** kehte hain.

```
http://localhost:8000/view/3
│                        │   │
│     Fixed Part         │   │── Path Parameter (dynamic, badal sakta hai)
│  (domain + route)      │
```

- `localhost:8000`  Domain (fixed, change nahi hota)
- `/view`  Route (fixed, change nahi hota)
- `/3`  **Path Parameter** (dynamic - yeh `3` ki jagah `4`, `5` ya kuch bhi ho sakta hai)

---

### 4. Path Parameters Ka Kaam

Path parameter ka sirf ek hi kaam hai - **ek specific resource ko identify karna** server par pade hue bahut saare resources mein se.

Jaise hamare database (JSON file) mein 5 patients hain. Path parameter ki madad se hum un 5 mein se **kisi ek particular patient** ko select kar paa rahe hain.

---

### 5. Path Parameters Kahan-Kahan Use Hote Hain?

Path parameters teen main operations mein extensively use hote hain:

| Operation | Example | Explanation |
|-----------|---------|-------------|
| **Retrieve (GET)** | `GET /view/3` | Ek specific patient ka data dekhna |
| **Update (PUT)** | `PUT /update/3` | Ek specific patient ka record update karna |
| **Delete (DELETE)** | `DELETE /delete/3` | Ek specific patient ko database se hatana |

> **Common Pattern:** Jab bhi aapko kisi single, specific resource ke saath kuch karna ho (dekhna, badalna, ya hatana), toh path parameter use hota hai.

#### Real-World Examples:

- **Social Media Profile:** `/users/nitesh`  Ek particular user ka profile dikhana
- **E-commerce Product:** `/products/42`  Ek particular product ki detail dikhana
- **Blog Post:** `/posts/108`  Ek particular blog post dikhana

---

### 6. Hamara Project - Naya Endpoint

Ab hamare Patient Management API mein ek **naya endpoint** add karenge:

**Goal:** Client (user) apne pasand ke **kisi bhi specific patient** ka data dekh sake - saare patients ka data nahi, sirf ek particular patient ka.

**Kaunsa patient?** Yeh humein URL ke through bataya jaayega - **path parameter** ki madad se.

```
# Existing endpoint - saare patients dikhata hai
GET /view          All patients ka data

# Naya endpoint - sirf ek patient dikhayega
GET /view/{patient_id}     Specific patient ka data (e.g., /view/P003)
```

---

### 7. Important Terms

| Term | Explanation |
|------|-------------|
| **Path Parameter** | URL ka dynamic segment jo ek specific resource ko identify karta hai |
| **Dynamic Segment** | URL ka woh hissa jo har request mein badal sakta hai |
| **Fixed Segment** | URL ka woh hissa jo har request mein same rehta hai (domain, route name) |
| **Resource** | Server par stored koi bhi data item (e.g., ek patient record, ek user profile) |
| **Specific Resource** | Bahut saare resources mein se ek particular item jise aap access karna chahte ho |

---

### 8. Code Demo - Path Parameter Endpoint Banana

Ab code mein implement karte hain. Hamare route ka naam rakhte hain `/patient` aur saath mein ek **dynamic segment** `{patient_id}` add karte hain:

```python
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'patient not found'}
```

**Code ka line-by-line breakdown:**

| Line | Explanation |
|------|-------------|
| `@app.get('/patient/{patient_id}')` | Route define kiya - `{patient_id}` ek **variable** hai. Abhi nahi pata client kaunsa patient maangega, isliye curly braces mein likha |
| `def view_patient(patient_id: str)` | Function jo is route ko handle karega. Route se mili `patient_id` yahan parameter mein aati hai. **Type hint `str`** isliye hai kyunki hamare `patients.json` mein IDs strings hain (`P001`, `P002`, etc.) |
| `data = load_data()` | Last video mein banaya hua utility function - poora JSON data load karta hai as a Python dictionary |
| `if patient_id in data:` | Check karta hai ki yeh patient ID hamare dictionary mein ek **key** ke roop mein exist karti hai ya nahi |
| `return data[patient_id]` | Agar exist karti hai toh us patient ka saara data (name, city, age, etc.) return kar do |
| `return {'error': 'patient not found'}` | Agar `if` condition false hai (patient ID nahi mili), toh error message return karo |

**Flow samjho:**

```
Client URL mein likhta hai: /patient/P001
          │
          
Route match hota hai: /patient/{patient_id}
patient_id variable mein "P001" aa jata hai
          │
          
Function view_patient(patient_id="P001") call hota hai
          │
          
data = load_data()    poora patients.json load hua
          │
          
Check: "P001" in data?
  ├── YES  return data["P001"]    Ananya Sharma ka data
  └── NO   return {'error': 'patient not found'}
```

---

### 9. Testing - Browser aur Swagger UI

Server run karo:

```bash
uvicorn main:app --reload
```

#### Browser se test karo:

| URL | Result |
|-----|--------|
| `http://localhost:8000/patient/P001` | Pehle patient (Ananya Sharma) ka data |
| `http://localhost:8000/patient/P003` | Teesre patient (Sneha Kulkarni) ka data |
| `http://localhost:8000/patient/P005` | Paanchve patient (Neha Sinha) ka data |
| `http://localhost:8000/patient/P999` | `{"error": "patient not found"}` |

#### Swagger UI (`/docs`) se test karo:

1. Browser mein `http://localhost:8000/docs` jaao
2. Naya endpoint dikhega: **GET /patient/{patient_id}**
3. Wahan clearly likha hoga ki `patient_id` ek **path parameter** hai aur **required** hai
4. **"Try it out"** click karo  `patient_id` field mein `P001` likho  **"Execute"** click karo
5. Neeche response mein us patient ka data dikh jaayega

---

### 10. Code Improvement - `Path` Function Se Readability Enhance Karna

Abhi Swagger UI mein endpoint dikhta hai, lekin client ko sirf itna pata chalta hai ki `patient_id` ek required path parameter hai. **Koi description ya example nahi dikhta** - toh client ko samajhne mein dikkat ho sakti hai ki patient ID ka format kya hai.

**Definition:**

> *"The `Path` function in FastAPI is used to provide metadata, validation rules, and documentation hints for path parameters in your API endpoints."*

#### `Path` Function Se Kya-Kya Kar Sakte Ho?

| Feature | Explanation |
|---------|-------------|
| **Title** | Path parameter ka title add karna |
| **Description** | Path parameter ka description add karna - client ko samajh aaye ki kya expect karna hai |
| **Example** | Ek ya multiple examples dena - taaki client ko pata chale ki input kaisa dikhta hai |
| **Validation (`ge`, `gt`, `le`, `lt`)** | Agar path parameter integer ho toh greater than, less than jaise constraints lagana (e.g., patient ID 0 se neeche nahi, 100 se upar nahi) |
| **`min_length` / `max_length`** | String path parameter ki minimum aur maximum length define karna |
| **`pattern` (regex)** | Regex pattern se data validation apply karna |

#### Practical Code - `Path` Function Use Karna

**Step 1 - Import karo:**

```python
from fastapi import FastAPI, Path
```

**Step 2 - Function parameter mein `Path()` call karo:**

```python
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'patient not found'}
```

**`Path()` ke arguments ka breakdown:**

| Argument | Value | Explanation |
|----------|-------|-------------|
| `...` (Ellipsis) | First argument | Yeh batata hai ki yeh path parameter **required** hai. Waise bhi saare path parameters required hote hain, lekin yeh ek achha practice hai explicitly likhna |
| `description` | `'ID of the patient in the DB'` | Swagger UI mein is parameter ke saath yeh description dikhega - client ko samajh aayega ki kya bhejna hai |
| `example` | `'P001'` | Swagger UI mein ek example value pre-fill hogi - client ko pata chal jaayega ki patient ID ka format kaisa hota hai |

#### Swagger UI Mein Fark

**Pehle (bina `Path`):**
- Sirf dikhta tha: `patient_id` - required, string
- Koi description nahi, koi example nahi

**Baad mein (`Path` ke saath):**
- Description dikhta hai: *"ID of the patient in the DB"*
- Example dikhta hai: *P001*
- Client ko clearly samajh mein aa jaata hai ki kya input dena hai

> **Key Takeaway:** `Path` function se aapke endpoints ki **readability enhance** hoti hai. Client ko pata chalta hai ki har parameter mein kya expected hai. Jab aap client ke saath kaam karte ho, toh achhi documentation bahut zaroori hai.


---

### 11. HTTP Status Codes - Response Ka Result Batane Wale Numbers

**Definition:**

> *"HTTP Status Codes are three-digit numbers returned by a web server to indicate the result of a client's request."*

Jab bhi server ek HTTP response prepare karta hai, toh us response mein hamesha ek **3-digit status code** add hota hai. Yeh code client ko batata hai ki uski request ke saath kya hua - successful rahi, ya kuch gadbad hui, aur agar gadbad hui toh kis tarah ki.

#### Status Code Categories

| Starts With | Category | Matlab |
|-------------|----------|--------|
| **2xx** | Success | Request successfully process ho gayi |
| **3xx** | Redirection | Further action chahiye request fulfill karne ke liye |
| **4xx** | Client Error | Client ki request mein kuch gadbad hai |
| **5xx** | Server Error | Server ki side se kuch gadbad hui |

#### Famous HTTP Status Codes

| Code | Name | Explanation |
|------|------|-------------|
| **200** | OK | Request sahi se process hui, response sahi aaya |
| **201** | Created | Naya resource successfully create ho gaya (POST requests mein common) |
| **204** | No Content | Success hai, lekin koi data return nahi karna (DELETE requests mein common) |
| **400** | Bad Request | Client ne galat request bheji - missing fields ya wrong data type |
| **401** | Unauthorized | Login kiye bina protected resource access karne ki koshish |
| **403** | Forbidden | Login ho chuka hai, lekin is resource ko dekhne ki permission nahi hai |
| **404** | Not Found | Jo resource client dhoondh raha hai, woh exist hi nahi karta |
| **500** | Internal Server Error | Server pe hi kuch gadbad ho gayi |
| **502** | Bad Gateway | HTTP communication beech mein broken ho gayi |
| **503** | Service Unavailable | Server down hai ya overloaded hai - baad mein try karo |

---

### 12. Code Improvement - `HTTPException` Se Proper Error Handling

**Problem:** Hamare puraane code mein jab patient nahi milta tha, toh hum ek normal JSON return kar rahe the:

```python
return {'error': 'patient not found'}
```

Yeh dikhne mein theek lagta hai, **lekin status code 200 (OK) aa raha tha** - jo galat hai. Kyunki resource mila nahi aur status code bol raha hai "sab sahi hai". Ideally **404 (Not Found)** aana chahiye.

**Solution:** FastAPI ka built-in **`HTTPException`** use karo.

**Definition:**

> *"HTTPException is a special built-in exception in FastAPI that is used to return custom HTTP error responses when something goes wrong in your API."*

Normal JSON return karne ke bajaye, aap gracefully ek **error raise** kar sakte ho jismein proper HTTP status code aur custom error message dono ho.

#### Updated Code

```python
from fastapi import FastAPI, Path, HTTPException

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')
```

**Puraana vs Naya - Comparison:**

| | Puraana Code | Naya Code |
|--|-------------|----------|
| **Kya karta hai** | Normal JSON return karta hai | HTTP exception raise karta hai |
| **Status Code** | 200 (galat - success bol raha hai) | 404 (sahi - resource nahi mila) |
| **Response Body** | `{"error": "patient not found"}` | `{"detail": "Patient not found"}` |
| **Best Practice?** | Nahi | Haan |

**`HTTPException` ke arguments:**

| Argument | Value | Explanation |
|----------|-------|-------------|
| `status_code` | `404` | HTTP status code jo client ko milega - yahan 404 = Not Found |
| `detail` | `'Patient not found'` | Custom error message jo response body mein dikhega |

> **Going Forward Rule:** Is project mein jab bhi kuch bhi gadbad hogi, toh normal JSON return karne ke bajaye hum **`HTTPException` raise karenge** with proper status code. Yeh industry best practice hai.

---

### 13. Important Terms

| Term | Explanation |
|------|-------------|
| **Path Parameter** | URL ka dynamic segment jo ek specific resource ko identify karta hai |
| **Dynamic Segment** | URL ka woh hissa jo har request mein badal sakta hai |
| **Fixed Segment** | URL ka woh hissa jo har request mein same rehta hai (domain, route name) |
| **Resource** | Server par stored koi bhi data item (e.g., ek patient record, ek user profile) |
| **Type Hint (`: str`)** | Function parameter ke expected data type ko specify karna |
| **`Path` function** | FastAPI ka built-in function jo path parameters ki readability aur validation enhance karta hai |
| **HTTP Status Code** | 3-digit number jo server response mein aata hai - request ka result batata hai |
| **`HTTPException`** | FastAPI ka built-in exception jo custom error responses (proper status code + message) return karta hai |
| **`raise`** | Python keyword jo exception trigger karta hai - `return` ki jagah use hota hai error cases mein |

---

### 14. Summary

- **Path Parameters** URL ke dynamic segments hote hain jo server par kisi **specific resource ko identify** karte hain.
- URL mein domain aur route name fixed rehte hain - sirf path parameter wala hissa dynamic hota hai.
- Path Parameters teen main CRUD operations mein use hote hain: **Retrieve (GET), Update (PUT), Delete (DELETE)**.
- Hamare project mein naya endpoint bana: `GET /patient/{patient_id}` - path parameter se specific patient ka data milta hai.
- **`Path` function** se Swagger docs mein description aur example add karke readability improve hoti hai.
- **HTTP Status Codes** 3-digit numbers hain jo batate hain request ka result kya raha - 2xx (success), 4xx (client error), 5xx (server error).
- Normal JSON return karne ke bajaye **`HTTPException`** raise karna best practice hai - proper status code (e.g., 404) aur custom error message ke saath.
- Do improvements kiye: (1) **`Path` function** se readability enhance ki, (2) **`HTTPException`** se proper error handling add ki.

---

## Topic 11: Query Parameters - Optional Data Bhejna URL Ke Through

### 1. Introduction

Path Parameters ke baad ab samajhte hain ek doosra bahut important concept - **Query Parameters**. Yeh bhi URL ke through data bhejne ka ek tarika hai, lekin inka nature **optional** hota hai.

---

### 2. Problem - Sorting Ki Zaroorat

Hamare project mein ek existing endpoint hai `GET /view` jo **saare patients ka data** chronologically dikhata hai (jis order mein database mein enter hua).

**Naya Requirement:** Client ko yeh flexibility dena hai ki agar woh chahe toh data ko **sorted manner** mein dekh sake:

- **Sort By:** Kis column ke basis pe sorting karni hai - `height`, `weight`, ya `bmi`
- **Order:** Ascending ya Descending

Aur sabse important baat - yeh dono **optional** hone chahiye. Agar client ne yeh values nahi bheji, toh default tarike se data dikhao.

---

### 3. Query Parameters - Kya Hain?

**Definition:**

> *"Query Parameters are optional key-value pairs appended to the end of the URL, used to pass additional data to the server in an HTTP request. They are typically employed for operations like filtering, sorting, searching, and pagination - without altering the endpoint path itself."*

#### URL Structure

```
http://localhost:8000/view?sort_by=weight&order=asc
│                    │   │          │     │         │
│   Endpoint URL     │   │  Query Parameter 1      │
│                    │   │                          │
│                    │   │       Query Parameter 2  │
│                    │   │                          │
│                    ?  Question mark (query params start)
│                        &  Ampersand (separator between params)
```

#### Key Rules:

| Rule | Explanation |
|------|-------------|
| **`?` (Question Mark)** | Query parameters yahan se shuru hote hain - endpoint URL ke baad |
| **Key-Value Pair** | Har parameter ek `key=value` format mein hota hai (e.g., `sort_by=weight`) |
| **`&` (Ampersand)** | Multiple query parameters ko separate karne ke liye use hota hai |
| **Optional** | Query parameters by default **optional** hote hain - nahi bhejna ho toh mat bhejo |

#### Examples:

```
# Sirf sorting by weight
http://localhost:8000/view?sort_by=weight

# Sorting by weight in descending order
http://localhost:8000/view?sort_by=weight&order=desc

# Filtering by city (future example)
http://localhost:8000/patients?city=Delhi&sort_by=age
```

---

### 4. Query Parameters Kahan Use Hote Hain?

| Use Case | Example | Explanation |
|----------|---------|-------------|
| **Sorting** | `?sort_by=weight&order=asc` | Data ko kisi column ke basis pe sort karna |
| **Filtering** | `?city=Delhi&gender=male` | Specific conditions ke basis pe data filter karna |
| **Searching** | `?query=AI+Agents` | Search bar se query bhejna |
| **Pagination** | `?page=2&limit=10` | Bahut zyada data mein pages banana - page 2 ke 10 records dikhao |

> **Key Point:** Query parameters se aap **existing endpoint ke path ko change kiye bina** additional features add kar sakte ho.

---

### 5. Path Parameters vs Query Parameters - Comparison

| | Path Parameter | Query Parameter |
|--|---------------|----------------|
| **Position** | URL path mein (`/patient/P001`) | URL ke end mein `?` ke baad (`?sort_by=weight`) |
| **Required?** | Hamesha **required** | By default **optional** |
| **Kaam** | Specific resource **identify** karna | Additional data / options **pass** karna |
| **Example** | Ek specific patient ka data dekhna | Data ko sorted order mein dekhna |
| **Syntax** | `/route/{variable}` | `/route?key=value&key2=value2` |

---

### 6. Hamara Project - Sorting Endpoint Ka Plan

Ek naya endpoint banayenge jo query parameters ki madad se patients ka data sorted order mein dikhayega:

**Endpoint:** `GET /view` (with query params)

**Do query parameters:**

| Parameter | Options | Default | Explanation |
|-----------|---------|---------|-------------|
| `sort_by` | `height`, `weight`, `bmi` | None (no sorting) | Kis column ke basis pe sort karna hai |
| `order` | `asc`, `desc` | `asc` | Ascending ya descending order |

**Possible URL combinations:**

```
# Koi sorting nahi - default order mein data
GET /view

# Weight ke basis pe ascending (default order)
GET /view?sort_by=weight

# BMI ke basis pe descending order
GET /view?sort_by=bmi&order=desc

# Height ke basis pe ascending order
GET /view?sort_by=height&order=asc
```

---

### 7. `Query` Function - Query Parameters Ko Enhance Karna

Jaise Path Parameters ke liye `Path` function tha, waise hi Query Parameters ke liye **`Query`** function hai.

> *"Query is a utility function provided by FastAPI to declare, validate, and document query parameters in your API endpoints."*

**Import karo:**

```python
from fastapi import FastAPI, Path, HTTPException, Query
```

**`Query` function se kya-kya kar sakte ho:**

| Feature | Explanation |
|---------|-------------|
| **Default Value** | Query parameter ki default value set karna (e.g., `Query('asc')`  default `asc`) |
| **Required banana** | `Query(...)` - teen dots = required (client ko value deni padegi) |
| **Title / Description** | Swagger docs mein readable metadata add karna |
| **Example(s)** | Ek ya multiple examples dena |
| **`min_length` / `max_length`** | String length constraints |
| **Regex pattern** | Custom validation pattern |

> `Query` function bilkul `Path` function ki tarah kaam karta hai - bas yeh query parameters ke liye hai.

---

### 8. Code Demo - Sorting Endpoint

```python
from fastapi import FastAPI, Path, HTTPException, Query

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort on the basis of height, weight or BMI'),
    order: str = Query('asc', description='Sort in asc or desc order')
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')

    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
```

**Code ka breakdown:**

| Line | Explanation |
|------|-------------|
| `sort_by: str = Query(...)` | Pehla query parameter - **required** hai (teen dots). Client ko batana padega kis column se sort karna hai |
| `order: str = Query('asc', ...)` | Doosra query parameter - **optional** hai. Default value `'asc'` set hai. Agar client ne nahi bheja toh ascending order mein sort hoga |
| `valid_fields = ['height', 'weight', 'bmi']` | Allowed columns ki list - sirf inhi teen ke basis pe sorting hogi |
| `if sort_by not in valid_fields` | Check karta hai ki client ne valid column diya ya nahi. Nahi diya toh **400 Bad Request** |
| `if order not in ['asc', 'desc']` | Check karta hai ki order sahi hai ya nahi. Galat diya toh **400 Bad Request** |
| `data = load_data()` | Poora patient data load karta hai |
| `sort_order = True if order == 'desc' else False` | Python ka `sorted()` function `reverse=True` pe descending sort karta hai, `False` pe ascending |
| `sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)` | Dictionary ki values nikal ke, specified column ke basis pe sort karta hai |

**Required vs Optional - Difference:**

| Parameter | `Query()` Value | Required? | Explanation |
|-----------|----------------|-----------|-------------|
| `sort_by` | `Query(...)` | Haan (required) | Teen dots = client ko value deni padegi |
| `order` | `Query('asc')` | Nahi (optional) | Default value set hai - nahi bheji toh `'asc'` use hoga |

---

### 9. Testing - Browser aur Swagger UI

#### Browser se test karo:

| URL | Result |
|-----|--------|
| `/sort?sort_by=height&order=desc` | Height ke basis pe descending - sabse zyada height pehle |
| `/sort?sort_by=bmi&order=desc` | BMI ke basis pe descending - sabse zyada BMI pehle |
| `/sort?sort_by=bmi` | BMI ke basis pe **ascending** (default order) - sabse kam BMI pehle |
| `/sort?sort_by=xyz` | **400 Error** - "Invalid field select from ['height', 'weight', 'bmi']" |
| `/sort?sort_by=bmi&order=xyz` | **400 Error** - "Invalid order select between asc and desc" |

#### Swagger UI (`/docs`) se test karo:

1. `http://localhost:8000/docs` mein jaao
2. **GET /sort** endpoint dikhega - dono query parameters listed honge
3. `sort_by` mein `height`/`weight`/`bmi` aur `order` mein `asc`/`desc` dalke test karo
4. Galat values dalke bhi test karo - 400 errors aayenge proper messages ke saath

---

### 10. Video Summary - Path Parameters vs Query Parameters (Final Recap)

| | Path Parameters | Query Parameters |
|--|----------------|-----------------|
| **Kya hai** | URL ka dynamic part | URL ke end mein `?` ke baad key-value pairs |
| **Required?** | Hamesha **required** | By default **optional** |
| **Kaam** | Specific resource identify karna | Additional features add karna (sorting, filtering, search, pagination) |
| **Use kab** | Retrieve, Update, Delete ek specific resource | Existing endpoint mein extra functionality |
| **Syntax** | `/patient/{patient_id}` | `/sort?sort_by=bmi&order=desc` |
| **Enhance** | `Path` function se | `Query` function se |
| **Ek saath use?** | Haan - dono ek hi endpoint mein use ho sakte hain |

---

### 11. Important Terms

| Term | Explanation |
|------|-------------|
| **Query Parameter** | URL ke end mein `?` ke baad optional key-value pairs jo additional data server ko bhejte hain |
| **`?` (Question Mark)** | URL mein query parameters ke start ka indicator |
| **`&` (Ampersand)** | Multiple query parameters ke beech separator |
| **Key-Value Pair** | `key=value` format mein data - e.g., `sort_by=weight` |
| **`Query` function** | FastAPI ka built-in function jo query parameters declare, validate, aur document karta hai |
| **Required (`...`)** | Teen dots (Ellipsis) dalne se parameter required ban jaata hai |
| **Optional (default value)** | Default value set karne se parameter optional ban jaata hai |
| **`sorted()` function** | Python ka built-in function jo data ko sort karta hai - `reverse=True` pe descending |
| **`lambda`** | Python mein chota anonymous function - yahan sorting key define karne ke liye use hua |
| **400 Bad Request** | HTTP status code jo client ki galat request indicate karta hai |

---

### 12. Summary

- **Query Parameters** URL ke end mein `?` ke baad optional key-value pairs hote hain.
- Yeh **filtering, sorting, searching, aur pagination** jaise operations ke liye use hote hain.
- Path parameter **specific resource identify** karta hai (required), jabki query parameter **additional options pass** karta hai (optional).
- **`Query` function** se query parameters ko describe, validate, aur document kiya jaata hai - bilkul `Path` function ki tarah.
- `Query(...)` = **required**, `Query('default_value')` = **optional** with default.
- Hamare project mein sorting endpoint bana: `GET /sort?sort_by=bmi&order=desc` - dono query parameters ke saath proper validation aur error handling (400 Bad Request).
- Dono parameters (Path + Query) ek hi endpoint mein bhi use ho sakte hain.

---

## Topic 8: Pydantic - Data Validation Library for Python

### 1. Introduction

Pydantic ek bahut important Python library hai jiski help se aap **data validation** perform kar sakte ho. Python mein static typing ka concept nahi hai - Python ek **dynamically typed language** hai. Matlab aap ek variable mein integer value bhi store kar sakte ho aur usi variable mein string value bhi store kar sakte ho. Beginners ke liye yeh feature accha hota hai, but jab aap **production-grade code** likhne jaoge toh bahut jaldi realize hoga ki **type validation aur data validation** software programming ka ek bahut important aspect hai.

Pydantic ki help se aap:
- **Type Validation** perform kar sakte ho (ensure correct data types)
- Complex **Data Validation** bhi kar sakte ho (custom rules aur constraints)
- **Data Models** build kar sakte ho
- Complex data ko easily **structure** kar sakte ho

**Pydantic kahan-kahan use hota hai:**
- **FastAPI** mein APIs build karte waqt
- **YAML config files** ke saath kaam karte waqt
- **Data Science** mein ML pipelines build karte waqt
- Basically koi bhi **production-grade Python code** jahan data correctness zaroori ho

> **Important:** Hamesha Pydantic **V2** use karo. V2 Rust mein likha hai - bahut fast hai. V1 aur V2 mein kaafi differences hain. Install: `pip install pydantic`

---

### 2. Why Pydantic? - Problem Statement

Pydantic do badi problems solve karta hai. Dono problems ko practically samajhte hain.

#### Problem 1: Type Validation

Maan lo ek function hai jo patient data receive karke database mein insert karta hai:

```python
def insert_patient_data(name, age):
    print(name)
    print(age)
    print("Inserted into database")
```

Ab ek junior programmer is function ko use karta hai. Usko function signature mein dikhta hai ki `name` aur `age` chahiye - but koi type information nahi hai. Toh wo kuch bhi bhej sakta hai:

```python
insert_patient_data("Nitish", "30")  # age string mein bhej diya!
```

**Problem:** Yeh code kaam kar jayega! Python koi error nahi dega. Database mein galat type ki value insert ho jayegi. Yeh ek bahut bada failure hai - type validation nahi ho rahi.

**Attempt 1 - Type Hinting:**

```python
def insert_patient_data(name: str, age: int):
    print(name)
    print(age)
    print("Inserted into database")
```

Ab function signature mein dikhta hai ki `name` string hona chahiye aur `age` integer. But agar junior programmer phir bhi galat type bhejta hai (`age = "30"` as string), toh **code phir bhi kaam kar jayega!** Kyunki Python ki type hinting **errors produce nahi karti** - yeh sirf informational hai, enforce nahi karti.

**Attempt 2 - Manual Type Checking (if-else):**

```python
def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted into database")
    else:
        raise TypeError("Incorrect data type")
```

Ab agar koi galat type bhejta hai toh error aayega. **But yeh approach scalable nahi hai.** Kyun?

- Agar ek aur function hai `update_patient_data(name, age)` toh usme bhi **same validation code copy-paste** karna padega.
- Agar naya field add hota hai (e.g., `weight`), toh **saare functions mein jaake update** karna padega.
- Sab jagah yahi boilerplate code repeat hoga.

---

#### Problem 2: Data Validation

Type sahi hone ke baad bhi, data ki **specific requirements** validate karni hoti hain. For example:

```python
def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative")
        else:
            print(name)
            print(age)
            print("Inserted into database")
    else:
        raise TypeError("Incorrect data type")
```

**Ab imagine karo:**
- Agar `email` field bhi aaye  email format validate karna padega
- Agar `phone` field aaye  phone number format validate karna padega
- 10 variables aayein  10 ke liye alag-alag data validation likhna padega
- **Plus** yahi sab `update_patient_data()` mein bhi copy-paste karna padega

> **Bottom line:** Production-grade function likhne ke liye bahut saara **boilerplate code** likhna padta hai manually - type checking, data validation, error handling. Yeh **scalable nahi hai** aur **maintainable nahi hai**.

---

### 3. How Pydantic Works - 3 Steps

Pydantic essentially **3 steps** mein kaam karta hai. Yeh samajh lo toh pura Pydantic samajh aa jayega:

#### Step 1: Pydantic Model banana (Schema define karna)

Ek **class** banate ho jo `BaseModel` inherit karti hai. Is class ke andar aap apne data ka **ideal schema** define karte ho - kaunse fields chahiye aur unka data type kya hoga.

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str       # field_name: data_type
    age: int
```

> **Yaad rakhne ka tarika:** Pydantic model = Python class + `BaseModel` inherit + fields ke saath type batana. Bas itna hi hai Step 1.

---

#### Step 2: Raw data se object banana (Validation auto hoti hai)

Ab ek dictionary (raw data) banao aur usse is class ka **object** banao. **Jab object banta hai, TAB validation automatically hoti hai:**
- Sab required fields present hain? 
- Har field ka type sahi hai? 
- Constraints follow ho rahe hain? 

Agar kuch bhi galat hoga  **ValidationError** aayega, object banega hi nahi.

```python
# Raw data - dictionary
patient_info = {'name': 'Nitish', 'age': 25}

# Object banao - ** se dictionary unpack hoti hai
patient1 = Patient(**patient_info)

# Ye same hai:
# patient1 = Patient(name='Nitish', age=25)
```

> **`**` kya karta hai?** Dictionary ke key-value pairs ko function arguments mein convert karta hai. `{'name': 'Nitish', 'age': 25}`  `name='Nitish', age=25`

---

#### Step 3: Validated object ko function mein use karna

Ab function ko individual `name`, `age` nahi milta - ek **pura validated object** milta hai. Object ke andar `.name`, `.age` se values access karte hain.

```python
def insert_patient(patient: Patient):       # Patient type ka object chahiye
    print(patient.name)                     # object.field_name se access karo
    print(patient.age)
    print("Inserted into database")

insert_patient(patient1)                    # Step 2 ka object bhejo
```

**Fayda:** Ab chahe `insert_patient()` ho ya `update_patient()` ho - dono ko same `Patient` object chahiye. Validation ek jagah hoti hai (model mein), har function mein repeat nahi karni padti.

```python
def update_patient(patient: Patient):       # same model, no duplicate validation!
    print(f"Updating: {patient.name}")
    print("Updated in database")
```

---

### 4. Complex Fields - List, Dict, Optional

#### Basic Types

```python
class Patient(BaseModel):
    name: str           # string
    age: int            # integer
    weight: float       # decimal number (65.5, 75.2)
    married: bool       # True / False
```

#### Complex Types - List aur Dict

Agar aap sirf `list` likhoge toh Pydantic sirf check karega ki "yeh list hai". But **list ke andar kya hona chahiye** - woh check nahi hoga. Isliye hum `list[str]` likhte hain - matlab "list honi chahiye, aur usme har item string hona chahiye."

```python
class Patient(BaseModel):
    allergies: list[str]               # list ka har item string hona chahiye
    contact_details: dict[str, str]    # dictionary jisme key=string, value=string
```

> **Yaad rakho:** `list[str]` = 2-level validation  pehle check: list hai? phir check: har item string hai?
> `dict[str, str]` = key bhi string, value bhi string.

#### Optional Fields

By default **saari fields required** hoti hain. Agar koi field optional banana ho toh:

```python
class Patient(BaseModel):
    name: str                                   # required
    age: int                                    # required
    allergies: list[str] | None = None          # optional - na bhejo toh None aa jayega
    married: bool = False                       # optional with default value
```

> **Yaad rakho:** Optional banana = `| None = None` ya `default value` dena. Bina default ke sab kuch required hai.

---

### 5. Data Validation - 3 Tarike

#### Tarika 1: Pydantic ke Custom Data Types (Built-in validators)

Pydantic kuch special data types deta hai jo common validations automatically kar dete hain:

```python
from pydantic import BaseModel, EmailStr   # EmailStr ke liye: pip install pydantic[email]

class Patient(BaseModel):
    email: EmailStr     # auto-validates email format (@ hona chahiye, domain hona chahiye)
```

- Sahi: `"abc@gmail.com"` 
- Galat: `"abcgmail.com"`  (@ nahi hai  error)

**Simlarly:**

```python
from pydantic import AnyUrl

class Patient(BaseModel):
    linkedin_url: AnyUrl    # URL format validate karta hai (http:// ya https:// hona chahiye)
```

- Sahi: `"https://linkedin.com/in/nitish"` 
- Galat: `"linkedin.com/in/nitish"`  (http:// nahi hai  error)

> **Yaad rakho:** Common validations (email, URL) ke liye Pydantic ke built-in types use karo - khud regex likhne ki zaroorat nahi!

---

#### Tarika 2: `Field()` Function - Custom Business Rules

Jab aapke **business ke hisaab se** custom rules lagane hain (e.g., age 0 se 120 ke beech hi ho), tab `Field()` function use hota hai.

```python
from pydantic import BaseModel, Field

class Patient(BaseModel):
    age: int = Field(gt=0, lt=120)              # age > 0 AND age < 120
    weight: float = Field(gt=0)                 # weight > 0
    name: str = Field(max_length=50)            # naam max 50 characters
    allergies: list[str] = Field(max_length=5)  # max 5 allergies list mein
```

**Field() ke available constraints:**

| Constraint | Kya karta hai | Example | Kahan use hota hai |
|-----------|--------------|---------|-------------------|
| `gt=0` | greater than 0 | `Field(gt=0)` | numbers (int/float) |
| `lt=120` | less than 120 | `Field(lt=120)` | numbers |
| `ge=0` | greater than or equal to 0 | `Field(ge=0)` | numbers |
| `le=100` | less than or equal to 100 | `Field(le=100)` | numbers |
| `max_length=50` | max 50 characters/items | `Field(max_length=50)` | strings, lists |
| `min_length=1` | minimum 1 character/item | `Field(min_length=1)` | strings, lists |
| `strict=True` | type conversion band karo | `Field(strict=True)` | koi bhi type |
| `default=value` | default value set karo | `Field(default=False)` | koi bhi field |

---

#### Tarika 3: `Annotated` + `Field()` - Full Power Syntax (Recommended)

Jab aapko ek field mein **data type + constraints + metadata** sab ek saath likhna ho, toh `Annotated` use karo. Yahi syntax sabse zyada professional code mein dikhega:

```python
from typing import Annotated
from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: Annotated[str, Field(
        max_length=50,
        title="Patient Name",
        description="Patient ka full name, 50 chars max",
        examples=["Nitish", "Amit"]
    )]
    
    age: Annotated[int, Field(gt=0, lt=120)]

    weight: Annotated[float, Field(gt=0, strict=True)]

    married: Annotated[bool, Field(
        default=False,
        description="Is the patient married or not"
    )]

    allergies: Annotated[list[str] | None, Field(
        default=None,
        max_length=5
    )]
```

> **`Annotated` ko aise samjho:** `Annotated[TYPE, FIELD(...)]` = pehle **type** batao, phir **rules aur metadata** batao. Bas!

**Field() se 3 kaam hote hain:**
1. **Data Validation** - `gt=0`, `max_length=50`, etc.
2. **Metadata** - `title`, `description`, `examples` (FastAPI docs mein dikhte hain)
3. **Default Values** - `default=None`, `default=False`

---

### 6. Smart Type Coercion (aur usse rokna)

Pydantic by default **smart** hai - agar aap `"30"` string bhejo age mein, toh wo khud samajh ke `30` integer bana deta hai (kyunki `"30"` ko int mein convert karna possible hai).

```python
patient_info = {'name': 'Nitish', 'age': '30'}  # age string mein hai
patient1 = Patient(**patient_info)
print(patient1.age)   # 30 (integer) - Pydantic ne convert kar diya!
```

**Yeh feature helpful bhi hai aur dangerous bhi.** Agar aap chahte ho ki **bilkul sahi type hi aaye, convert mat karo**, toh `strict=True` lagao:

```python
weight: Annotated[float, Field(gt=0, strict=True)]
```

Ab `"65.0"` string bhejoge toh **error** aayega - sirf `65.0` float hi chalega.

> **Yaad rakho:** `strict=True` = "exactly yahi type chahiye, convert mat karna." Use it jab aapko 100% sure hona hai ki sahi type aa rahi hai.

---

### 7. Important Terms

| Term | Explanation |
|------|-------------|
| **Pydantic** | Python ki data validation library - type aur data validation enforce karti hai |
| **BaseModel** | Pydantic ki base class - isko inherit karke apna model banate hain |
| **Dynamic Typing** | Python ka feature jahan ek variable mein koi bhi type store ho sakti hai |
| **Static Typing** | Java/C++ jaisi languages mein variable ka type fix hota hai |
| **Type Hinting** | `name: str` likhna - sirf informational, enforce nahi karta |
| **ValidationError** | Pydantic ka error - jab data type ya constraints fail kare |
| **Field()** | Function jo constraints (gt, lt), metadata (title, description), aur defaults set karta hai |
| **Annotated** | `typing` module se - `Annotated[type, Field(...)]` syntax mein type + rules ek saath likhte hain |
| **Type Coercion** | Pydantic ka smart behavior - `"30"` string ko `30` int mein auto-convert karna |
| **strict=True** | Type coercion band karna - exact type hi accept hoga |
| **EmailStr** | Pydantic ka built-in type - email format validate karta hai |
| **AnyUrl** | Pydantic ka built-in type - URL format validate karta hai |
| **`**dict`** | Dictionary unpack - `{'a':1}` -> `a=1` mein convert hota hai |

---

### 8. FastAPI in ML/AI/RAG

Pydantic ka role FastAPI aur ML/AI systems mein critical hai:

- **FastAPI Request Validation:** FastAPI internally Pydantic use karta hai. Jab aap Pydantic model define karte ho, FastAPI automatically galat requests reject kar deta hai. `Field()` ka metadata (title, description) FastAPI ke Swagger docs mein automatically dikhta hai.
- **ML Pipeline Input Validation:** ML pipelines mein input data ka correct format hona zaroori hai. Pydantic se har stage par data quality enforce hoti hai.
- **LLM Structured Output:** LLMs ka output unpredictable hota hai. Pydantic se strict schema enforce kar sakte ho (LangChain/LlamaIndex pattern).
- **Config Management:** ML experiments mein hyperparameters aur settings ko Pydantic se validate karo - galat config se experiment fail hone se pehle error mil jaata hai.

---

### 9. Summary

- Pydantic 3 steps mein kaam karta hai: (1) Model/class banao (schema define karo) -> (2) Raw data se object banao (validation auto hoti hai) -> (3) Validated object function mein use karo.
- BaseModel inherit karna zaroori hai - tabhi class Pydantic model banegi.
- Saari fields by default required hain - optional banana ho toh = None ya default value do.
- Complex types: list[str] = list jisme har item string ho. dict[str, str] = dict jisme key aur value dono string ho.
- Data Validation ke 3 tarike: (1) Built-in types (EmailStr, AnyUrl), (2) Field() function (gt, lt, max_length), (3) Annotated[type, Field(...)] - recommended full-power syntax.
- Field() ke 3 kaam: Data validation + Metadata + Default values.
- Pydantic by default type coercion karta hai ("30" -> 30). Rokna ho toh strict=True.
- Ek baar model define karo -> n functions mein reuse karo - no boilerplate!

---

### 10. Syntax Cheatsheet - Quick Revision

Jab bhool jaao toh yahan dekh lo:

```python
# --- IMPORTS ---
from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import Annotated

# --- BASIC MODEL ---
class Patient(BaseModel):
    name: str                   # required string
    age: int                    # required integer

# ═══════════ COMPLEX TYPES ═══════════
class Patient(BaseModel):
    allergies: list[str]        # list of strings
    contacts: dict[str, str]    # dict with string keys and string values

# ═══════════ OPTIONAL FIELDS ═══════════
class Patient(BaseModel):
    allergies: list[str] | None = None    # optional - None if not provided
    married: bool = False                 # optional with default False

# ═══════════ FIELD() - CONSTRAINTS ═══════════
class Patient(BaseModel):
    age: int = Field(gt=0, lt=120)        # 0 < age < 120
    weight: float = Field(gt=0)           # weight > 0
    name: str = Field(max_length=50)      # max 50 chars

# ═══════════ ANNOTATED + FIELD() - FULL POWER ═══════════
class Patient(BaseModel):
    name: Annotated[str, Field(
        max_length=50,
        title="Patient Name",
        description="50 chars max",
        examples=["Nitish"]
    )]
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False)]
    allergies: Annotated[list[str] | None, Field(default=None, max_length=5)]

# ═══════════ BUILT-IN VALIDATORS ═══════════
class Patient(BaseModel):
    email: EmailStr             # validates email format
    # website: AnyUrl           # validates URL format

# ═══════════ OBJECT BANANA ═══════════
data = {'name': 'Nitish', 'age': 25, 'weight': 65.0}
patient = Patient(**data)       # ** = dictionary unpack

# ═══════════ FUNCTION MEIN USE ═══════════
def insert_patient(patient: Patient):
    print(patient.name)         # dot notation se access
    print(patient.age)

# --- FIELD VALIDATOR ---
from pydantic import field_validator

class Patient(BaseModel):
    name: str
    email: str

    @field_validator('email')            # kaunsi field pe lagana hai
    @classmethod                         # hamesha classmethod hona chahiye
    def validate_email(cls, value):      # cls = class, value = field ki value
        # custom logic likho
        if '@hdfc.com' not in value:
            raise ValueError('Not a valid domain')
        return value                     # HAMESHA value return karo!

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):      # transformation bhi kar sakte ho
        return value.upper()             # naam hamesha CAPITAL mein

# --- FIELD VALIDATOR - BEFORE/AFTER MODE ---
class Patient(BaseModel):
    age: int

    @field_validator('age', mode='after')     # default = 'after' (type coercion ke BAAD)
    @classmethod
    def check_age(cls, value):
        if not (0 < value < 100):
            raise ValueError('Age 0-100 ke beech hona chahiye')
        return value
    # mode='before'  type coercion ke PEHLE value milegi (raw input)

# --- MODEL VALIDATOR ---
from pydantic import model_validator

class Patient(BaseModel):
    age: int
    contacts: dict

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        # model parameter mein pura validated object milta hai
        if model.age > 60 and 'emergency' not in model.contacts:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

# --- COMPUTED FIELDS ---
from pydantic import computed_field

class Patient(BaseModel):
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

```

---

### 11. Field Validator - Custom Business Logic

#### Kab use karna hai?

Jab aapko kisi **ek field** ke upar **business-specific validation** ya **transformation** lagani ho jo Field() se possible nahi hai. For example:
- Email mein check karo ki domain hdfc.com ya icici.com hai
- Patient ka naam hamesha UPPERCASE mein store karo

> Yaad rakho: Field() = numeric range, length limit jaise simple rules. @field_validator = koi bhi complex custom logic jo aap Python code mein likh sako.

---

#### Syntax - Step by Step

```python
from pydantic import BaseModel, field_validator

class Patient(BaseModel):
    name: str
    email: str

    #  Decorator - batao kaunsi field pe lagana hai
    @field_validator('email')
    #  Hamesha @classmethod likhna zaroori hai
    @classmethod
    #  Method ka naam kuch bhi rakho. cls = class, value = us field ki value
    def validate_email(cls, value):
        # Apna custom logic likho
        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]       # @ ke baad wala part nikalo
        if domain not in valid_domains:
            raise ValueError('Not a valid domain')
        return value                        # HAMESHA value return karo!
```

**4 cheezein yaad rakhni hain:**
1. @field_validator('field_name') - decorator mein field ka naam batao
2. @classmethod - hamesha likhna hai
3. cls, value - method ko class aur field ki value milti hai
4. return value - hamesha value return karo (chahe change karo ya na karo)

---

#### Use Case 1: Custom Validation (Email domain check)

```python
@field_validator('email')
@classmethod
def validate_email(cls, value):
    valid_domains = ['hdfc.com', 'icici.com']
    domain = value.split('@')[-1]
    if domain not in valid_domains:
        raise ValueError('Not a valid domain')
    return value
```

- "abc@hdfc.com" kaam karega
- "abc@gmail.com" ValueError: Not a valid domain

---

#### Use Case 2: Transformation (Name uppercase)

```python
@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()        # "nitish" -> "NITISH"
```

Jab bhi patient object banega, naam automatically capital ho jayega. Koi extra code likhne ki zaroorat nahi.

---

#### Before vs After Mode

Field validator ko do modes mein chala sakte ho:

| Mode | Kab milti hai value | Default? | Use kab karo |
|--------------|-------------------|----------|-------------|
| mode='after' | Type coercion ke BAAD (converted value) | Haan (default) | Jab aapko final type ki value chahiye |
| mode='before' | Type coercion ke PEHLE (raw input) | Nahi | Jab raw input pe kaam karna ho |

**Example:**

```python
# Agar age = "30" (string) bheji aur model mein age: int hai:

@field_validator('age', mode='before')       # value = "30" (string milegi)
@field_validator('age', mode='after')        # value = 30  (int milegi - converted)
@field_validator('age')                      # same as mode='after' (default)
```

**Practical problem with mode='before':**
```python
@field_validator('age', mode='before')
@classmethod
def check_age(cls, value):
    if 0 < value < 100:      # ERROR! string aur int compare nahi ho sakta
        return value
    raise ValueError('Invalid age')
```

Agar age = "30" bheji toh value ek string hai ("30"), aur 0 < "30" compare nahi hoga kyunki Python string aur int compare nahi kar sakta. Solution: mode='after' use karo (default), toh value = 30 (int) milega.

> Yaad rakho: 99% cases mein mode='after' (default) hi sahi hai. mode='before' sirf tab use karo jab aapko raw input pe kuch karna ho.

---

### 12. Model Validator - Multi-field Validation

#### Kab use karna hai?

Jab aapka validation ek se zyada fields par depend karta ho. 
Example: Agar patient ki age 60 se zyada hai, toh humein ek emergency contact number zaroori chahiye. Simple Field() ya field_validator se yeh nahi ho sakta kyunki woh sirf ek field ko dekhte hain.

#### Syntax

```python
from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    age: int
    contacts: dict

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        # 'model' parameter mein pura object (Patient) milta hai 
        # jisme saari fields accessible hain (age, contacts, etc.)
        if model.age > 60 and 'emergency' not in model.contacts:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
```

**Key Points:**
- @model_validator(mode='after') use karo.
- Method ko cls aur model (ya self) milta hai.
- Isme aap model.age aur model.contacts dono ko ek saath check kar sakte ho.

---

### 13. Computed Fields - Dynamic Data

#### Kab use karna hai?

Aisi field jo user se input nahi milti, balki baki fields se calculate hoti hai.
Example: User weight aur height deta hai, hum BMI khud calculate karke model mein add kar dete hain.

#### Syntax

```python
from pydantic import BaseModel, computed_field

class Patient(BaseModel):
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        # bmi calculate karke return karo
        result = self.weight / (self.height ** 2)
        return round(result, 2)
```

**Important:**
- @computed_field aur @property dono hamesha saath use hote hain.
- Method ka jo naam hoga (yahan 'bmi'), wahi field ka naam ban jayega.
- isse hum object.bmi karke value access kar sakte hain.

### 14. Nested Models - Hierarchy in Data

#### Kab use karna hai?

Jab aapka data complex ho aur uske andar bhi ek structure ho. Example: Patient ke data mein Address bhi hai. Address ke andar City, State, Pin Code hota hai. Agar address ko simple string rakhoge toh data access karna mushkil hoga. Iska solution hai **Nested Models** - yaani ek Pydantic model ke andar dusra model.

#### Syntax

```python
from pydantic import BaseModel

# 1. Pehle sub-component ka model banao
class Address(BaseModel):
    city: str
    state: str
    pincode: int

# 2. Phir main model mein use karo
class Patient(BaseModel):
    name: str
    age: int
    address: Address        # Nested model
```

#### Benefits:
- **Better Organization:** Data structure neat aur clean rehta hai.
- **Auto Validation:** Address ke fields (City, State etc.) bhi automatically validate ho jate hain.
- **Easy Access:** Dot notation se asani se data nikal sakte ho: `patient.address.city`.
- **Reusability:** Address model ko aap Student ya Employee model mein bhi reuse kar sakte ho.

---

### 15. Exporting Models - Dictionary & JSON

#### Kab use karna hai?

Jab aapne Pydantic object bana liya, validation ho gayi, ab aapko woh data wapas ek simple Python Dictionary (`dict`) ya JSON string format mein chahiye (e.g., database mein save karne ke liye ya framework jaise FastAPI mein API response bhejne ke liye, ya debugging ke liye).

#### 1. Dictionary mein Export (`model_dump`)

```python
# Pydantic object ko dict mein convert karna
patient_dict = patient.model_dump()

print(type(patient_dict))   # <class 'dict'>
print(patient_dict)         # {'name': 'Nitish', 'address': {'city': 'Gurgaon', ...}}
```

**Key Point:** `model_dump()` nested objects ko bhi dictionary mein convert kar deta hai automatically.

#### 2. JSON String mein Export (`model_dump_json`)

Agar aapko seedha JSON text (string) chahiye, toh aap `model_dump_json()` use kar sakte ho.

```python
# Pydantic object ko json string mein convert karna
patient_json = patient.model_dump_json()

print(type(patient_json))   # <class 'str'>
print(patient_json)         # {"name": "Nitish", "address": {"city": "Gurgaon", ...}}
```

---

### 16. Export Filtering - Data Control Karna

Jab aap data export karte ho, kabhi-kabhi aapko pura data nahi bhejta hota. Password, internal IDs, ya unnecessary fields ko hide karna padta hai. Pydantic iske liye bohat saare options deta hai.

#### 1. Sirf specific fields bhejna (`include`)

Agar aapko sirf naam chahiye baki sab ignore karna hai:

```python
# Sirf name field export hogi
data = patient.model_dump(include={'name'}) 
print(data)  # {'name': 'Nitish'}
```

#### 2. Specific fields ko hatana (`exclude`)

Agar aapko naam aur age chhodke baaki sab chahiye:

```python
# name aur age export nahi hongi
data = patient.model_dump(exclude={'name', 'age'}) 
```

**Nested fields exclude karna:**
Agar 'address' ke andar 'state' field nahi bhejna hai, toh aap is tarah se dictionary bhej sakte ho:

```python
# Address ke andar state nahi aayega
data = patient.model_dump(exclude={'address': {'state'}}) 
```

#### 3. Default values ko hide karna (`exclude_unset`)

Maan lo aapne model mein `gender: str = 'Male'` default set kiya hai. Lekin patient create karte time aapne `gender` field provide nahi ki (woh default value utha liya).
Agar aap chahte ho ki aise fields (jo user ne actually "set" nahi kiye they) export na hon, toh aap `exclude_unset=True` use kar sakte ho.

```python
# Sirf wahi data export hoga jo explicit provide kiya gaya tha
data = patient.model_dump(exclude_unset=True) 
```

Yeh database queries optimization ya API response payload size chhota karne mein bohat kaam aata hai.

---
