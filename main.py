from time import sleep
import requests

class ProximaProject:
    """
    Main application class for the ProximaProject.
    This class provides all the functions to run the application. 

    Notes:
        This class relies on 'time' and 'requests' libraries.
    """

    def iss_tracking(self):
        """
        Track the International Space Station with it's latitude and longitude.

            Return:
                    Coordinates (list): Current ISS coordinates as [latitude, longitude].
        
        """

        ISS_TRACKING_URL = "http://api.open-notify.org/iss-now.json"
        self.iss_location = []

        # Fetch request response
        iss_tracking_response = requests.get(ISS_TRACKING_URL)
        
        # Response status code verification
        if iss_tracking_response.status_code == 200:
            # Fetch the current location
            iss_tracking_data = iss_tracking_response.json()
            iss_longitude = iss_tracking_data["iss_position"]["longitude"]
            iss_latitude = iss_tracking_data["iss_position"]["latitude"]

            # Adding longitude & lattitude in a list
            self.iss_location.append(iss_longitude)
            self.iss_location.append(iss_latitude)

            return self.iss_location

        else:
            print(f"Error {iss_tracking_response.status_code}")
            
if __name__ == "__main__":
    p = ProximaProject()
    p.iss_tracking()