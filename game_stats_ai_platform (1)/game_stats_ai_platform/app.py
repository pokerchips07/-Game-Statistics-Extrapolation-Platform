
from analytics.predictor import predict_next_score
from gui.dashboard import launch_dashboard

if __name__ == "__main__":
    print("Launching Game Statistics AI Platform")
    prediction = predict_next_score([12, 15, 14, 18, 20])
    print(f"Predicted next score: {prediction}")
    launch_dashboard()
