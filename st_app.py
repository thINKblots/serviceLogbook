import streamlit as st
# Import the functions we just made from the other file
import log_manager

# --- Page Setup ---
# 'st.set_page_config' should be the first Streamlit command
st.set_page_config(page_title="Service Logbook", layout="centered")

# --- Load Data ---
# We load the logbook *once* at the start of the script
logbook = log_manager.load_logbook()

# --- App Title ---
# st.title() puts a big title at the top
st.title("⚙️ Command-Line Service Logbook")

# --- Sidebar Menu ---
# st.sidebar.radio creates a navigation menu in a sidebar
menu_choice = st.sidebar.radio(
    "Navigation Menu",
    ["Add New Log", "View All Logs", "Delete a Log"]
)

# --- "Add New Log" Page Logic ---
if menu_choice == "Add New Log":
    st.header("Add a New Service Log")
    
    # 'st.form' creates a "form" that groups inputs
    # This waits until the "Submit" button is pressed.
    with st.form(key="add_log_form"):
        # st.text_input replaces your 'input()'
        machine = st.text_input("Machine Details")
        issue = st.text_area("Describe Issue/Complaint") # text_area is bigger
        correction = st.text_area("Describe Work Performed")
        
        # st.form_submit_button is the button for the form
        submit_button = st.form_submit_button(label="Save Log Entry")

        # This 'if' block only runs when the button is clicked
        if submit_button:
            if machine and issue and correction:
                # Create the new entry dictionary
                new_log_entry = {
                    "machine": machine,
                    "issue": issue,
                    "correction": correction
                }
                # Append to our in-memory list
                logbook.append(new_log_entry)
                
                # Save the *updated* list back to the JSON file
                if log_manager.save_logbook(logbook):
                    st.success("Log entry saved successfully!")
                else:
                    st.error("Failed to save log entry.")
            else:
                st.warning("Please fill out all fields.")

# --- "View All Logs" Page Logic ---
elif menu_choice == "View All Logs":
    st.header("All Service Logs")
    
    if not logbook:
        st.info("No log entries found.")
    else:
        # We loop through the list *backwards* to show newest first
        for i, log in enumerate(reversed(logbook)):
            # 'st.expander' is a nice collapsable box
            with st.expander(f"Entry #{len(logbook) - i}: {log['machine']}"):
                st.markdown(f"**Issue:** {log['issue']}")
                st.markdown(f"**Correction:** {log['correction']}")

# --- "Delete a Log" Page Logic ---
elif menu_choice == "Delete a Log":
    st.header("Delete a Log Entry")
    
    if not logbook:
        st.info("No log entries to delete.")
    else:
        st.warning("Warning: Deletions are permanent.")
        
        # Loop through and create a "delete" button for each entry
        # We loop backwards (reversed) so our index doesn't get messed up
        # when we delete an item.
        for i, log in enumerate(reversed(logbook)):
            # This is the actual index in the *original* list
            original_index = len(logbook) - 1 - i 
            
            st.subheader(f"Entry #{original_index + 1}: {log['machine']}")
            st.markdown(f"**Issue:** {log['issue']}")
            
            # We must give each button a *unique* 'key'
            # This is how Streamlit tells them apart.
            if st.button(f"Delete This Entry", key=f"delete_{original_index}"):
                
                # Use .pop() to remove the item from the list
                logbook.pop(original_index)
                
                # Save the modified list
                if log_manager.save_logbook(logbook):
                    st.success(f"Deleted entry #{original_index + 1}.")
                    # 'st.experimental_rerun()' forces the page to reload
                    # so the deleted item disappears immediately.
                    st.experimental_rerun()
                else:
                    st.error("Failed to save after deletion.")
                
            st.markdown("---") # A horizontal line