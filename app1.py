import streamlit as st
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
        # if not Insert_table.TABLE_CREATED:
        #     cur.execute("""
        #         CREATE TABLE IF NOT EXISTS connect(
        #             id TEXT PRIMARY KEY,
        #             name TEXT,
        #             text TEXT
        #         );
        #     """)
        #     Insert_table.TABLE_CREATED = True

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





st.set_page_config(page_title="connection", layout="centered")

params = st.query_params

if "page" not in st.session_state:
    st.session_state.page = "home"

# if st.session_state.page = "Done":
#     st.empty()
#     # st.rerun()
#     st.write("✅ Done!")
#     st.stop
# --- When Next is clicked ---
if "next" in params:
    her_name=' '
    connection=' '
    st.session_state.page='next'
    if st.session_state.page != "Done":
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
        her_name=str(st.text_input("name", placeholder="name:", label_visibility="hidden"))
        connection = str(st.text_input("connection", placeholder="یک راه ارتباطی هرچی که راحت هستید برای هماهنگی یه قرار کافه (id- eamil -number): ", label_visibility="hidden"))
        text_main =str(st.text_input("text", placeholder=" اگه صحبتی دارید ",  label_visibility="hidden"))

        b0=st.button('send')
        if b0:
            Insert_table(connection,her_name ,text_main)
            state=Insert_table.status(connection,her_name ,text_main)
            st.write(state)

        b1=st.button('my connection')
        if b1:
            st.write('telegram id: @Ro_Taha')
            print(her_name)

        b2=st.button("Done")
        if b2:
            st.session_state.page = "Done"
            st.write('your name : '+ her_name + ' --   your connection : '+connection)
            st.write("✅ Done!")
            st.stop()
        
    if "finished" not in st.session_state:
        st.session_state.finished = False
        st.stop()
    st.stop()
    


# --- When Finish 
# --- When Finish is clicked ---

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





