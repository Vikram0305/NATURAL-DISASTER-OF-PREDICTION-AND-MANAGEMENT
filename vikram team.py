import random

# Constants
MAGNITUDE_THRESHOLD = 5.0
HISTORY_LENGTH = 10

# History arrays
magnitude_history = [0.0] * HISTORY_LENGTH
prediction_history = [False] * HISTORY_LENGTH

# Function to simulate seismic magnitude
def get_current_seismic_magnitude():
    return 1 + 9 * random.random()  # Generates a float between 1.0 and 10.0

# Function to predict earthquake risk
def predict_earthquake():
    global magnitude_history, prediction_history

    current_magnitude = get_current_seismic_magnitude()

    # Shift the history to the right
    for i in range(HISTORY_LENGTH - 1, 0, -1):
        magnitude_history[i] = magnitude_history[i - 1]
        prediction_history[i] = prediction_history[i - 1]

    # Insert new values
    magnitude_history[0] = current_magnitude
    prediction = current_magnitude >= MAGNITUDE_THRESHOLD
    prediction_history[0] = prediction

    return prediction

# Function to print history
def print_prediction_history():
    print("\nPrediction History (most recent first):")
    for i in range(HISTORY_LENGTH):
        status = "High risk of earthquake" if prediction_history[i] else "Low risk of earthquake"
        print(f"Magnitude: {magnitude_history[i]:.2f} - Prediction: {status}")

# Main simulation
if __name__ == "__main__":
    for _ in range(HISTORY_LENGTH):
        prediction = predict_earthquake()
        print(f"New seismic reading: Magnitude {magnitude_history[0]:.2f}")
        if prediction:
            print("⚠️ Warning: High risk of earthquake!")
        else:
            print("✅ Status: Low risk of earthquake.")

    print_prediction_history()
