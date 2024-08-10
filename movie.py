import streamlit as st
import pandas as pd

# Sample data for movies, showtimes, and available seats
movies = {
    "Movie A": ["10:00 AM", "1:00 PM", "4:00 PM"],
    "Movie B": ["11:00 AM", "2:00 PM", "5:00 PM"],
    "Movie C": ["12:00 PM", "3:00 PM", "6:00 PM"]
}

seats = 50  # Total number of seats available per show

# Initialize booking records
if "booking_data" not in st.session_state:
    st.session_state.booking_data = pd.DataFrame(columns=["Movie", "Time", "Seats Booked"])

# Streamlit App
st.title("Movie Show Booking App")

# Select a movie
movie_selected = st.selectbox("Select a Movie:", list(movies.keys()))

# Select a showtime based on the selected movie
time_selected = st.selectbox("Select a Showtime:", movies[movie_selected])

# Number of seats to book
seats_to_book = st.number_input("Number of Seats:", min_value=1, max_value=seats)

# Check availability
booked_seats = st.session_state.booking_data[(st.session_state.booking_data["Movie"] == movie_selected) & 
                                             (st.session_state.booking_data["Time"] == time_selected)]["Seats Booked"].sum()

remaining_seats = seats - booked_seats

st.write(f"Remaining Seats: {remaining_seats}")

# Book seats
if st.button("Book Now"):
    if seats_to_book <= remaining_seats:
        new_booking = {"Movie": movie_selected, "Time": time_selected, "Seats Booked": seats_to_book}
        st.session_state.booking_data = st.session_state.booking_data.append(new_booking, ignore_index=True)
        st.success(f"Successfully booked {seats_to_book} seats for {movie_selected} at {time_selected}.")
    else:
        st.error("Not enough seats available.")

# Display booking history
st.subheader("Booking History")
st.table(st.session_state.booking_data)

