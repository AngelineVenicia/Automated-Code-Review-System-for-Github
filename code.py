import streamlit as st
import requests
import os
import base64
import json
# Function to retrieve the repository details and process PRs
# Get all closed PRs from the repository
# Get review comments for a specific PR
# Get modified files for a specific PR (files listed in the "Files changed" section)
# Get the new version of a file (the code) based on the commit SHA
# function to fetch PR data (closed PRs, review comments by the reviewer, and modified code)
# Fetch Review Comments (Only comment body, no commenter name)
# Fetch Modified Files and their new version (Only code content)
# Streamlit UI setup
st.title("GitHub PR File Retriever")

# User inputs
repo_owner = st.text_input("Enter Repository Owner (e.g., username)", "")
repo_name = st.text_input("Enter Repository Name (e.g., repository)", "")
github_token = st.text_input("Enter GitHub Personal Access Token", type="password")

# Define the button behavior
if st.button("Retrieve Files"):
    if repo_owner and repo_name and github_token:
        with st.spinner('Retrieving files...'):
            try:
                # Fetch PR data
                pr_data = get_review_comments_and_code(repo_owner, repo_name, github_token)

                # Save the PR data as JSON files (the original code logic remains)
                for pr in pr_data:
                    filename = f"pr_{pr['pr_number']}_review_comments_and_code.json"
                    with open(filename, mode="w", encoding="utf-8") as file:
                        json.dump(pr, file, indent=4)

                # Once files are saved, display message
                st.success("Files retrieved and saved successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide all required inputs!")
