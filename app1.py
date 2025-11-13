import streamlit as st
import json

# from user_agent import generate_user_agent, generate_navigator
# inf=generate_user_agent()



# Convert JSON string → dict
# data = json.loads(inf)

# st.title("Detect Device Type")


# Get user agent via JS
# print(type(inf))
# print('s')
# print(str(inf))
# print(inf["navigator_id"])


if "Done" not in st.session_state:
    st.session_state.Done = False

st.set_page_config(page_title="Farsi Buttons", layout="centered")

params = st.query_params

# --- When Next is clicked ---
if "next" in params:
    if st.session_state.Done:
        st.empty()  # clears existing elements
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
    name = st.text_input("", placeholder="یک راه ارتباطی هرچی که راحت هستید برای هماهنگی یه قرار کافه (id- eamil -number): ")
    name2 = st.text_input("", placeholder=" اگه صحبتی دارید ")
    b0=st.button('send')
    if b0:
        st.write('sended')
    b1=st.button('my connection')
    if b1:
        st.write('telegram id: @Ro_Taha')
    # st.markdown("<br><a href='?'>🔙 finish</a>", unsafe_allow_html=True)
    # st.markdown(
    # """
    # <a href='?' style='
    #     display:inline-block;
    #     padding:10px 20px;
    #     background-color:green;
    #     color:white;
    #     text-decoration:none;
    #     border-radius:10px;
    # '>🎉 done</a>
    # """,
    # unsafe_allow_html=True
    # )
    if "finished" not in st.session_state:
        st.session_state.finished = False

    # If user already clicked Done, show empty page
    # if st.session_state.finished:
    #     st.markdown(
    #         "<body style='background-color:black;'></body>",
    #         unsafe_allow_html=True
    #     )
    #     st.stop()

    # Normal page content


    if st.button("Done"):
        st.session_state.Done = True
        # json_string = json.dumps(data)
        # st.write(json_string)
        st.rerun()

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


#-----------------------------------------
# pip install qrcode[pil]
# import qrcode

# # Your web address
# url = "https://www.example.com"

# # Generate QR code
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(url)
# qr.make(fit=True)

# # Create an image
# img = qr.make_image(fill_color="black", back_color="white")

# # Save the image
# img.save("my_qrcode.png")

# # my page
# st.write(hi)
# b_finish=st.button('finish')
# if b_finish:
#   #the page clear and write finish