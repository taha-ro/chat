    if st.button("Done"):
        if st.session_state.Done:
            st.empty()  # clears existing elements
            A='your name:' + her_name + '-- your id:'+ str(connection)  
            st.write(her_name)
            st.write("✅ Done")
            st.stop()
