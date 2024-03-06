import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

column_names = ["reliability", "communication", "listener", "partiicpation", "comfort", "cooperation", "flexibility", "commitment", "problem_solving", "respect"]

# Function to initialize session state
def init_session_state():
    if 'answers_submitted' not in st.session_state:
        st.session_state.answers_submitted = False
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []

# Function to ask user to submit answers
def ask_user_to_submit():
    st.write("Please submit your answers to the question.")
    # Add your question and scale inputs here
    reliable = st.slider("Are your teammates reliable?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    communication = st.slider("Are you able to communicate your ideas to others?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    listener = st.slider("Do you feel others listen to your ideas?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    participation = st.slider("Is everybody actively participating?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    comfort = st.slider("Do you feel comfortable in sharing your knowledge with others?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    cooperation = st.slider("Are you able to work well with the others?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    flexibility = st.slider("Can you and the others adjust to sudden changes?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    commitment = st.slider("Do you feel others are committed to the work?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    problem_solving = st.slider("Are others able to focus on solutions?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    respect = st.slider("Do you feel respected?", 1, 5, step=1, help="1=strongly agree;2=agree;3=neutral;4=disagree;5=strongly disagree")
    submit_button = st.button("Submit Answers")
    
    if submit_button:
        # Save answers or perform any other necessary actions
        # In this example, just set answers_submitted to True
        st.session_state.answers_submitted = True
        st.session_state.user_answers = [reliable, communication, listener, participation, comfort, cooperation, flexibility, commitment, problem_solving, respect]
        save_to_csv()

# Function to show statistics
def show_statistics():
    total  = 10*5
    user_sum = sum(st.session_state.user_answers)
    percentage = user_sum/total * 100
    st.write("You are", round(percentage, 2), "% satisfied with the teamwork.")

    submissions = read_csv_to_df()
    row_averages = submissions.sum(axis=1) / total
    overall_average = row_averages.mean() * 100
    st.write("Average employee satisfaction with the teamwork is ", round(overall_average, 2), "%")

    data_sorted, labels_sorted = zip(*sorted(zip(st.session_state.user_answers, column_names), reverse=False))

    col_ave = submissions.mean()
    data_sorted2, labels_sorted2 = zip(*sorted(zip(col_ave, column_names), reverse=False))

    fig, ax = plt.subplots(1, 2, figsize=(12,6))

    ax[0].bar(labels_sorted, data_sorted)
    ax[0].set_xlabel('Qualities')
    ax[0].set_ylabel('Score')
    ax[0].set_title("Your teamwork evaluation")
    ax[0].tick_params(axis='x', rotation=90)

    ax[1].bar(labels_sorted2, data_sorted2)
    ax[1].set_xlabel('Qualities')
    ax[1].set_ylabel('Score')
    ax[1].set_title("Average teamwork evaluation")
    ax[1].tick_params(axis='x', rotation=90)

    st.pyplot(fig)

# Function to save answers to CSV file
def save_to_csv():
    df = pd.DataFrame([st.session_state.user_answers])
    df.to_csv('submissions.csv', mode='a', header=not st.session_state.answers_submitted, index=False)

# Function to read CSV file and convert to DataFrame
def read_csv_to_df():
    try:
        df = pd.read_csv('submissions.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=column_names)
    return df

# Main function
def main():
    init_session_state()

    if not st.session_state.answers_submitted:
        submission = ask_user_to_submit()
    else:
        show_statistics()

if __name__ == "__main__":
    main()
