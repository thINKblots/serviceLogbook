import streamlit as st
import log_manager

# Page setup
st.set_page_config(page_title="Service Logbook", layout="centered")

# Load data
logbook = log_manager.load_logbook()

# App title
st.title("⚙️ Service Logbook")

# Navigation menu
menu_choice = st.sidebar.radio(
    "Navigation Menu",
    ["Add New Log", "View All Logs", "Delete a Log"]
)

# Add new log
if menu_choice == "Add New Log":
    st.header("Add a New Service Log")

    with st.form(key="add_log_form"):
        machine = st.text_input("Machine Details")
        issue = st.text_area("Describe Issue/Complaint")
        correction = st.text_area("Describe Work Performed")

        submit_button = st.form_submit_button(label="Save Log Entry")

        if submit_button:
            if machine and issue and correction:
                new_log_entry = {
                    "machine": machine,
                    "issue": issue,
                    "correction": correction
                }
                logbook.append(new_log_entry)

                if log_manager.save_logbook(logbook):
                    st.success("Log entry saved successfully!")
                else:
                    st.error("Failed to save log entry.")
            else:
                st.warning("Please fill out all fields.")

# View all logs
elif menu_choice == "View All Logs":
    st.header("All Service Logs")

    if not logbook:
        st.info("No log entries found.")
    else:
        for i, log in enumerate(reversed(logbook)):
            with st.expander(f"Entry #{len(logbook) - i}: {log['machine']}"):
                st.markdown(f"**Issue:** {log['issue']}")
                st.markdown(f"**Correction:** {log['correction']}")

# Delete a log
elif menu_choice == "Delete a Log":
    st.header("Delete a Log Entry")

    if not logbook:
        st.info("No log entries to delete.")
    else:
        st.warning("Warning: Deletions are permanent.")

        for i, log in enumerate(reversed(logbook)):
            original_index = len(logbook) - 1 - i

            st.subheader(f"Entry #{original_index + 1}: {log['machine']}")
            st.markdown(f"**Issue:** {log['issue']}")

            if st.button(f"Delete This Entry", key=f"delete_{original_index}"):
                logbook.pop(original_index)

                if log_manager.save_logbook(logbook):
                    st.success(f"Deleted entry #{original_index + 1}.")
                    st.experimental_rerun()
                else:
                    st.error("Failed to save after deletion.")

            st.markdown("---")
