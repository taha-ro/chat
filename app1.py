import streamlit as st
import psycopg
# address='postgresql://neondb_owner:npg_x3iBFOE7gNsX@ep-solitary-tree-ah78vw8j-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require'
#         conn = psycopg.connect(address)

import psycopg

class Insert_table:

    TABLE_CREATED = False  # prevent recreating table every time

    def __init__(self, id, name, word):
        address='postgresql://neondb_owner:npg_x3iBFOE7gNsX@ep-solitary-tree-ah78vw8j-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require'
        conn = psycopg.connect(address)
        conn.autocommit = True
        cur = conn.cursor()

        self.name = str(name)
        self.id = str(id)
        self.word = str(word)

        # Create table ONCE
        if not Insert_table.TABLE_CREATED:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS connect(
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    text TEXT
                );
            """)
            Insert_table.TABLE_CREATED = True

        # Insert safely
        cur.execute("""
        INSERT INTO connect (id, name, text)
        VALUES (%s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """, (self.id, self.name, self.word))

        cur.close()
        conn.close()

    @classmethod
    def status(cls, id, name, word):
        id = str(id)
        name = str(name)
        word = str(word)
        address='postgresql://neondb_owner:npg_x3iBFOE7gNsX@ep-solitary-tree-ah78vw8j-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require'
        conn = psycopg.connect(address)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("SELECT * FROM connect;")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        if (id, name, word) in rows:
            print('yes')
            return "sended"
        else:
            print('no')
            return "failed please try again"




if "Done" not in st.session_state:
    st.session_state.Done = False

st.set_page_config(page_title="conncetion", layout="centered")

params = st.query_params


# --- When Next is clicked ---
if "next" in params:
    her_name=' '
    connection=' '
    if st.session_state.Done:
        st.empty()  # clears existing elements
        # A='your name:' + str(her_name) + '-- your id:'+ str(connection)  
        # st.write(A)
        st.write("✅ Done")
        st.stop()
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap" rel="stylesheet">
        <style>
        .farsi-hi {
            font-family: 'Vazirmatn', sans-serif;
            font-size: 28px;
            color: white;
            text-align: center;
            margin-top: 100px;
            direction: rtl;
        }
        body { background-color: black; }
        </style>
        <p class="farsi-hi">سلام! 🙌 یه برنامه نویس خجالتی که اگه مایل باشید دوست داره باشما بیشتر آشنا بشه(ماشین برقی سفیده) اگه هم مایل نیستید ببخشید وقتتون رو گرفتم </p>
        """,
        unsafe_allow_html=True,
    )
    her_name=str(st.text_input("name", placeholder="name:",label_visibility="hidden"))
    connection = str(st.text_input("connection", placeholder="یک راه ارتباطی هرچی که راحت هستید برای هماهنگی یه قرار کافه (id- eamil -number): ",label_visibility="hidden"))
    text_main =str(st.text_input("text", placeholder=" اگه صحبتی دارید ",label_visibility="hidden"))
    b0=st.button('send')
    if b0:
        Insert_table(connection,her_name ,text_main)
        state=Insert_table.status(connection,her_name ,text_main)
        st.write(state)
    b1=st.button('my connection')
    if b1:
        st.write('telegram id: @Ro_Taha')
        print(her_name)
    
    if st.button("Done"):
        st.empty()  # clears existing elements
        A='your name:' + her_name + '-- your id:'+ str(connection)  
        st.write(her_name)
        st.write("✅ Done")
        st.stop()
    if "finished" not in st.session_state:
        st.session_state.finished = False
        st.stop()


        # st.session_state.Done = True
        # st.rerun()
        # st.stop()

    st.stop()


# --- When Finish 


# --- When Finish is clicked ---
if "finish" in params:
    st.markdown(
        """
        <style>
        .finish-text {
            color: white;
            text-align: center;
            font-size: 26px;
            margin-top: 100px;
            font-family: 'Vazirmatn', sans-serif;
            direction: rtl;
        }
        </style>
        <p class="finish-text">❌ عذر می خوام</p>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

# --- Default (first page) ---
text1 = "سلام! اگر سینگل هستید لطفا دکمه"
text2 = "Next"
text3 = "و در غیر این صورت من عذر می‌خوام و این کاغذ رو آتیش بزنید."

st.markdown(
    f"""
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap" rel="stylesheet">
    <style>
    body {{ background-color: black; }}
    .farsi-text {{
        font-family: 'Vazirmatn', sans-serif;
        font-size: 26px;
        color: white;
        direction: rtl;
        text-align: center;
        background-color: #333;
        padding: 15px;
        border-radius: 10px;
        margin-top: 80px;
    }}
    .btn {{
        color: white;
        padding: 14px 32px;
        font-size: 18px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
        box-shadow: 0 5px 0 0 #000;
        text-decoration: none;
        display: inline-block;
    }}
    .green-btn {{
        background-color: #4CAF50;
        box-shadow: 0 5px 0 0 #2e7d32;
    }}
    .green-btn:hover {{
        background-color: #45a049;
        transform: translateY(-2px);
    }}
    .red-btn {{
        background-color: #f44336;
        box-shadow: 0 5px 0 0 #b71c1c;
    }}
    .red-btn:hover {{
        background-color: #d32f2f;
        transform: translateY(-2px);
    }}
    .buttons-container {{
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 40px;
    }}
    </style>

    <p class="farsi-text">🌸 {text1} <b>{text2}</b> {text3}</p>

    <div class="buttons-container">
        <a class="btn green-btn" href="?next=1">Next</a>
        <a class="btn red-btn" href="?finish=1">Finish</a>
    </div>
    """,
    unsafe_allow_html=True,
)


