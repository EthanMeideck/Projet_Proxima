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
                    coordinates (list): Current ISS coordinates as [latitude, longitude].
        
        """
        pass

if __name__ == "__main__":
    p = ProximaProject()
    print(p.iss_tracking.__doc__)