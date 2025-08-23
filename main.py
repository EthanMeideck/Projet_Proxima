from time import sleep
import requests

class ProximaProject:
    """
    Main application class for the ProximaProject.
    This class provides all the functions to run the application. 

    Notes:
        This class relies on 'time' and 'requests' libraries.
    """

    ISS_TRACKING_URL = "http://api.open-notify.org/iss-now.json"

    def iss_tracking(self):
        """
        Track the International Space Station with it's latitude and longitude.

            Return:
                    Coordinates (list): Current ISS coordinates as [latitude, longitude].
        
        """

        iss_tracking_response = requests.get(self.ISS_TRACKING_URL)
        
        if iss_tracking_response.status_code == 200:
            iss_tracking_data = iss_tracking_response.json()
            self.iss_longitude = iss_tracking_data["iss_position"]["longitude"]
            self.iss_latitude = iss_tracking_data["iss_position"]["longitude"]

        else:
            print(f"Error {iss_tracking_response.status_code}")
            

if __name__ == "__main__":
    p = ProximaProject()
    print(p.iss_tracking())