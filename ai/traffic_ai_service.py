
from ai.predictor import TrafficPredictor
from ai.traffic_data_collector import TrafficDataCollector


class TrafficAIService:
    """Connects traffic data collection with the trained AI model."""

    def __init__(self, model_path="ai/traffic_model.pkl"):
        self.predictor = TrafficPredictor(model_path)

    def analyse_intersection(self, intersection):
        observations = TrafficDataCollector.collect(intersection)

        predictions = []

        for observation in observations:
            result = self.predictor.predict(observation)

            predictions.append({
                "intersection_id": observation["intersection_id"],
                "road_id": observation["road_id"],
                "vehicle_count": observation["vehicle_count"],
                "density_percentage": observation["density_percentage"],
                "congestion_level": result["congestion_level"],
                "confidence": result["confidence"]
            })

        return predictions

    @staticmethod
    def display_predictions(predictions):
        print("\n==============================================")
        print("       AI TRAFFIC CONGESTION ANALYSIS")
        print("==============================================")

        for prediction in predictions:
            print(
                f"\nRoad: {prediction['road_id']}"
                f"\nVehicles: {prediction['vehicle_count']}"
                f"\nDensity: {prediction['density_percentage']}%"
                f"\nAI Congestion: {prediction['congestion_level']}"
                f"\nConfidence: {prediction['confidence']}%"
            )

        print("\n==============================================")


if __name__ == "__main__":
    print("Traffic AI service module loaded successfully.")
